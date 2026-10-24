import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def organize_directory():
  #hide the main tkinter root window
  root = tk.Tk()
  root.withdraw()

  #open file manager browsing window to choose a directory
  print("Opening file browser...")
  selected_dir = filedialog.askdirectory(title="Select Directory to Organize")

  if not selected_dir:
    print("No directory selected. Operation cancelled.")
    return

  target_path = Path(selected_dir)
  print(f"\nTarget Directory: {target_path}")

  #scan files and create directories based on extensions
  files_moved = 0
  for item in target_path.iterdir():
    #skip if it's a directory (don't organize folders inside folders)
    if item.is_dir():
      continue

    #skip the script if running inside the same folder
    if item.suffix.lower() == ".py":
      continue

    #get file extension
    file_ext = item.suffix.lstrip(".").lower()

    #handle files with no extension
    if not file_ext:
      file_ext = "no_extension"

    #define destination folder path
    dest_dir = target_path / file_ext

    #create directory if doesn't exist
    dest_dir.mkdir(exist_ok=True)

    #move each file to appropriate directory
    dest_path = dest_dir / item.name

    #handle name collisions
    if dest_path.exists():
      base = item.stem
      suffix = item.suffix
      counter = 1
      while dest_path.exists():
        dest_path = dest_dir / f"{base}_{counter}{suffix}"
        counter += 1

    shutil.move(str(item), str(dest_path))
    print(f"Moved: {item.name} -> {file_ext}/")
    files_moved += 1

  print(f"\nSuccess! Organized {files_moved} files.")


if __name__ == "__main__":
  organize_directory()