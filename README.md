# Giao diện 8 quân hậu đơn giản

## 1. Cấu trúc dự án
```text
├── assets
│   ├── queen.png
│   ├── rook.png
├── helpers
│   ├── algorithms
│   │   ├── AC3.py
│   │   ├── ao_search.py
│   │   ├── astar.py
│   │   ├── backtracking.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── dls.py
│   │   ├── foward_checking.py
│   │   ├── ga.py
│   │   ├── hill_climbing.py
│   │   ├── ids.py
│   │   ├── local_beam.py
│   │   ├── sa.py
│   │   ├── sensorless.py
│   │   ├── ucs.py
│   ├── loader.py
├── .gitignore
├── app.py
├── read.md
├── README.md
```
## 2. Yêu cầu hệ thống

* **Python** 3.8+ (khuyến nghị 3.10 trở lên)
* **Pip** để cài thư viện
* Các thư viện **Tkinter** và **Pillow** hỗ trợ


## 3. Cài đặt và chạy

```bash
git clone https://github.com/dangminhtai/8-QUEEN
cd 8-QUEEN
pip install pillow tkinter
```
Chạy ứng dụng:

* **Terminal / PowerShell (Windows):**

  ```powershell
  python .\main.py
  ```
* **Terminal (macOS/Linux):**

  ```bash
  python3 main.py
  ```
* **VS Code:** mở thư mục dự án → mở `main.py` → Run (hoặc dùng Code Runner `Ctrl+Alt+N`).

> **Lưu ý:** Chạy từ **thư mục gốc** của dự án để đường dẫn `assets/queen.png` hoạt động chính xác.

## 4. Tính năng chính

* Hai **Canvas** bên trái/phải để hiển thị bàn cờ và trạng thái quân hậu.
* Theme tùy chỉnh có 4 màu (Xanh rêu,Blue,Red,Gray)
* Ảnh quân hậu được lấy từ `assets/queen.png` và **resize** tương ứng với kích thước ô (`TILE`).
* Nhấn nút **[Tên thuật toán]** để chạy thuật toán và hiển thị kết quả, trong đó tên thuật toán là tên file trong thư mục `helpers/algorithms`.
* Nhấn thêm nút **[Tên thuật toán]** 1 lần nữa để hiển thị kết quả tiếp theo.
## 5. Các tệp quan trọng

* Thư mục `assets` chứa hình ảnh con hậu `queen.png`
* app.py chứa giao diện và cấu hình ban đầu
* Thư mục `helpers/algorithms` chứa các thuật toán
* Thư mục `helpers/loader.py` chứa hàm load thuật toán


---

## Liên hệ

Nếu có thắc mắc gì về code, bạn có thể liên hệ mình qua

<p align="center">
  <a href="mailto:dmt826321@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white&style=for-the-badge"/></a>
  <a href="https://facebook.com/tamidanopro"><img src="https://img.shields.io/badge/Facebook-1877F2?logo=facebook&logoColor=white&style=for-the-badge"/></a>
  <a href="https://github.com/dangminhtai"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=for-the-badge"/></a>
</p>

> Thả 1 star ⭐ nếu cảm thấy code của mình hữu ích, cảm ơn rất nhiều!
