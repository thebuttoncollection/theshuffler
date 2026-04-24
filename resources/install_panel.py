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

def check_dependencies():
    """Check that Xcode Command Line Tools are installed and Swift compiler matches SDK."""
    print("[ 0 / 3 ] Checking dependencies...")

    # check xcode-select
    code, out, err = run("xcode-select -p")
    if code != 0:
        print()
        print("  ERROR: Xcode Command Line Tools not found.")
        print()
        print("  Please install them by running this in Terminal:")
        print("    xcode-select --install")
        print()
        print("  Wait for the install to fully complete, restart your Mac,")
        print("  then run this installer again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    # check swiftc exists
    code, out, err = run("which swiftc")
    if code != 0:
        print()
        print("  ERROR: Swift compiler (swiftc) not found.")
        print()
        print("  Please install Xcode Command Line Tools:")
        print("    xcode-select --install")
        print()
        print("  Wait for the install to fully complete, restart your Mac,")
        print("  then run this installer again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    # check swift compiler version matches SDK
    # this catches the mismatch that causes the SwiftBridging redefinition error
    code, out, err = run("swiftc --version")
    compiler_version = out.strip()

    code2, out2, err2 = run("xcrun --sdk macosx --show-sdk-path")
    sdk_path = out2.strip()

    if not sdk_path:
        print()
        print("  ERROR: macOS SDK not found. Your Xcode Command Line Tools")
        print("  may be corrupted or mismatched with your macOS version.")
        print()
        print("  To fix, run these commands one at a time:")
        print("    sudo rm -rf /Library/Developer/CommandLineTools")
        print("    xcode-select --install")
        print()
        print("  Wait for the install to fully complete, restart your Mac,")
        print("  then run this installer again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    # do a quick compile test to catch SDK mismatch before the real compile
    test_swift = "/tmp/the_shuffler_test.swift"
    test_bin = "/tmp/the_shuffler_test"
    with open(test_swift, "w") as f:
        f.write('import Foundation\nprint("ok")\n')

    code, out, err = run(f'swiftc "{test_swift}" -o "{test_bin}"')

    # clean up test files
    for f in [test_swift, test_bin]:
        try:
            os.remove(f)
        except:
            pass

    if code != 0:
        print()
        print("  ERROR: Swift compiler and macOS SDK are mismatched.")
        print("  This usually happens after a macOS update.")
        print()
        print("  To fix, run these commands one at a time in Terminal:")
        print("    sudo rm -rf /Library/Developer/CommandLineTools")
        print("    xcode-select --install")
        print()
        print("  IMPORTANT: Wait for the popup to say 'Done' before continuing.")
        print("  Then restart your Mac and run this installer again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    print("  All good.")
    print()

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

    # ── STEP 0: check dependencies ──
    check_dependencies()

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
