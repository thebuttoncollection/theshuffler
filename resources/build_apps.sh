#!/bin/bash
# BUILD APPS FOR THE SHUFFLER
# run this once from inside THE_SHUFFLER folder to create both .app bundles
# usage: bash build_apps.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ICON_SRC="$SCRIPT_DIR/the_icon.jpg"

build_icon() {
    local APP_PATH="$1"
    if [ -f "$ICON_SRC" ]; then
        ICONSET="/tmp/the_shuffler.iconset"
        mkdir -p "$ICONSET"
        sips -z 16 16     "$ICON_SRC" --out "$ICONSET/icon_16x16.png"      > /dev/null 2>&1
        sips -z 32 32     "$ICON_SRC" --out "$ICONSET/icon_16x16@2x.png"   > /dev/null 2>&1
        sips -z 32 32     "$ICON_SRC" --out "$ICONSET/icon_32x32.png"      > /dev/null 2>&1
        sips -z 64 64     "$ICON_SRC" --out "$ICONSET/icon_32x32@2x.png"   > /dev/null 2>&1
        sips -z 128 128   "$ICON_SRC" --out "$ICONSET/icon_128x128.png"    > /dev/null 2>&1
        sips -z 256 256   "$ICON_SRC" --out "$ICONSET/icon_128x128@2x.png" > /dev/null 2>&1
        sips -z 256 256   "$ICON_SRC" --out "$ICONSET/icon_256x256.png"    > /dev/null 2>&1
        sips -z 512 512   "$ICON_SRC" --out "$ICONSET/icon_256x256@2x.png" > /dev/null 2>&1
        sips -z 512 512   "$ICON_SRC" --out "$ICONSET/icon_512x512.png"    > /dev/null 2>&1
        sips -z 1024 1024 "$ICON_SRC" --out "$ICONSET/icon_512x512@2x.png" > /dev/null 2>&1
        iconutil -c icns "$ICONSET" -o "$APP_PATH/Contents/Resources/AppIcon.icns" 2>/dev/null
        rm -rf "$ICONSET"
    fi
}

# ─────────────────────────────────────────
# 1. BUILD: THE SHUFFLER.app
# ─────────────────────────────────────────
APP1="$ROOT_DIR/THE SHUFFLER.app"
echo "Building THE SHUFFLER.app..."
[ -d "$APP1" ] && rm -rf "$APP1"
mkdir -p "$APP1/Contents/MacOS"
mkdir -p "$APP1/Contents/Resources"

cat > /tmp/launcher_shuffler.c << 'EOF'
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <mach-o/dyld.h>

int main() {
    char path[4096];
    uint32_t size = sizeof(path);
    _NSGetExecutablePath(path, &size);
    char *dir = dirname(dirname(dirname(dirname(path))));
    char script[4096];
    snprintf(script, sizeof(script), "bash \"%s/resources/the_shuffler.sh\"", dir);
    return system(script);
}
EOF
cc -o "$APP1/Contents/MacOS/launcher" /tmp/launcher_shuffler.c

cat > "$APP1/Contents/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launcher</string>
    <key>CFBundleIdentifier</key>
    <string>com.avesig.theshuffler</string>
    <key>CFBundleName</key>
    <string>THE SHUFFLER</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>LSUIElement</key>
    <true/>
</dict>
</plist>
PLIST

build_icon "$APP1"
echo "Done: THE SHUFFLER.app"

# ─────────────────────────────────────────
# 2. BUILD: Install.app
# ─────────────────────────────────────────
APP2="$ROOT_DIR/Install.app"
echo "Building Install.app..."
[ -d "$APP2" ] && rm -rf "$APP2"

# also remove old name if it exists
[ -d "$ROOT_DIR/Install Panel.app" ] && rm -rf "$ROOT_DIR/Install Panel.app"

mkdir -p "$APP2/Contents/MacOS"
mkdir -p "$APP2/Contents/Resources"

cat > /tmp/launcher_installer.c << 'EOF'
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <mach-o/dyld.h>

int main() {
    char path[4096];
    uint32_t size = sizeof(path);
    _NSGetExecutablePath(path, &size);
    char *dir = dirname(dirname(dirname(dirname(path))));
    char script[4096];
    snprintf(script, sizeof(script), "osascript -e 'tell application \"Terminal\" to do script \"python3 \\\"%s/resources/install_panel.py\\\"\"'", dir);
    return system(script);
}
EOF
cc -o "$APP2/Contents/MacOS/launcher" /tmp/launcher_installer.c

cat > "$APP2/Contents/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launcher</string>
    <key>CFBundleIdentifier</key>
    <string>com.avesig.install</string>
    <key>CFBundleName</key>
    <string>Install</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
</dict>
</plist>
PLIST

build_icon "$APP2"
echo "Done: Install.app"

# ─────────────────────────────────────────
echo ""
echo "Both apps built. Folder structure:"
echo "  THE_SHUFFLER/"
echo "  ├── THE SHUFFLER.app     <- the fidget button"
echo "  ├── Install.app          <- run this once on any new machine"
echo "  ├── resources/"
echo "  └── wallpaper images/    <- swap images here"
