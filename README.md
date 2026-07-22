# Games (V2)
A GTK3 GUI launcher for games. (A successor to kissgamelauncher)

## Features:
- GTK3 User Interface
- Icons
- Search bar

## Requirements
- Python 3
- PyGObject

## How to use

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
