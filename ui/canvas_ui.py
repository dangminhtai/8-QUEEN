#ui/canvas_ui.py
import tkinter as tk

def create_canvases(root, width=600, height=600):
    """Tạo và trả về 2 canvas"""
    canvas_1 = tk.Canvas(root, width=width, height=height)
    canvas_1.place(x=50, y=50)
    canvas_2 = tk.Canvas(root, width=width, height=height)
    canvas_2.place(x=700, y=50)
    return canvas_1, canvas_2
