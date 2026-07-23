# Games (V2)
A GTK3 GUI launcher for games. (A successor to kissgamelauncher)

<img width="283" height="460" alt="preview" src="https://github.com/user-attachments/assets/a1057efb-1353-4d11-a437-0c21c1b484d4" />


## Features:
- GTK3 User Interface
- Icons
- Search bar

## Requirements
- Python 3
- PyGObject

## How to use

0. `chmod +x` the `.py` files.
1. Create `~/.config/kiss/games.json`
2. Run `./games.py`
3. Click on a game
4. Press play.

## More Permanent Install
Run `install.py` for a more permanent install.

## Example games.json
```json
{
	"doom": {
		"cmd": "gzdoom",
		"name": "DOOM",
		"icon": "gzdoom"
	},
	"luanti": {
		"cmd": "luanti",
		"name": "Luanti (Minetest)",
		"icon": "luanti"
	}
}
```
