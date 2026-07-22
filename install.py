#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent / "games.py"
DESKTOP_DIR = Path.home() / ".local/share/applications"
BIN_DIR = Path.home() / ".local/bin"

DESKTOP_ENTRY = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=Games
Comment=KISS Game Launcher V2
Exec={BIN_DIR}/games
Icon=xfce-games
Terminal=false
Categories=Game;
StartupNotify=true
"""

def main():
	DESKTOP_DIR.mkdir(parents=True,exist_ok=True)
	BIN_DIR.mkdir(parents=True,exist_ok=True)
	shutil.copy(SCRIPT_PATH, BIN_DIR / "games")
	os.chmod(BIN_DIR / "games", 0o755)
	
	desktop_file = DESKTOP_DIR / "games.desktop"
	with open(desktop_file, "w") as f:
		f.write(DESKTOP_ENTRY)
	
	try:
		subprocess.run(["update-desktop-database", str(DESKTOP_DIR)],check=False)
	except FileNotFoundError:
		pass
	
	print("Installed")

if __name__ == "__main__":
	main()
