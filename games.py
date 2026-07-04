#!/usr/bin/python3
import os
games = {
    "doom": "crispy-doom -iwad /home/korin/Games/DOOM/doom1.wad"
}

def main():
    global games
    print("KISS Game Launcher")
    print("*"*18)
    for key in games.keys():
        print(f"- ] {key}")
        print("*"*18)
        x = input("- ? ")
    try:
        gameval = games.get(x)
        os.system(gameval)
    except Exception as e:
        print("*"*18)
        


if __name__ == "__main__":
    main()
