#!/bin/bash
# THE SHUFFLER
# portable wallpaper shuffler + sound
# images go in: THE_SHUFFLER/wallpaper images/
# sound goes in: THE_SHUFFLER/resources/

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

SOUND="$SCRIPT_DIR/the_sound.aiff"
IMAGES_DIR="$ROOT_DIR/wallpaper images"
SETWALLPAPER="$SCRIPT_DIR/setwallpaper"
LOCKFILE="/tmp/the_shuffler.lock"
PIDFILE="/tmp/the_shuffler.pid"

# if already running, kill the previous instance and take over
if [ -f "$PIDFILE" ]; then
    OLD_PID=$(cat "$PIDFILE")
    if kill -0 "$OLD_PID" 2>/dev/null; then
        kill "$OLD_PID" 2>/dev/null
        pkill -f "the_shuffler.sh" 2>/dev/null
        pkill -f "afplay" 2>/dev/null
    fi
    rm -f "$PIDFILE" "$LOCKFILE"
fi

# write our PID and set cleanup on exit
echo $$ > "$PIDFILE"
trap 'rm -f "$LOCKFILE" "$PIDFILE"' EXIT

touch "$LOCKFILE"

# play sound immediately in background
if [ -f "$SOUND" ]; then
    afplay "$SOUND" &
fi

# collect all images into an array
IMAGES=()
while IFS= read -r -d '' file; do
    IMAGES+=("$file")
done < <(find "$IMAGES_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.tiff" -o -name "*.tif" -o -name "*.bmp" \) -print0)

COUNT=${#IMAGES[@]}
if [ "$COUNT" -eq 0 ]; then
    osascript -e 'display notification "No images found in wallpaper images folder" with title "THE SHUFFLER"'
    exit 1
fi

# pick a random image
INDEX=$(( RANDOM % COUNT ))
IMAGE="${IMAGES[$INDEX]}"

if [ ! -f "$IMAGE" ]; then
    osascript -e 'display notification "Could not find image file" with title "THE SHUFFLER"'
    exit 1
fi

# set wallpaper
"$SETWALLPAPER" "$IMAGE"

# notify
FILENAME=$(basename "$IMAGE")
osascript -e "display notification \"$FILENAME\" with title \"THE SHUFFLER\""
