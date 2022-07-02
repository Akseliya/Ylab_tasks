import os
import time
import random


class ReverseTicTacToe:
    _INPUT_CHAR = {'А': 0, 'а': 0, 'Б': 1, 'б': 1, 'В': 2, 'в': 2, 'Г': 3,
                   'г': 3, 'Д': 4, 'д': 4, 'Е': 5, 'е': 5, 'Ж': 6, 'ж': 6,
                   'З': 7, 'з': 7, 'И': 8, 'и': 8, 'К': 9, 'к': 9}
    _PLAYER_MARK = 'x'
    _COMPUTER_MARK = 'o'
    _EMPTY_MARK = '.'
    _width = _height = 10

    def __init__(self):
        self._playing_field = [[self._EMPTY_MARK for x in range(self._width)]
                               for x in range(self._height)]
        self._computer_cells = [(i, j) for i in range(self._height)
                                for j in range(self._width)]
        self._computer_fail_cells = []
        self._width -= 1
        self._height -= 1

    def start(self):
        """Управление процессом игры"""
        try:
            while True:
                self._print_playng_field()
                time.sleep(0.4)
                cell = self._input_cell()
                self._put_mark(cell, self._PLAYER_MARK)
                self._print_playng_field()
                if not self._is_safe_cell(cell, self._PLAYER_MARK):
                    print('\n\nВы проиграли.')
                    break

                time.sleep(0.8)
                cell, is_computer_fail = self._get_computer_selected_cell()
                self._put_mark(cell, self._COMPUTER_MARK)
                self._print_playng_field()
                if is_computer_fail:
                    print('\n\nПоздравляем! Вы победили!')
                    break
        except IndexError:
            print('\n\nНичья!')

    def _print_playng_field(self):
        """Печать игрового поля"""
        os.system('cls')
        print('\nИгра "Обратные крестики-нолики". Проигрывает тот, кто '
              'соберёт 5 в ряд.\n\n')
        print('   А Б В Г Д Е Ж З И К')
        print()
        for i, string in enumerate(self._playing_field):
            print(i, end='  ')
            for cell in string:
                print(cell, end=' ')
            print()

    def _input_cell(self):
        """Ввод ячейки пользователем"""
        print()
        while True:
            cell = input('\nВведите номер ячейки (например, "д5"): ').strip()
            if not (len(cell) == 2 and cell[0] in self._INPUT_CHAR and
                    cell[1].isdigit() and '0' <= cell[1] <= '9'):
                print('Ошибка! Ожидаются русская буква и цифра в диапазоне '
                      'поля, попробуйте ещё раз.')
                continue

            cell = (int(cell[1]), self._INPUT_CHAR[cell[0]])
            if self._playing_field[cell[0]][cell[1]] != self._EMPTY_MARK:
                print('Ошибка! Выбирать можно только пустые ячейки.')
                continue

            if cell in self._computer_fail_cells:
                self._computer_fail_cells.remove(cell)

            return cell

    def _is_safe_cell(self, cell, mark):
        """Проверка, не проиграет ли игрок, если сделает ход в эту ячейку"""
        def get_count(sign_i, sign_j):
            """Подсчёт кол-ва стоящих в ряд элементов в одном из 8 заданных
            направлений (вверх, вправо-вверх, вправо...)"""
            i = cell_i
            j = cell_j
            count = 0
            for x in range(4):
                i += sign_i
                j += sign_j
                if not (0 <= i <= self._height) or not (0 <= j <= self._width):
                    break
                if self._playing_field[i][j] != mark:
                    break
                count += 1

            return count

        def is_count_less_then_5(line):
            """Проверка по 4 направлениям (горизонталь, вертикаль,
            две диагонали), что кол-во элементов меньше 5"""
            count_mark = 1
            count_mark += get_count(*line[0])
            count_mark += get_count(*line[1])

            return count_mark < 5

        cell_i = cell[0]
        cell_j = cell[1]
        lines = (
            ((0, -1), (0, 1)),  # горизонтальная линия
            ((-1, 0), (1, 0)),  # вертикальная линия
            ((-1, -1), (1, 1)),  # главная диагональ
            ((1, -1), (-1, 1))  # обратная диагональ
        )
        for line in lines:
            if not is_count_less_then_5(line):
                return False

        return True

    def _put_mark(self, cell, mark):
        """Проставление отметки в указанную ячейку"""
        self._playing_field[cell[0]][cell[1]] = mark
        if cell in self._computer_cells:
            self._computer_cells.remove(cell)

    def _get_computer_selected_cell(self):
        """Получение выбранной компьютером ячейки"""
        while True:
            if not self._computer_cells:
                cell = random.choice(self._computer_fail_cells)
                return (cell, True)

            cell = random.choice(self._computer_cells)
            self._computer_cells.remove(cell)
            if not self._is_safe_cell(cell, self._COMPUTER_MARK):
                self._computer_fail_cells.append(cell)
                continue

            return (cell, False)


if __name__ == '__main__':
    game = ReverseTicTacToe()
    game.start()
