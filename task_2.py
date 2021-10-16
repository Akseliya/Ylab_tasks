# Задача 2 - обратные крестики-нолики против компьютера

import os
import time
import random


class ReverseTicTacToe:
    _INPUT_CHAR = {'А': 0, 'а': 0, 'Б': 1, 'б': 1, 'В': 2, 'в': 2, 'Г': 3,
                   'г': 3, 'Д': 4, 'д': 4, 'Е': 5, 'е': 5, 'Ж': 6, 'ж': 6,
                   'З': 7, 'з': 7, 'И': 8, 'и': 8, 'К': 9, 'к': 9}
    _computer_mark = 'o'
    _player_mark = 'x'
    _computer_fail_cells = []
    _width = 10
    _height = 10
    _empty_mark = '.'

    def __init__(self):
        self._playing_field = [[self._empty_mark for x in range(self._width)]
                               for x in range(self._height)]
        self._computer_cells = [(i, j) for i in range(self._height)
                                for j in range(self._width)]
        self._width -= 1
        self._height -= 1

    def start(self):
        """Управление процессом игры"""
        while True:
            self._print_playng_field()
            time.sleep(0.4)
            cell = self._input_cell()
            self._put_mark(cell, self._player_mark)
            self._print_playng_field()
            if self._is_safe_cell(cell, self._player_mark):
                time.sleep(0.8)
                cell, is_fail = self._get_computer_selected_cell()
                self._put_mark(cell, self._computer_mark)
                self._print_playng_field()
                if is_fail:
                    print('\n\nПоздравляем! Вы победили!')
                    break
            else:
                print('\n\nВы проиграли!')
                break

    def _print_playng_field(self):
        """Печать игрового поля"""
        os.system('cls')
        print('\nИгра "Обратные крестики-нолики". Проигрывает тот, кто '
              'соберёт 5 в ряд.\n\n')
        print('   А Б В Г Д Е Ж З И К')
        print()
        i = 0
        for string in self._playing_field:
            print(i, end='  ')
            for cell in string:
                print(cell, end=' ')
            print()
            i += 1

    def _input_cell(self):
        """Ввод ячейки пользователем"""
        print()
        while True:
            cell = input('\nВведите номер ячейки (например, "Д5"): ').strip()
            if (len(cell) == 2 and cell[1].isdigit()
                    and cell[0] in self._INPUT_CHAR
                    and 0 <= int(cell[1]) <= 9):
                cell = (int(cell[1]), self._INPUT_CHAR[cell[0]])
                if self._playing_field[cell[0]][cell[1]] == self._empty_mark:
                    return cell
                else:
                    print('Ошибка! Выбирать можно только пустые ячейки.')
            else:
                print('Ошибка! Ожидаются русская буква и цифра, '
                      'попробуйте ещё раз.')

    def _is_safe_cell(self, cell, mark):
        """Проверка, не проиграет ли игрок, если сделает ход в эту ячейку"""
        def get_count_on_line(sign_i, sign_j):
            """Считает кол-во стоящих в ряд элементов в заданном направлении"""
            i = cell_i
            j = cell_j
            count = 0
            for x in range(4):
                if sign_i == '+':
                    i += 1
                elif sign_i == '-':
                    i -= 1
                if sign_j == '+':
                    j += 1
                elif sign_j == '-':
                    j -= 1

                if not (0 <= i <= self._height) or not (0 <= j <= self._width):
                    break
                if self._playing_field[i][j] != mark:
                    break
                count += 1

            return count

        cell_i = cell[0]
        cell_j = cell[1]

        # пять в ряд по горизонтали
        count_mark = 1
        count_mark += get_count_on_line(0, '-')
        count_mark += get_count_on_line(0, '+')
        if count_mark >= 5:
            return False

        # пять в ряд по вертикали
        count_mark = 1
        count_mark += get_count_on_line('-', 0)
        count_mark += get_count_on_line('+', 0)
        if count_mark >= 5:
            return False

        # пять в ряд по главной диагонали
        count_mark = 1
        count_mark += get_count_on_line('-', '-')
        count_mark += get_count_on_line('+', '+')
        if count_mark >= 5:
            return False

        # пять в ряд по побочной диагонали
        count_mark = 1
        count_mark += get_count_on_line('+', '-')
        count_mark += get_count_on_line('-', '+')
        if count_mark >= 5:
            return False

        return True

    def _put_mark(self, cell, mark):
        """Проставление отметки в указанную ячейку"""
        self._playing_field[cell[0]][cell[1]] = mark
        if cell in self._computer_cells:
            del self._computer_cells[self._computer_cells.index(cell)]

    def _get_computer_selected_cell(self):
        """Получение выбранной компьютером ячейки"""
        while True:
            if self._computer_cells:
                cell = random.choice(self._computer_cells)
                del self._computer_cells[self._computer_cells.index(cell)]
                if self._is_safe_cell(cell, self._computer_mark):
                    return (cell, False)
                else:
                    self._computer_fail_cells.append(cell)
            else:
                cell = random.choice(self._computer_fail_cells)
                return (cell, True)


if __name__ == '__main__':
    game = ReverseTicTacToe()
    game.start()
