# ♕
import tkinter as tk
import os
from PIL import Image, ImageTk
root=tk.Tk()
root.geometry("1400x700+10+10")
root.title("8 quân hậu")
TILE=75
N=8
canvas_1=tk.Canvas(root,width=600,height=600)
canvas_1.place(x=50,y=50)
canvas_2 = tk.Canvas(root, width=600, height=600)
canvas_2.place(x=700, y=50)

queen_pos=[['♕','','','','','','',''],
           ['','','','','♕','','',''],
           ['','','','','','','','♕'],
           ['','','','','','♕','',''],
           ['','','♕','','','','',''],
           ['','','','','','','♕',''],
           ['','♕','','','','','',''],
           ['','','','♕','','','','']
           ]
# Lấy đường dẫn ảnh
current_path = os.path.dirname(os.path.abspath(__file__))
queen_path = os.path.join(current_path, "image.png")
img = Image.open(queen_path)
img = img.resize((TILE-5, TILE-5), Image.Resampling.LANCZOS)
queen_img = ImageTk.PhotoImage(img) 
# def switch_theme():
    
def shuffle_num(x,draw_q=False):
    for i in range(N):
        for j in range(N):
            x1 = i*TILE
            y1 = j*TILE
            x2 = x1 + TILE
            y2 = y1 + TILE
            if (j+i)%2==0:
                x.create_rectangle(x1,y1,x2,y2,fill="#EBECD0",width=0)
            else:
                x.create_rectangle(x1,y1,x2,y2,fill="#739552",width=0)

            if draw_q and queen_pos[j][i] == '♕':
                x.create_image((x1+x2)/2, (y1+y2)/2,
                                    image=queen_img)
shuffle_num(canvas_1)
shuffle_num(canvas_2,draw_q=True)
# btn_sw=tk.Button(root,text="Switch Theme",command=switch_theme)
root.mainloop()