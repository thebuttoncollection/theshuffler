import AppKit
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: setwallpaper <image_path>")
    exit(1)
}

let imagePath = CommandLine.arguments[1]
let imageURL = URL(fileURLWithPath: imagePath)

guard FileManager.default.fileExists(atPath: imagePath) else {
    print("File not found: \(imagePath)")
    exit(1)
}

let workspace = NSWorkspace.shared
let screens = NSScreen.screens

for screen in screens {
    try? workspace.setDesktopImageURL(imageURL, for: screen, options: [:])
}

RunLoop.main.run(until: Date(timeIntervalSinceNow: 0.25))

exit(0)
