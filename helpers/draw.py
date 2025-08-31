#helpers/draw.py
from tkinter import colorchooser
from config.board import *

def draw_queen(canvas,image=None,draw_q=False):
    """Vẽ bàn cờ và quân hậu (nếu có)"""
    canvas.delete("all")
    for i in range(N):
        for j in range(N):
            x1, y1 = i*TILE, j*TILE
            x2, y2 = x1+TILE, y1+TILE
            color = LIGHT_COLOR if (i+j) % 2 == 0 else DARK_COLOR
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)
            if draw_q and QUEEN_POS[j][i] == '♕':
                canvas.create_image((x1+x2)/2, (y1+y2)/2, image=image)

def apply_theme(canvas_1,canvas_2,light, dark,image=None):
    """Áp dụng theme có sẵn"""
    global LIGHT_COLOR, DARK_COLOR
    LIGHT_COLOR, DARK_COLOR = light, dark
    draw_queen(canvas_1)
    draw_queen(canvas_2,image,draw_q=True)

def custom_theme(canvas_1,canvas_2,image=None):
    """Người dùng chọn màu tùy ý"""
    global LIGHT_COLOR, DARK_COLOR
    c1 = colorchooser.askcolor(title="Chọn màu ô sáng")[1]
    if c1:
        LIGHT_COLOR = c1
    c2 = colorchooser.askcolor(title="Chọn màu ô tối")[1]
    if c2:
        DARK_COLOR = c2
    draw_queen(canvas_1)
    draw_queen(canvas_2,image,draw_q=True)