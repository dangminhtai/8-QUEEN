import tkinter as tk
from PIL import Image, ImageTk
import os
from helpers.loader import load_algorithm 
import tkinter.messagebox as messagebox
TILE = 75
N = 8

LIGHT_COLOR = "#EBECD0"
DARK_COLOR = "#739552"
THEMES = {
    "Classic (Xanh rêu)": ("#EBECD0", "#739552"),
    "Blue": ("#D0E6F7", "#3B7EBF"),
    "Red": ("#F7D0D0", "#BF3B3B"),
    "Gray": ("#F0F0F0", "#808080")
}


class NQueensApp:
    def __init__(self, root):
        self.root = root
        root.title("8 quân hậu")
        root.geometry("1400x700+10+10")

        # Canvas 2 bàn cờ
        self.canvas_1 = tk.Canvas(root, width=TILE * N, height=TILE * N)
        self.canvas_1.place(x=50, y=50)

        self.canvas_2 = tk.Canvas(root, width=TILE * N, height=TILE * N)
        self.canvas_2.place(x=700, y=50)

        # Load hình quân hậu
        current_path = os.path.dirname(os.path.abspath(__file__))
        queen_path = os.path.join(current_path, "assets/queen.png")
        img = Image.open(queen_path).resize((TILE - 5, TILE - 5), Image.Resampling.LANCZOS)
        self.queen_img = ImageTk.PhotoImage(img)

        # Màu mặc định
        self.light, self.dark = LIGHT_COLOR, DARK_COLOR

        # Nút đổi theme
        self.theme_var = tk.StringVar(value="Classic (Xanh rêu)")
        self.theme_menu = tk.OptionMenu(root, self.theme_var, *THEMES.keys(), command=self.change_theme)
        self.theme_menu.place(x=650, y=10)

        # Vẽ 2 bàn cờ
        self.draw_board(self.canvas_1)
        self.draw_board(self.canvas_2)

        # === Load danh sách thuật toán ===
        algo_dir = "helpers/algorithms"
        algos = [f[:-3] for f in os.listdir(algo_dir) if f.endswith(".py") and f != "__init__.py"]

        # Tạo button cho mỗi thuật toán
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.place(x=50, y=10)

        # Biến lưu nghiệm
        self.solutions = []
        self.current_index = 0
        self.current_algo = None

        for algo_name in algos:
            btn = tk.Button(
                self.buttons_frame,
                text=algo_name.upper(),
                command=lambda name=algo_name: self.run_algorithm(name)
            )
            btn.pack(side="left", padx=5)

    def draw_board(self, canvas):
        canvas.delete("board")
        for i in range(N):
            for j in range(N):
                x1, y1 = j * TILE, i * TILE
                x2, y2 = x1 + TILE, y1 + TILE
                color = self.light if (i + j) % 2 == 0 else self.dark
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0, tags="board")

    def draw_queen(self, canvas, state):
        """state = list vị trí quân hậu theo hàng [col0, col1, ...]"""
        canvas.delete("queen")
        for row, col in enumerate(state):
            if col != -1:
                x1, y1 = col * TILE, row * TILE
                x2, y2 = x1 + TILE, y1 + TILE
                canvas.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self.queen_img, tag="queen")

    def change_theme(self, choice):
        self.light, self.dark = THEMES[choice]
        self.draw_board(self.canvas_1)
        self.draw_board(self.canvas_2)

    def run_algorithm(self, name):
        """Mỗi lần bấm nút thuật toán => in ra nghiệm tiếp theo"""
        if self.current_algo != name:
            # nếu đổi thuật toán thì load lại toàn bộ nghiệm
            algo = load_algorithm(name)
            self.solutions = algo(N)
            self.current_index = 0
            self.current_algo = name

        if not self.solutions:
            messagebox.showinfo("Thông báo", "Không có nghiệm cho thuật toán này")
            return

        if self.current_index < len(self.solutions):
            state = self.solutions[self.current_index]
            self.draw_board(self.canvas_2)
            self.draw_queen(self.canvas_2, state)
            self.current_index += 1
        else:
            messagebox.showinfo("Thông báo", "Đã hết nghiệm cho thuật toán này")


if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensApp(root)
    root.mainloop()
