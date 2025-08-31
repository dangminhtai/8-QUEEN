#ui/menu_ui.py
import tkinter as tk

def create_menu(root, themes, apply_theme, custom_theme):
    """Tạo menu tuỳ chỉnh theme"""
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    theme_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Tùy chỉnh", menu=theme_menu)
    for name, (light, dark) in themes.items():
        theme_menu.add_command(label=name, command=lambda l=light, d=dark: apply_theme(l, d))
    theme_menu.add_command(label="Custom...", command=custom_theme)
