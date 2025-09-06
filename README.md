# 🖥️ ToDoListWallpaper for macOS

A simple yet powerful Python utility that turns a plain text file (`tasks.txt`) into your **dynamic desktop wallpaper**.  
Keep your to-do list front and center by having it automatically update on your screen every time you log in.

---

## ✨ Features
- **Plain Text Simplicity**: Manage your to-do list in a simple `tasks.txt` file. No special software needed.  
- **Automatic Image Generation**: Reads your text file and generates a clean, minimalist wallpaper image.  
- **Fully Customizable**: Change background color, text color, font, and font size directly in the script.  
- **Set-and-Forget Automation**: Runs automatically whenever you log in to your Mac.  

---

## ⚙️ How It Works
- The project consists of a single Python script (`app.py`) that uses the **Pillow** library to create an image from your text file.  
- It then uses **AppleScript** to set this image as your desktop background.  
- The automation is handled by **launchd**, macOS's built-in service manager, which triggers the script at every user login.  

---

## 📋 Prerequisites
Make sure you have:
- macOS (script is macOS-only)  
- Python 3 (macOS includes Python, but a recent version is recommended)  
- [Homebrew](https://brew.sh/) (optional but recommended for Mac developers)  

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository
```bash
cd ~
git clone https://github.com/your-username/ToDoListWallpaper.git
cd ToDoListWallpaper
```

### Step 2: Install Dependencies
The script requires the **Pillow** library:
```bash
pip3 install Pillow
```

### Step 3: Create Your To-Do List
```bash
touch tasks.txt
```
Now open `tasks.txt` in a text editor and add your to-do items.

### Step 4: Customize the Script (Optional)
At the top of `app.py` you can change the wallpaper appearance:
```python
# --- 🎨 CUSTOMIZE YOUR WALLPAPER HERE ---
TASKS_FILE = "tasks.txt"
OUTPUT_WALLPAPER = "current_tasks_wallpaper.png"
IMAGE_WIDTH = 3840      # Adjust to your screen resolution
IMAGE_HEIGHT = 2160     # Adjust to your screen resolution
BACKGROUND_COLOR = "#1c1c1c"
TEXT_COLOR = "#d0d0d0"
FONT_SIZE = 60
FONT_PATH = "/System/Library/Fonts/Supplemental/HelveticaNeue.ttc"
# -----------------------------------------
```

---

## ⚡ Automation: Run on Login

For the best experience, use a **launchd Agent** to run the script every time you log in.

### 1. Create the launchd Configuration File
```bash
mkdir -p ~/Library/LaunchAgents
nano ~/Library/LaunchAgents/com.user.taskwallpaper.plist
```

### 2. Add the Configuration
Paste this:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.taskwallpaper</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Library/Frameworks/Python.framework/Versions/3.13/bin/python3</string>
        <string>/Users/pranavkothapalli/ToDoListWallpaper/app.py</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>WorkingDirectory</key>
    <string>/Users/pranavkothapalli/ToDoListWallpaper</string>

    <key>StandardErrorPath</key>
    <string>/Users/pranavkothapalli/ToDoListWallpaper/wallpaper_agent.log</string>
    
    <key>StandardOutPath</key>
    <string>/Users/pranavkothapalli/ToDoListWallpaper/wallpaper_agent.log</string>
</dict>
</plist>
```

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

### 3. Load the Service
```bash
launchctl load ~/Library/LaunchAgents/com.user.taskwallpaper.plist
```

---

## 📌 Usage
- Edit your `tasks.txt` anytime to update your to-do list.  
- Log out and log back in — your wallpaper will refresh automatically.  

---

## 🛠️ Troubleshooting
- **Permissions**: Grant *Full Disk Access* to your terminal or editor (`System Settings > Privacy & Security > Full Disk Access`).  
- **Paths**: Double-check Python and script paths in `.plist`.  
- **Logs**: Check `wallpaper_agent.log` inside your project folder if something fails.  
- **Check launchd Status**:
```bash
launchctl list | grep com.user.taskwallpaper
```

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/your-username/ToDoListWallpaper/issues).

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
