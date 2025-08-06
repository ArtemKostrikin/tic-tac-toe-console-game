# Создание пустого игрового поля
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Печать поля в консоль
def print_board(board):
    print("   1 2 3")  # Заголовок колонок
    for i, row in enumerate(board):
        print(f"{i + 1}  {'|'.join(row)}")  # Нумерация строк от 1
        if i < 2:
            print("  -----")

# Проверка победы
def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Строка
            return True
        if all(row[i] == player for row in board):    # Столбец
            return True
    # Диагонали
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Проверка на ничью
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Получение корректного хода от игрока
def get_move(player, board):
    while True:
        try:
            coords = input(f"Игрок {player}, введите координаты хода (формат: строка столбец, например: 2 3): ")
            y, x = map(int, coords.strip().split())
            x -= 1  # перевод в индексы от 0
            y -= 1
            if x in range(3) and y in range(3):
                if board[y][x] == " ":
                    return x, y
                else:
                    print("Эта клетка уже занята. Попробуйте снова.")
            else:
                print("Координаты должны быть от 1 до 3.")
        except ValueError:
            print("Неверный формат. Введите два числа через пробел.")

# Основной игровой цикл
def play_game():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        x, y = get_move(current_player, board)
        board[y][x] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Поздравляем! Игрок {current_player} победил!")
            break
        elif check_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

# Запуск игры
if __name__ == "__main__":
    play_game()
