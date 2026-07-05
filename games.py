#!/usr/bin/python3
import os
import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".config/kiss/games.json"

def load_games():
    if not CONFIG_PATH.exists():
        print("KISS: Game config file ~/.config/kiss/games.json missing.")
        quit()
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    return data

def main():
    games = load_games()
    print("KISS Game Launcher")
    print("*"*32)
    for key, value in games.items():
        print(f"- ] <{key}>\t\t\"{value['name']}\"")
    print("*"*32)
    x = input("- ? ")
    if not x in games:
        print(f"KISS: Game '{x}' not found.")
        quit()
    try:
        gameval = games[x]["cmd"]

        os.system(gameval)
    except Exception as e:
        print("ERR: " + e)
        


if __name__ == "__main__":
    main()
