
import tkinter as tk
from config.board import *
from ui.canvas_ui import create_canvases
from ui.menu_ui import create_menu
from helpers.draw import draw_queen,custom_theme,apply_theme
from utils.image_loader import load_queen_image

# Giao diện
root=tk.Tk()
root.geometry("1400x700+10+10")
root.title("8 quân hậu")
queen_img = load_queen_image(TILE)
canvas_1, canvas_2 = create_canvases(root)

def set_theme(light, dark):
    apply_theme(canvas_1, canvas_2, light, dark, image=queen_img)

def set_custom_theme():
    custom_theme(canvas_1, canvas_2, image=queen_img)

create_menu(root, THEMES, set_theme, set_custom_theme)
draw_queen(canvas_1)
draw_queen(canvas_2,queen_img,draw_q=True)
root.mainloop()