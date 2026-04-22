# THE SHUFFLER

click. shuffle. repeat.

---

THE SHUFFLER is a single-purpose wallpaper randomizer that lives in your macOS Accessibility Keyboard. No app running in the background. No daemon. No CPU drain. It does exactly one thing — and only when you tell it to.

Think of it as a fidget toy for your desktop. Waiting for a page to load? Click it. Waiting for a file to export? Click it. Just need something to do with your hands while your brain is doing seventeen other things? Click it. Each press fires a new random wallpaper and a little sound. That's it. That's the whole app.

Built for the ADHD/autistic brain that needs just a little something to do while the computer catches up.

---

## WHAT'S INSIDE

```
THE_SHUFFLER/
├── THE SHUFFLER.app     — the button. double-click to test it anytime
├── Install.app          — run this first on any new machine
├── resources/           — the engine. don't move anything out of here
└── wallpaper images/    — your images live here. swap them out anytime
```

**resources/** contains the scripts, binaries, sound file, and panel config that make everything work. You don't need to touch anything in here — but it needs to stay in the same folder as the apps.

**wallpaper images/** is yours. Delete the included images, drop in your own JPGs, PNGs, or TIFFs, and THE SHUFFLER will pick from whatever is in there.

---

## GETTING STARTED

### 1. Clone the repo
```bash
git clone https://github.com/thebuttoncollection/theshuffler.git ~/Desktop/the_shuffler && cd ~/Desktop/the_shuffler && bash resources/build_apps.sh
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

---

## REQUIREMENTS

- macOS Sequoia (15.x) or later
- Xcode Command Line Tools — install with: `xcode-select --install`
- macOS will ask for permission to access your Desktop folder and System Events the first time — click Allow

---

## MOVING THE FOLDER

Move the whole folder anywhere you want, then run **Install.app** again. Everything reconfigures itself automatically.

---

*one button. one job. zero background processes.*
