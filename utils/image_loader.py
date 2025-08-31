#utils/image_loader.py
import os
from PIL import Image, ImageTk

def load_queen_image(tile_size):
    current_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(current_path)  
    queen_path = os.path.join(root_path, "assets/queen.png")
    img = Image.open(queen_path)
    img = img.resize((tile_size - 5, tile_size - 5), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)
