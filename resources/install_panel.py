#!/usr/bin/env python3
"""
THE SHUFFLER - Panel Installer
Compiles binaries, rewrites the panel config with the correct app path,
and walks the user through setup. Run this once on any new machine.
"""

import os
import shutil
import subprocess
import sys
import time
import re
from pathlib import Path

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout, result.stderr

def main():
    script_dir = Path(__file__).parent.resolve()
    root_dir = script_dir.parent.resolve()
    app_path = root_dir / "THE SHUFFLER.app"
    config_source = script_dir / "home_panel.ascconfig"
    config_temp = Path("/tmp/THE_SHUFFLER_install.ascconfig")
    setwallpaper_src = script_dir / "setwallpaper.swift"
    setwallpaper_bin = script_dir / "setwallpaper"
    build_script = script_dir / "build_apps.sh"

    print("THE SHUFFLER — Installer")
    print("=" * 40)
    print()

    # ── STEP 1: compile setwallpaper ──
    print("[ 1 / 3 ] Compiling wallpaper engine...")
    if setwallpaper_src.exists():
        code, out, err = run(f'swiftc "{setwallpaper_src}" -o "{setwallpaper_bin}"')
        if code != 0:
            print(f"  ERROR compiling setwallpaper:\n{err}")
            input("\nPress Enter to exit...")
            sys.exit(1)
        print("  Done.")
    else:
        print("  setwallpaper.swift not found — skipping (using existing binary if present)")

    # ── STEP 2: build .app bundles ──
    print("[ 2 / 3 ] Building apps...")
    if build_script.exists():
        code, out, err = run(f'bash "{build_script}"', cwd=str(script_dir))
        if code != 0:
            print(f"  ERROR building apps:\n{err}")
            input("\nPress Enter to exit...")
            sys.exit(1)
        print("  Done.")
    else:
        print("  build_apps.sh not found — skipping (using existing apps if present)")

    # ── STEP 3: rewrite panel config ──
    print("[ 3 / 3 ] Configuring panel...")

    if not app_path.exists():
        print(f"  ERROR: Could not find THE SHUFFLER.app at:\n  {app_path}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    if not config_source.exists():
        print(f"  ERROR: Could not find home_panel.ascconfig at:\n  {config_source}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    if config_temp.exists():
        shutil.rmtree(config_temp)
    shutil.copytree(config_source, config_temp)

    plist_path = config_temp / "Contents" / "Resources" / "PanelDefinitions.plist"
    with open(plist_path, "r", encoding="utf-8") as f:
        content = f.read()

    old_pattern = r'(<key>Path</key>\s*<string>)[^<]*(</string>)'
    new_content = re.sub(old_pattern, rf'\g<1>{app_path}\g<2>', content)

    with open(plist_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("  Done.")
    print()
    print("=" * 40)
    print("SETUP COMPLETE — NEXT STEPS:")
    print()
    print("  1. Go to System Settings > Accessibility > Keyboard")
    print("  2. Turn ON Accessibility Keyboard")
    print("  3. Click 'Panel Editor...'")
    print("  4. In Panel Editor: File > Import Panels")
    print("  5. Navigate to the resources folder inside THE_SHUFFLER")
    print("     and select 'home_panel.ascconfig'")
    print("  6. Press Cmd+S to save")
    print("  7. THE SHUFFLER button will appear in your Accessibility Keyboard")
    print()
    print(f"  Config location: {config_source}")
    print("=" * 40)
    print()
    print("Opening System Settings in 5 seconds...")

    time.sleep(5)
    subprocess.Popen([
        "open",
        "x-apple.systempreferences:com.apple.preference.universalaccess"
    ])

    input("\nPress Enter to exit the installer...")

if __name__ == "__main__":
    main()
