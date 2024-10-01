import random
import string



# Bảng Sudoku mẫu với một vài ô trống (được đánh dấu bằng số 0)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Hàm in bảng Sudoku ra màn hình
def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

# Hàm kiểm tra xem số đặt vào ô có hợp lệ không
def is_valid(board, num, pos):
    # Kiểm tra hàng ngang
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Kiểm tra cột dọc
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Kiểm tra ô vuông 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# Hàm tìm ô trống trên bảng
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # hàng, cột

    return None

# Hàm giải Sudoku bằng phương pháp backtracking
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Hàm cho người chơi nhập vào số
def play_sudoku(board):
    print("Bắt đầu chơi Sudoku!")
    while True:
        print_board(board)
        row = int(input("Nhập số hàng (0-8): "))
        col = int(input("Nhập số cột (0-8): "))
        num = int(input("Nhập số cần điền (1-9): "))

        if board[row][col] == 0:
            if is_valid(board, num, (row, col)):
                board[row][col] = num
            else:
                print("Số không hợp lệ. Hãy thử lại.")
        else:
            print("Ô này đã có số. Hãy chọn ô khác.")

        # Kiểm tra xem bảng đã được điền đầy đủ chưa
        if find_empty(board) is None:
            print("Bạn đã hoàn thành trò chơi Sudoku!")
            break

# Chạy trò chơi
play_sudoku(board)