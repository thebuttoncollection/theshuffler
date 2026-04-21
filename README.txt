# THE SHUFFLER

A fidget toy for your desktop.

Waiting for a page to load? Click it. Waiting for a file to export? Click it. Need something to do with your hands while your brain is doing seventeen other things? Click it. Each press fires a new random wallpaper and a little sound. That's it. That's the whole app.

Click. Shuffle. Repeat.

Built for the ADHD/autistic brain that needs just a little something to do while the computer catches up.

---

## WHAT'S INSIDE

THE_SHUFFLER/
├── THE SHUFFLER.app     — the button. double-click to test it anytime
├── Install.app          — run this first on any new machine
├── resources/           — the engine. don't move anything out of here
└── wallpaper images/    — your images live here. swap them out anytime

**Resources/** contains the scripts, binaries, sound file, and panel config that make everything work. You don't need to touch anything in here — but it needs to stay in the same folder as the apps.

**Wallpaper images/** is yours. Delete the included images, drop in your own JPGs, PNGs, or TIFFs, and THE SHUFFLER will pick from whatever is in there.

---

## GETTING STARTED

### 1. Run the installer
Double-click **Install.app**. A Terminal window will open and walk you through everything. It will:
- Compile the necessary components for your machine
- Configure the panel button with the correct file paths
- Open System Settings to the right place when ready

### 2. Set up the Accessibility Keyboard
Follow the steps in the Terminal window:
1. System Settings > Accessibility > Keyboard
2. Turn **ON** Accessibility Keyboard
3. Click **Panel Editor...**
4. File > Import Panels
5. Navigate to the **resources** folder and select **home_panel.ascconfig**
6. Press **Cmd+S** to save
7. THE SHUFFLER button will appear in your floating keyboard

### 3. Use it
Click the button in your Accessibility Keyboard whenever you feel like it. CLICK ALLOW WHEN PROMPTED. Each click plays a sound and shuffles to a new random wallpaper. Rapid fire is encouraged.

---

## SWAPPING YOUR WALLPAPERS

Open the **wallpaper images** folder and replace the images with whatever you want. Any JPG, JPEG, PNG, TIFF, or BMP will work. No limit on how many you add. The more the better. You can also swap the main image for the keyboard panel button in the resources folder to be anything you'd like.

---

## SWAPPING THE SOUND / PANEL ICON

You can find the_sound.aiff in the resources folder ad replace with whatever you like just keep the same name. You can also change the image of the "panel_icon.png" the same way.

## BUGS

- Rapid firing can occasionally outrun the app. You might hear the click sound but the wallpaper doesn’t change. If that happens, just click again — it will catch up.
- In general, very fast or repeated clicks may cause the app to briefly lag behind. Nothing breaks, it just needs a second. Also, make sure the image extensions are lowercase (png vs PNG, jpg vs JPG). For some reason this ensures the images work on my end.

---

## HOW IT WORKS

When you click the button, the Accessibility Keyboard triggers THE SHUFFLER.app. The app plays a sound, picks a random image from your wallpaper images folder, and sets it as your desktop wallpaper — then exits completely. Nothing stays running. Nothing is watching in the background. Your CPU has no idea it existed.

---

## NOTES

- The installer needs to be run once on each new machine you use it on
- Xcode Command Line Tools are required (most Macs already have these)
- macOS will ask for permission to access your Desktop folder and System Events the first time — click Allow
- To move THE_SHUFFLER folder to a new location, just move the whole folder and run Install.app again

---

## AUTHOR

Built by Avelyn (aka ave.sig)

Product Designer / Sound Engineer
