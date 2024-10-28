import pygame
rows, cols = 9, 9
cell_size = 100
def draw_hv(selected=None):
    for row in range(rows):
        for col in range(cols):
            # Xác định màu của ô
            color = 'white'
            width_line = 2
            color_line = (198, 204, 206)

            # Nếu có ô được chọn
            if selected:
                selected_row, selected_col = selected

                # Đổi màu các ô cùng dòng, cùng cột
                if row == selected_row or col == selected_col:
                    color = (226, 235, 251)

                # Đổi màu các ô cùng khối 3x3
                if (row // 3 == selected_row // 3) and (col // 3 == selected_col // 3):
                    color = (226, 235, 251)

                # Đổi màu ô được chọn
                if row == selected_row and col == selected_col:
                    color = (187, 222, 251)
            # Vẽ ô vuông
            pygame.draw.rect(screen, color, (col * cell_size + 30, row * cell_size + 30, cell_size, cell_size))
            # kẻ line ngang
            pygame.draw.line(window, color_line, (col * cell_size + 28, row * cell_size + 30),
                             (col * cell_size + 28 + cell_size, row * cell_size + 30), width_line)
            # kẻ line dọc
            pygame.draw.line(window, color_line, (col * cell_size + 28, row * cell_size + 28),
                             (col * cell_size + 28, row * cell_size + 28 + cell_size), width_line)
    for i in range(0, 10):
        # vẽ đậm những đường 0 | 3 | 6 | 9
        if i % 3 == 0:
            pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
            pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)
        else:
            continue


# lấy tọa độ cell
def get_cell(pos):
    x, y = pos
    row = (y - 30) // cell_size
    col = (x - 30) // cell_size
    return row, col
