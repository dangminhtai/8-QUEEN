# ♕
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import colorchooser
from config.board import *
from ui.canvas_ui import create_canvases
from ui.menu_ui import create_menu
# Giao diện
root=tk.Tk()
root.geometry("1400x700+10+10")
root.title("8 quân hậu")
# Lấy đường dẫn ảnh
current_path = os.path.dirname(os.path.abspath(__file__))
queen_path = os.path.join(current_path, "assets/queen.png")
img = Image.open(queen_path)
img = img.resize((TILE-5, TILE-5), Image.Resampling.LANCZOS)
queen_img = ImageTk.PhotoImage(img)
canvas_1, canvas_2 = create_canvases(root)
#Hàm
def draw_queen(x,draw_q=False):
    """Vẽ các ô cờ, màu mặc định"""
    x.delete("all") #Tránh đè Canvas
    for i in range(N):
        for j in range(N):
            x1 = i*TILE
            y1 = j*TILE
            x2 = x1 + TILE
            y2 = y1 + TILE
            if (j+i)%2==0:
                x.create_rectangle(x1,y1,x2,y2,fill=LIGHT_COLOR,width=0)
            else:
                x.create_rectangle(x1,y1,x2,y2,fill=DARK_COLOR,width=0)
            
            if draw_q and QUEEN_POS[j][i] == '♕':
                x.create_image((x1+x2)/2, (y1+y2)/2,
                                    image=queen_img)
                
def apply_theme(light, dark):
    """Áp dụng theme có sẵn"""
    global LIGHT_COLOR, DARK_COLOR
    LIGHT_COLOR, DARK_COLOR = light, dark
    draw_queen(canvas_1)
    draw_queen(canvas_2, draw_q=True)

def custom_theme():
    """Người dùng chọn màu tùy ý"""
    global LIGHT_COLOR, DARK_COLOR
    c1 = colorchooser.askcolor(title="Chọn màu ô sáng")[1]
    if c1:
        LIGHT_COLOR = c1
    c2 = colorchooser.askcolor(title="Chọn màu ô tối")[1]
    if c2:
        DARK_COLOR = c2
    draw_queen(canvas_1)
    draw_queen(canvas_2, draw_q=True)
    
# Menu
create_menu(root, THEMES, apply_theme, custom_theme)
draw_queen(canvas_1)
draw_queen(canvas_2,draw_q=True)
root.mainloop()