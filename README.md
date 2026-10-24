# 📁 Automatic File Organizer

A lightweight Python utility with a graphical file selection interface that automatically categorizes and organizes messy directories by file extension.

---

## 🌟 Features

- **Interactive File Selection:** Opens a native system file browser window to let you pick any folder to clean up.
- **Dynamic Categorization:** Scans files and automatically creates subfolders based on existing file extension types (e.g., `pdf`, `png`, `docx`).
- **Safe Execution:** Automatically handles filename collisions by appending unique numbers (e.g., `document_1.pdf`) to avoid overwriting existing files.
- **Standalone Executable Support:** Can be compiled into a single `.exe` file that runs on any Windows PC without needing Python installed.

---

## 🚀 How to Run (Python)

### Prerequisites
This project requires Python 3.6+ and uses built-in standard libraries (`tkinter`, `shutil`, `pathlib`), so **no third-party package installation is required** to run the script.

### Running the Script
1. Clone or download this repository.
2. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Run the script:
   ```bash
   python organizer.py
   ```
4. A file chooser dialog will appear. Select the folder you wish to organize.

---

## 📦 Building an Executable (`.exe`)

You can compile this project into a portable executable that runs on Windows machines without Python.

### Step 1: Install PyInstaller
```bash
pip install pyinstaller
```

### Step 2: Build without Console Window
Run PyInstaller using the `--onefile` and `--noconsole` flags:
```bash
pyinstaller --onefile --noconsole organizer.py
```

### Step 3: Locate the `.exe`
Once the build process completes, locate your standalone executable in the `dist/` directory:
```
dist/
└── organizer.exe
```
Simply copy `organizer.exe` and run it on any target PC!

---

## 🛠️ Rebuilding / Modifying Code

If you make updates to `organizer.py` and want to build a fresh executable, run PyInstaller with the `--clean` flag:

```bash
pyinstaller --onefile --noconsole --clean organizer.py
```

---

## 📄 License
This project is open-source and free to use for personal or commercial projects.