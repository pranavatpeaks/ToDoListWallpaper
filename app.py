import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# --- 🎨 CUSTOMIZE YOUR WALLPAPER HERE ---
TASKS_FILE = "tasks.txt"
OUTPUT_WALLPAPER = "current_tasks_wallpaper.png"
IMAGE_WIDTH = 3840  # Adjust to your screen resolution (e.g., 1920)
IMAGE_HEIGHT = 2160 # Adjust to your screen resolution (e.g., 1080)
BACKGROUND_COLOR = "#1c1c1c" # Dark Gray
TEXT_COLOR = "#d0d0d0"       # Light Gray
FONT_SIZE = 60
# On macOS, you can find fonts in /System/Library/Fonts/
# Helvetica Neue is a good, clean default.
FONT_PATH = "/System/Library/Fonts/Supplemental/HelveticaNeue.ttc"
# -----------------------------------------

def create_wallpaper_from_text():
    """Reads text from a file and draws it onto a new image."""
    print(f"1. Reading tasks from '{TASKS_FILE}'...")
    try:
        with open(TASKS_FILE, "r") as f:
            text_content = f.read()
            if not text_content.strip():
                print("⚠️ Warning: tasks.txt is empty. Wallpaper will be blank.")
    except FileNotFoundError:
        print(f"❌ FATAL ERROR: '{TASKS_FILE}' not found. Please create it.")
        sys.exit(1)

    print("2. Creating a new wallpaper image...")
    # Create a new blank image
    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load the font
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        print("❌ FATAL ERROR: Font not found. Using default.")
        font = ImageFont.load_default()

    # Position and draw the text
    # The text will be left-aligned and vertically centered.
    draw.text(
        (IMAGE_WIDTH * 0.1, IMAGE_HEIGHT / 2), # x, y position
        text_content,
        fill=TEXT_COLOR,
        font=font,
        anchor="lm" # Anchor "left-middle"
    )

    # Save the final image
    img.save(OUTPUT_WALLPAPER)
    print(f"✅ Wallpaper image saved as '{OUTPUT_WALLPAPER}'")
    return os.path.abspath(OUTPUT_WALLPAPER)

def set_wallpaper(image_path):
    """Sets the desktop wallpaper and refreshes the Dock."""
    print("3. Setting the new wallpaper...")
    applescript = f'''
    tell application "System Events"
        tell every desktop
            set picture to POSIX file "{image_path}"
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", applescript], check=True)
    
    print("4. Refreshing the desktop...")
    subprocess.run(["killall", "Dock"], check=True)
    print("✅ Done!")


if __name__ == "__main__":
    wallpaper_path = create_wallpaper_from_text()
    if wallpaper_path:
        set_wallpaper(wallpaper_path)