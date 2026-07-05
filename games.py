#!/usr/bin/python3
import os
import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".config/kiss/games.json"
COLORAMA_ENABLED = True

if COLORAMA_ENABLED:
    try:
        from colorama import init, Fore, Style
        init(autoreset=True)
    except ImportError:
        COLORA_ENABLED = False

def color(text, color="white"):
    if not COLORAMA_ENABLED:
        return text
    colors = {
            "red": Fore.RED,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE,
            "bold": Style.BRIGHT
            }
    return f"{colors.get(color)}{text}{Style.RESET_ALL}"
            

def load_games():
    if not CONFIG_PATH.exists():
        print(f"{color("KISS:", "magenta")} Game config file ~/.config/kiss/games.json missing.")
        
        quit()
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    return data

def main():
    games = load_games()
    print(color("KISS Game Launcher", "magenta"))
    print(color("*"*32, "blue"))
    for key, value in games.items():
        print(f"- ] <{color(key, 'green')}>\t\t\"{color(value['name'], 'red')}\"")
    print(color("*"*32, "blue"))
    if COLORAMA_ENABLED:
        x = input(f"- ? {Fore.CYAN}{Style.BRIGHT}")
    else:
        x = input("- ? ")
    if not x in games:
        print(color(f"KISS: Game '{x}' not found.", "red"))
        quit()
    try:
        gameval = games[x]["cmd"]

        os.system(gameval)
    except Exception as e:
        print("ERR: " + e)
        


if __name__ == "__main__":
    main()
