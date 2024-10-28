import pygame
from new import draw_number_and_new_game_button, control_grid  # Kiểm tra xem biến control_grid có tồn tại không
from new import draw_numbers
from new import get_cell_index
from new import get_clicked_number
from new import insert_into_grid



# Tạo pygame
pygame.init()

# Tạo cửa sổ trò chơi
width = 1800
hight = 1000
color = (255, 255, 255)
window = pygame.display.set_mode((width, hight))
window.fill(color)

# Vẽ lưới
for i in range(0, 10):
    pygame.draw.line(window, (198, 204, 206), (30, (i * 100) + 30), (930, (i * 100 + 30)), 2)
    pygame.draw.line(window, (198, 204, 206), (100 * i + 30, 30), ((i * 100 + 30), 930), 2)
for i in range(0, 10):
    # Vẽ đậm những đường 0 | 3 | 6 | 9
    if i % 3 == 0:
        pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
        pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)

# Biến chạy game và biến trạng thái ô đã chọn
running = True
selected_cell_insert = None  # Di chuyển biến này ra ngoài để lưu trạng thái
selected_cell_delete = None

# Vòng lặp chính
def desktop():
    global running  # Khai báo biến toàn cục để sử dụng trong hàm

    while running:
        # Vẽ
        draw_number_and_new_game_button(window)

        # Sự kiện điền đề lên lưới
        draw_numbers(window)

        for event in pygame.event.get():
            # Sự kiện thoát game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Sự kiện thêm vào lưới
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Phần 1: lấy vị trí của cell lưới:
                cell_id = get_cell_index(event.pos)  # Lấy chỉ số hàng và cột
                if cell_id:  # Kiểm tra nếu cell_index hợp lệ
                    row, col = cell_id
                print(f"chọn ô ({row}:{col})")
                # Phần 2: chọn ô phụ để thêm vào grid
                value = get_clicked_number(event.pos)
                if value:  # Kiểm tra nếu value không phải là None
                    print(f"Chọn số: {value}")
                    insert_into_grid(value, row, col)  # Điền giá trị vào ô


        # Cập nhật hiển thị
        pygame.display.update()


def main():
    # Vẽ trạng thái ban đầu của lưới
    for i in range(9):
        for j in range(9):
            print(control_grid[i][j], end=" ")  # Sử dụng end để không xuống dòng
        print()  # Xuống dòng sau khi in một hàng

    desktop()


if __name__ == "__main__":
    main()