#!/usr/bin/env python3
import json
import os
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

VERSION = [
	2,								# MAJOR
	1,								# MINOR
	1								# PATCH/BUGFIX
]
VERSION_COMMENT = "Added Versioning & Fix Search"

def get_version_str():
	return "%d.%d~%d" % (VERSION[0], VERSION[1], VERSION[2])

class KissLauncher(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title(f"Games [{get_version_str()}]")
        self.set_default_size(250, 400)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.current_selection = None
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        
        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Search...")
        self.search_entry.connect("search-changed", self.on_search_changed)
        vbox.pack_start(self.search_entry, False, False, 0)
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)

        self.listbox.connect("row-selected", self.on_row_selected)
        
        self.load_games()
        
        scrolled.add(self.listbox)
        vbox.pack_start(scrolled, True, True, 0)
        
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        self.status = Gtk.Label(label=f"{len(self.games)} games loaded")
        self.status.set_halign(Gtk.Align.START)
        status_box.pack_start(self.status, True, True, 0)
        
        self.play_button = Gtk.Button.new_with_label("Play")
        self.play_button.set_sensitive(False)
        self.play_button.connect("clicked", self.on_play_clicked)
        status_box.pack_start(self.play_button, False, False, 0)
        
        vbox.pack_start(status_box, False, False, 0)
        
        self.add(vbox)
        self.show_all()
    
    def load_games(self):
        config_path = os.path.expanduser("~/.config/kiss/games.json")
        try:
            with open(config_path, 'r') as f:
                self.games = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.games = {}
        
        self.populate_list(self.games)
    
    def populate_list(self, games):
        for child in self.listbox.get_children():
            self.listbox.remove(child)
        
        for key, game in games.items():
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            
            icon_name_or_path = game.get("icon", "applications-games-symbolic")
            
            if os.path.exists(icon_name_or_path):
                icon = Gtk.Image.new_from_file(icon_name_or_path)
                icon.set_pixel_size(24)
            else:
                icon_theme = Gtk.IconTheme.get_default()
                if not icon_theme.lookup_icon(icon_name_or_path, Gtk.IconSize.MENU, 0):
                    icon_name = "dialog-error"
                icon = Gtk.Image.new_from_icon_name(icon_name_or_path, Gtk.IconSize.MENU)
            hbox.pack_start(icon, False, False, 0)
            
            label = Gtk.Label(label=game.get("name", key))
            label.set_xalign(0)
            hbox.pack_start(label, True, True, 0)
            
            row.add(hbox)
            row.game_key = key
            row.show_all()
            self.listbox.add(row)
            
    
    def on_search_changed(self, entry):
        search_text = entry.get_text().lower()
        if not search_text:
            self.populate_list(self.games)
            self.status.set_text(f"{len(self.games)} games loaded")
            self.listbox.select_row(None)
            self.current_selection = None
            self.play_button.set_sensitive(False)
            return
        
        filtered = {k: v for k, v in self.games.items() 
                    if search_text in k.lower() or search_text in v.get("name", "").lower()}
        self.populate_list(filtered)
        self.status.set_text(f"{len(filtered)} of {len(self.games)} games")
        self.listbox.select_row(None)
        self.current_selection = None
        self.play_button.set_sensitive(False)
    
    def on_row_selected(self, listbox, row):
        if row is None:
            self.current_selection = None
            self.play_button.set_sensitive(False)
            return
        
        self.current_selection = row.game_key
        self.play_button.set_sensitive(True)
    
    def on_play_clicked(self, button):
        if self.current_selection is not None:
            self.launch_game(self.current_selection)
    
    def launch_game(self, game_key):
        game = self.games.get(game_key)
        if game and "cmd" in game:
            subprocess.Popen(game["cmd"], shell=True)
            self.destroy()

if __name__ == "__main__":
    win = KissLauncher()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
