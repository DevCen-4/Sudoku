import pygame
from new import draw_number_and_new_game_button, control_grid
from new import draw_numbers
from new import get_cell_index
from new import get_clicked_number
from new import insert_into_grid
from new import get_clicked_circle  # Hàm này để xóa giá trị từ lưới
from new import get_clicked_new_game
from new import delete_on
from new import set_new_game

# Tạo pygame
pygame.init()

# Tạo cửa sổ trò chơi
width = 1800
height = 1000
color = (255, 255, 255)
window = pygame.display.set_mode((width, height))
window.fill(color)

# Vẽ lưới
def draw_grid():
    for i in range(0, 10):
        pygame.draw.line(window, (198, 204, 206), (30, (i * 100) + 30), (930, (i * 100 + 30)), 2)
        pygame.draw.line(window, (198, 204, 206), (100 * i + 30, 30), ((i * 100 + 30), 930), 2)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
            pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)

# Biến chạy game
running = True

# Vòng lặp chính
def desktop():
    global running
    row, col = None, None  # Khởi tạo row và col

    while running:
        # Vẽ
        window.fill((255, 255, 255))  # Làm mới màn hình
        draw_grid()  # Vẽ lại lưới
        draw_number_and_new_game_button(window)
        draw_numbers(window)

        for event in pygame.event.get():
            # Sự kiện thoát game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Sự kiện chuột
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Phần 1: lấy vị trí của cell lưới
                cell_id = get_cell_index(event.pos)  # Lấy chỉ số hàng và cột
                if cell_id:  # Kiểm tra nếu cell_index hợp lệ
                    row, col = cell_id
                    print(f"Đã chọn ô ({row}, {col})")

                # Phần 2: chọn số để thêm vào grid
                value = get_clicked_number(event.pos)
                if value:  # Kiểm tra nếu value không phải là None
                    print(f"Chọn số: {value}")
                    insert_into_grid(value, row, col)  # Điền giá trị vào ô

                # Phần 3: kiểm tra click vào các nút delete, return, idea
                mouse_pos = pygame.mouse.get_pos()  # Lấy tọa độ của chuột
                button_clicked = get_clicked_circle(mouse_pos)  # Kiểm tra nút nào đã được click
                if button_clicked:
                    print(f"Đã bấm nút: {button_clicked}")
                    if button_clicked == "delete":
                        delete_on(row, col)  # Gọi hàm để xóa giá trị
                        print(f"Đã xóa giá trị tại ô ({row}, {col})")

                new_game_clicked = get_clicked_new_game(event.pos)
                if new_game_clicked:
                    print("clicked new game button")
                    # Thực hiện hành động khi nhấn nút New Game
                    set_new_game()

        # Cập nhật hiển thị
        pygame.display.update()

def main():
    # In trạng thái ban đầu của lưới
    for i in range(9):
        for j in range(9):
            print(control_grid[i][j], end=" ")
        print()  # Xuống dòng sau khi in một hàng

    desktop()

if __name__ == "__main__":
    main()
