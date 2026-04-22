# THE SHUFFLER (macOS)
A fidget-widget for your macOS desktop.
Built for the ADHD brain that needs something to do while the computer catches up. It's a single-purpose wallpaper randomizer that lives in your macOS Accessibility Keyboard. No background processes. No daemon or helpers. Virtually no CPU drain. Fires once and dies.
---
## WHAT'S INSIDE
```
THE_SHUFFLER/
├── THE SHUFFLER.app     — the button. double-click to test it anytime
├── Install.app          — run this once on any new machine
├── resources/           — the engine. don't move anything out of here
└── wallpaper images/    — your images live here. swap them out anytime
```
**resources/** contains the scripts, binaries, sound file, and panel config that make everything work. You don't need to touch anything in here — but it needs to stay in the same folder as the apps.
**wallpaper images/** is yours. Delete the included images, drop in your own JPGs, PNGs, or TIFFs, and THE SHUFFLER will pick from whatever is in there.
---
## GETTING STARTED
### 1. Clone the repo
```bash
git clone https://github.com/thebuttoncollection/theshuffler.git && cd theshuffler && bash resources/build_apps.sh
```
Or download the ZIP from GitHub and run:
```bash
bash resources/build_apps.sh
```
### 2. Run the installer
Double-click **Install.app**.
> If macOS says the app can't be opened: right-click → Open → Open anyway. This is a Gatekeeper warning for unsigned apps — it's safe to proceed.
A Terminal window will open and walk you through everything. It will:
- Compile the necessary components for your machine
- Configure the panel button with the correct file paths
- Open System Settings to the right place when ready
### 3. Set up the Accessibility Keyboard
Follow the steps in the Terminal window:
1. System Settings > Accessibility > Keyboard
2. Turn **ON** Accessibility Keyboard
3. Click **Panel Editor...**
4. File > Import Panels
5. Navigate to the **resources** folder and select **home_panel.ascconfig**
6. Press **Cmd+S** to save
7. THE SHUFFLER button will appear in your floating keyboard
### 4. Use it
Click the button in your Accessibility Keyboard whenever you feel like it. Each click plays a sound and shuffles to a new random wallpaper. Rapid fire is encouraged.
---
## SWAPPING YOUR WALLPAPERS
Open the **wallpaper images** folder and replace the images with whatever you want. Any JPG, JPEG, PNG, TIFF, or BMP will work. No limit on how many you add. The more the better.
---
## SWAPPING THE SOUND
Replace **resources/the_sound.aiff** with any AIFF or WAV file. Keep the filename the same.
---
## HOW IT WORKS (the short version)
When you click the button, the Accessibility Keyboard triggers THE SHUFFLER.app. The app plays a sound, picks a random image from your wallpaper images folder, and sets it as your desktop wallpaper — then exits completely. Nothing stays running. Nothing is watching in the background. Your CPU has no idea it existed.
## BUGS
- Rapid firing can occasionally outrun the app. You might hear the click sound but the wallpaper doesn't change. If that happens, just click again and it will catch up.
- Make sure the image extensions are lowercase (png vs PNG, jpg vs JPG). For some reason this ensures the images work on my end.
---
## REQUIREMENTS
- macOS Sequoia (15.x) or later
- Xcode Command Line Tools — install with: `xcode-select --install`
- macOS will ask for permission to access your Desktop folder and System Events the first time — click Allow
---
## MOVING THE FOLDER
Move the whole `THE_SHUFFLER` folder anywhere you want, then run **Install.app** again. Everything reconfigures itself automatically.
