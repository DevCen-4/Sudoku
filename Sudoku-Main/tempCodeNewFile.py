from subprocess import check_output
# from tarfile import TruncatedHeaderError
from turtle import Screen
import pygame
import math
import random
import numpy
import copy

import Notification
from Notification import create_game_win_window
from Notification import create_game_over_window

# import pyautogui

# Hàm tạo nút trò chơi mới
# màu
width_number = 180
height_number = 180
before_event_color = (234, 238, 244)
after_event_color = (220, 227, 237)
border_radius_number = 10
textcolor = (60, 121, 215)
textsize = 150

num_error = 3


def SolutionSudoku():
    # Đọc file Test và tạo file để lưu kết quả
    file = open('Result.txt', 'w')
    a = copy.deepcopy(grid)
    aa = copy.deepcopy(grid)

    # Khởi tạo những giá trị cần thiết
    N = 9

    row = [[0 for _ in range(10)] for _ in range(10)]
    column = [[0 for _ in range(10)] for _ in range(10)]
    square = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]

    x = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)]

    # Xóa những số có giá trị 0 ở trong mảng những số có thể điền vào ô trống
    def Delete_Number_0():
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    x[i][j] = [num for num in x[i][j] if num != 0]

    # Kiểm tra xem những giá trị có thể điền có đúng hay không
    def Check_Again():
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    for tmp in range(len(x[i][j])):
                        if (row[i][x[i][j][tmp]] == 1 or column[j][x[i][j][tmp]] == 1 or square[i // 3][j // 3][
                            x[i][j][tmp]] == 1) and x[i][j][tmp] != 0:
                            x[i][j][tmp] = 0

    # Điền vào ô chỉ còn duy nhất một số có thể điền vào
    def The_Last_Free_Cell(i, j):
        if len(x[i][j]) == 1 and row[i][x[i][j][0]] == 0 and column[j][x[i][j][0]] == 0 and square[i // 3][j // 3][
            x[i][j][0]] == 0:
            if x[i][j][0] != aa[i][j]:
                return

            file.write("1 " + str(i) + " " + str(j) + " " + str(x[i][j][0]) + '\n')

            a[i][j] = x[i][j][0]
            row[i][x[i][j][0]] = 1
            column[j][x[i][j][0]] = 1
            square[i // 3][j // 3][x[i][j][0]] = 1

    # Điền vào ô trống giá trị mà ở hàng đó duy nhất ô đang xét có thể điền được
    def The_Last_Remaining_Cell_In_Row(i, j):
        colList = []
        colList.clear()

        for col in range(0, 9):
            if a[i][col] == 0 and col != j:
                colList.extend(x[i][col])

        for num in x[i][j]:
            if num in colList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i // 3][j // 3][
                num] == 1:
                continue
            if len(colList) == 0:
                return
            if aa[i][j] != num:
                return

            file.write("2 " + str(i) + " " + str(j) + " " + str(num) + '\n')

            a[i][j] = num
            row[i][num] = 1
            column[j][num] = 1
            square[i // 3][j // 3][num] = 1
            return

    # Điền vào ô trống giá trị mà ở cột đó duy nhất ô đang xét có thể điền được
    def The_Last_Remaining_Cell_In_Column(i, j):
        rowList = []
        rowList.clear()

        for r in range(0, 9):
            if a[r][j] == 0 and r != i:
                rowList.extend(x[r][j])

        for num in x[i][j]:
            if num in rowList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i // 3][j // 3][
                num] == 1:
                continue
            if len(rowList) == 0:
                return
            if aa[i][j] != num:
                return

            file.write("3 " + str(i) + " " + str(j) + " " + str(num) + '\n')

            a[i][j] = num
            row[i][num] = 1
            column[j][num] = 1
            square[i // 3][j // 3][num] = 1
            return

    # Điền vào ô trống giá trị mà ở ô vuông đó duy nhất ô đang xét có thể điền được
    def The_Last_Remaining_Cell_In_Square(i, j):
        squareList = []
        squareList.clear()

        for r in range(i // 3 * 3, i // 3 * 3 + 3):
            for col in range(j // 3 * 3, j // 3 * 3 + 3):
                if a[r][col] == 0 and r != i and col != j:
                    squareList.extend(x[r][col])

        for num in x[i][j]:
            if num in squareList or num == 0 or row[i][num] == 1 or column[j][num] == 1 or square[i // 3][j // 3][
                num] == 1:
                continue
            if len(squareList) == 0:
                return
            if aa[i][j] != num:
                return

            file.write("4 " + str(i) + " " + str(j) + " " + str(num) + '\n')

            a[i][j] = num
            row[i][num] = 1
            column[j][num] = 1
            square[i // 3][j // 3][num] = 1
            return

            # Giải ma trận Sudoku bằng phương pháp sinh thông thường

    def isSafe(aa, row, col, num):
        for x in range(9):
            if aa[row][x] == num:
                return False

        for x in range(9):
            if aa[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if aa[i + startRow][j + startCol] == num:
                    return False
        return True

    def solveSudoku(aa, row, col):
        if (row == N - 1 and col == N):
            return True

        if col == N:
            row += 1
            col = 0

        if aa[row][col] > 0:
            return solveSudoku(aa, row, col + 1)
        for num in range(1, N + 1, 1):
            if isSafe(aa, row, col, num):
                aa[row][col] = num
                if solveSudoku(aa, row, col + 1):
                    return True

            aa[row][col] = 0
        return False

    # Kiểm tra các cột, hàng, ô vuông cho phù hợp
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] != 0:
                row[i][a[i][j]] = 1
            else:
                row[i][a[i][j]] = 0

    for j in range(0, 9):
        for i in range(0, 9):
            if a[i][j] != 0:
                column[j][a[i][j]] = 1
            else:
                column[j][a[i][j]] = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] != 0:
                square[i // 3][j // 3][a[i][j]] = 1
            else:
                square[i // 3][j // 3][a[i][j]] = 0

    # Xem xét những ô trống có thể điền được những giá trị gì
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == 0:
                for value in range(1, 10):
                    if row[i][value] != 1 and column[j][value] != 1 and square[i // 3][j // 3][value] != 1:
                        x[i][j].append(value)

    # Solution of Sudoku
    if (solveSudoku(aa, 0, 0)):
        pass
    else:
        pass
        # print("no solution  exists ")

    # Giải Sudoku theo từng bước giải
    for count in range(0, 100):
        Check_Again()
        Delete_Number_0()
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    The_Last_Free_Cell(i, j)

        Check_Again()
        Delete_Number_0()
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    The_Last_Remaining_Cell_In_Row(i, j)

        Check_Again()
        Delete_Number_0()
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    The_Last_Remaining_Cell_In_Column(i, j)

        Check_Again()
        Delete_Number_0()
        for i in range(0, 9):
            for j in range(0, 9):
                if a[i][j] == 0:
                    The_Last_Remaining_Cell_In_Square(i, j)

    file.close()


def FindHint(filename='Result.txt'):
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            x = numbers[1]
            y = numbers[2]
            value = numbers[3]
            if grid[x][y] == 0 or grid[x][y] != value:
                insert_into_grid(value, x, y, True)
                return (x, y)


def draw_button(screen, text, x, y, w, h, inactive_color, active_color, radius, text_color, text_size):
    mouse = pygame.mouse.get_pos()

    # Kiểm tra nếu con trỏ chuột đang nằm trong nút
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h), border_radius=radius)  # Màu sáng khi di chuột qua
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h), border_radius=radius)  # Màu bình thường

    # Vẽ chữ lên nút
    font = pygame.font.SysFont(None, text_size)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=((x + w // 2), (y + h // 2)))
    screen.blit(text_surf, text_rect)


# Hàm vẽ nút tròn
def draw_circle(screen, text, x, y, inactive_color, active_color, radius, img):
    mouse = pygame.mouse.get_pos()

    # Tính khoảng cách giữa chuột và tâm hình tròn
    distance = math.sqrt((mouse[0] - x) ** 2 + (mouse[1] - y) ** 2)

    # Kiểm tra nếu khoảng cách nhỏ hơn bán kính
    if distance < radius:
        pygame.draw.circle(screen, active_color, (x, y), radius)  # Màu sáng khi di chuột qua
    else:
        pygame.draw.circle(screen, inactive_color, (x, y), radius)  # Màu bình thường

    # Vẽ icon lên nút
    screen.blit(img, (x - img.get_width() // 2, y - img.get_height() // 2))

    # Vẽ chữ cho nút
    font = pygame.font.SysFont(None, 35)
    text_surf = font.render(text, True, (60, 121, 215))
    text_rect = text_surf.get_rect(center=(x, y + 70))
    screen.blit(text_surf, text_rect)


def draw_exercise():
    return


def draw_number_and_new_game_button(window):
    # Vẽ các số từ 1->9 và Nút  NewGame
    draw_button(window, '1', 1030, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '2', 1230, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '3', 1430, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '4', 1030, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '5', 1230, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '6', 1430, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '7', 1030, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '8', 1230, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '9', 1430, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, 'New Game', 1030, 830, 580, 100, (90, 123, 192), (90, 123, 200), 30, 'white', 100)
    # vẽ nút xóa quay lại
    img_delete = pygame.image.load('Image/delete.png').convert_alpha()
    img_return = pygame.image.load('Image/return.png').convert_alpha()
    img_idea = pygame.image.load('Image/answer.png').convert_alpha()
    draw_circle(window, 'DELETE', 1120, 100, before_event_color, after_event_color, 45, img_delete)
    draw_circle(window, 'HINT', 1320, 100, before_event_color, after_event_color, 45, img_return)
    draw_circle(window, 'ANSWER', 1520, 100, before_event_color, after_event_color, 45, img_idea)


# Điền số
# Sudoku grid matrix (9x9), 0 means empty, 1-9 are the numbers to be printed

# Sinh đề
b = numpy.load('data.npz')['data']

test_code = random.randint(1, 5000)

grid = b[test_code].tolist()


# Hàm xác định cho tuple cố định, để tránh thao tác lên đề
def define_control_grid(grid):
    control_grid = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                control_grid[i][j] = -1
            else:
                control_grid[i][j] = 0
    return control_grid


control_grid = define_control_grid(grid)


# hàm in số lên màn hình
def draw_numbers(screen, selected=None):
    global num_error, count_false_number
    font = pygame.font.SysFont(None, 90)  # Kích thước font là 90
    for i in range(9):
        for j in range(9):
            color = 'white'
            # Nếu có ô được chọn
            if selected:
                selected_row, selected_col = selected
                # Đổi màu các ô cùng dòng, cùng cột
                if i == selected_row or j == selected_col:
                    color = (226, 235, 251)
                # Đổi màu các ô cùng khối 3x3
                if (i // 3 == selected_row // 3) and (j // 3 == selected_col // 3):
                    color = (226, 235, 251)
                # Đổi màu ô được chọn
                if i == selected_row and j == selected_col:
                    color = (187, 222, 251)
            # Vẽ ô vuông
            pygame.draw.rect(screen, color, (j * CELL_SIZE + 30, i * CELL_SIZE + 30, CELL_SIZE, CELL_SIZE))
            number = grid[i][j]
            if number != 0:  # Kiểm tra nếu ô không rỗng
                # Đặt màu tương ứng dựa trên trạng thái của control_grid
                if control_grid[i][j] == -1:
                    text_color = (0, 25, 51)  # Màu xám cho các ô không thể thay đổi
                elif control_grid[i][j] == -2 or control_grid[i][j] == -3:
                    text_color = (0, 76, 153)  # Màu cho các số đã điền
                elif control_grid[i][j] == -4:
                    text_color = (255, 0, 0)  # màu đỏ cho số điền sai
                else:
                    text_color = (0, 0, 0)  # Màu đen cho các ô trống

                if text_color == (255, 0, 0):
                    count_false_number += 1;

                text_surf = font.render(str(number), True, text_color)
                text_rect = text_surf.get_rect(center=(j * 100 + 80, i * 100 + 80))  # Tính vị trí trung tâm
                screen.blit(text_surf, text_rect)  # Vẽ số lên màn hình


GRID_SIZE = 9
CELL_SIZE = 100  # Kích thước của mỗi ô lưới


# Hàm lấy vị trí cell lưới
def get_cell_index(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    # Tính chỉ số hàng và cột dựa vào vị trí chuột
    grid_x = (mouse_x - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel
    grid_y = (mouse_y - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel

    # Kiểm tra xem chỉ số có nằm trong giới hạn không
    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        return (grid_y, grid_x)  # Trả về tuple (hàng, cột)
    return None  # Trả về None nếu không có ô nào được nhấp


def get_clicked_number(mouse):
    click = pygame.mouse.get_pressed()

    # Danh sách chứa thông tin vị trí của các nút số (tọa độ x, y, số hiển thị)
    number_buttons = [
        (1030, 230, '1'), (1230, 230, '2'), (1430, 230, '3'),
        (1030, 430, '4'), (1230, 430, '5'), (1430, 430, '6'),
        (1030, 630, '7'), (1230, 630, '8'), (1430, 630, '9')
    ]

    if click[0] == 1:  # Nếu nhấn chuột trái
        for button in number_buttons:
            x, y, number = button
            if x + width_number > mouse[0] > x and y + height_number > mouse[1] > y:
                return int(number)  # Trả về giá trị của số được nhấn (1 -> 9)

    return None  # Nếu không nhấn vào nút nào, trả về None


# hàm thêm lên ma trận lưới
def insert_into_grid(value, row, col, valid):
    if row is not None and col is not None:
        if control_grid[row][col] == 0 and valid:
            grid[row][col] = value
            control_grid[row][col] = -2
        elif control_grid[row][col] == 0 and not valid:
            grid[row][col] = value
            control_grid[row][col] = -4


#
# def insert_into_grid_false(value, row, col):
#     if row is not None and col is not None:
#         if control_grid[row][col] == 0:
#             grid[row][col] = value
#             control_grid[row][col] = -4

# nhận biết phím chức năng được bấm
def get_clicked_circle(mouse_pos):
    click = pygame.mouse.get_pressed()
    # Danh sách chứa thông tin của các nút (tọa độ x, y, bán kính, tên nút)
    circle_buttons = [
        (1120, 100, 45, 'delete'),  # Tọa độ và bán kính của nút delete
        (1320, 100, 45, 'hint'),  # Tọa độ và bán kính của nút hint
        (1520, 100, 45, 'answer')  # Tọa độ và bán kính của nút idea
    ]

    if click[0] == 1:  # Nếu nhấn chuột trái
        for button in circle_buttons:
            x, y, radius, name = button
            # Tính khoảng cách từ vị trí chuột tới tâm của nút
            distance = math.sqrt((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2)
            if distance < radius:  # Kiểm tra nếu khoảng cách nhỏ hơn bán kính
                # print(f'Bạn đã bấm vào nút {name}')
                return name  # Trả về tên của nút đã bấm

    return None  # Nếu không bấm vào nút nào


# hàm test nút delete
def delete_on(row, col):
    if row is not None and col is not None:
        if control_grid[row][col] == -2 or control_grid[row][col] == -4:
            grid[row][col] = 0
            control_grid[row][col] = 0


# các hàm xử lý nút trò chơi mới
def get_clicked_new_game(mouse_pos):
    click = pygame.mouse.get_pressed()

    # Thông tin về nút "New Game"
    new_game_x = 1030
    new_game_y = 830
    new_game_width = 580
    new_game_height = 100

    if click[0] == 1:  # Nếu nhấn chuột trái
        if new_game_x + new_game_width > mouse_pos[0] > new_game_x and new_game_y + new_game_height > mouse_pos[
            1] > new_game_y:
            print('Bạn đã bấm vào nút New Game')
            return True  # Trả về True nếu nút được nhấn

    return False  # Nếu không nhấn vào nút "New Game", trả về False


def set_new_game():
    global grid, control_grid, num_error  # Đảm bảo bạn có quyền truy cập vào biến toàn cục
    global count_false_number  # khai báo biến đếm lỗi sai global
    count_false_number = 0  # trả lại lại giá trị mặc định cho biến đếm lỗi sai
    # Sinh lại đề mới (sử dụng dữ liệu từ file hoặc tạo mới)
    b = numpy.load('data.npz')['data']
    test_code = random.randint(1, 10000)
    grid = b[test_code].tolist()
    control_grid = define_control_grid(grid)  # Cập nhật control_grid theo đề mới
    num_error = 3


# Hàm giải đề
N = 9


def isSafe(row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


# hàm đã được điền full:
def check_full():
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    # Khi nào full thì không cho xóa nữa
    return True


# Biến lưu số lỗi sai
count_false_number = 0


# Hàm kiểm tra số lần sai để xác định thua
def check_lose():
    global count_false_number
    count_false_number = 0  # Đặt lại số lỗi về 0 trước khi kiểm tra
    for row in range(0, 9):
        for col in range(0, 9):
            if control_grid[row][col] == -4:  # Nếu có ô bị đánh dấu sai
                count_false_number += 1
                # Trả về kết quả dựa trên số lỗi
                return count_false_number >= 3


def solveSudoku(row, col):
    global grid
    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(row, col + 1)
    for num in range(1, N + 1, 1):
        if isSafe(row, col, num):
            grid[row][col] = num
            control_grid[row][col] = -3
            for i in range(0, 9):
                for j in range(0, 9):
                    if check_full():
                        if control_grid[i][j] == -2:
                            control_grid[i][j] = -3
            if solveSudoku(row, col + 1):
                return True

        grid[row][col] = 0
    return False


# hàm kiểm tra xem trong bài có lỗi sai nào không
def has_false_answer():
    for row in range(0, 9):
        for col in range(0, 9):
            if control_grid[row][col] == -4:
                return True
    return False


# Hàm hiển thị lỗi sai lên màn hình:
def draw_fraction(screen):
    # Khai báo các biến cần dùng
    font = pygame.font.SysFont('Arial', 36)  # Font chữ, kích thước chữ
    color = (255, 0, 0)  # Màu chữ (đen)
    global count_false_number  # Biến toàn cục

    # Tạo chuỗi dạng "x/3", trong đó x là count_false_number
    text = f"Số lỗi sai: {count_false_number}/3"

    # Render chuỗi thành đối tượng surface
    rendered_text = font.render(text, True, color)

    # Lấy vị trí để căn chỉnh chuỗi
    text_rect = rendered_text.get_rect()
    text_rect.topright = (1900 - 30, 30)  # Căn góc phải trên, cách mép 10px

    # Vẽ chuỗi lên screen
    screen.blit(rendered_text, text_rect)
