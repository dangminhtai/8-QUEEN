# ♕
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import colorchooser
from config.board import *

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


canvas_1=tk.Canvas(root,width=600,height=600)
canvas_1.place(x=50,y=50)
canvas_2 = tk.Canvas(root, width=600, height=600)
canvas_2.place(x=700, y=50)
#Hàm
def shuffle_num(x,draw_q=False):
    """Vẽ các ô cờ, màu mặc định"""
    x.delete("all") #Tránh đè Canvas
    for i in range(N):
        for j in range(N):
            x1 = i*TILE
            y1 = j*TILE
            x2 = x1 + TILE
            y2 = y1 + TILE
            if (j+i)%2==0:
                x.create_rectangle(x1,y1,x2,y2,fill=light_color,width=0)
            else:
                x.create_rectangle(x1,y1,x2,y2,fill=dark_color,width=0)
            
            if draw_q and queen_pos[j][i] == '♕':
                x.create_image((x1+x2)/2, (y1+y2)/2,
                                    image=queen_img)
                
def apply_theme(light, dark):
    """Áp dụng theme có sẵn"""
    global light_color, dark_color
    light_color, dark_color = light, dark
    shuffle_num(canvas_1)
    shuffle_num(canvas_2, draw_q=True)

def custom_theme():
    """Người dùng chọn màu tùy ý"""
    global light_color, dark_color
    c1 = colorchooser.askcolor(title="Chọn màu ô sáng")[1]
    if c1:
        light_color = c1
    c2 = colorchooser.askcolor(title="Chọn màu ô tối")[1]
    if c2:
        dark_color = c2
    shuffle_num(canvas_1)
    shuffle_num(canvas_2, draw_q=True)

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tùy chỉnh", menu=theme_menu)
for name, (light, dark) in themes.items():
    theme_menu.add_command(label=name, command=lambda l=light, d=dark: apply_theme(l, d))
theme_menu.add_command(label="Custom...", command=custom_theme)
shuffle_num(canvas_1)
shuffle_num(canvas_2,draw_q=True)
root.mainloop()