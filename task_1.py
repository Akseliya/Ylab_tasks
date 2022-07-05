# Задача 1 - поиск кратчайшего пути для почтальона

from itertools import permutations


def get_distance(point_1, point_2):
    """Получение расстояния между двумя точками"""
    return ((point_2[0] - point_1[0]) ** 2 +
            (point_2[1] - point_1[1]) ** 2) ** 0.5


def get_path(addresses):
    """Получение пути - словаря с точками пути и суммарным
    расстоянием между ними"""
    post_office = (0, 2)  # координаты почтового отделения
    result = {'points': [post_office], 'distances': []}
    points = (*addresses, post_office)
    prev_point = post_office
    sum_distance = 0
    for point in points:
        result['points'].append(point)
        sum_distance += get_distance(prev_point, point)
        result['distances'].append(sum_distance)
        prev_point = point

    return result


# координаты точек пути - набор перестановок из точек адресатов
path_points = permutations(((2, 5), (5, 2), (6, 6), (8, 3)))

min_path = get_path(next(path_points))
for path_point in path_points:
    current_path = get_path(path_point)

    if current_path['distances'][-1] < min_path['distances'][-1]:
        min_path = current_path

print(f"{min_path['points'][0]} -> ", end='')
for i in range(len(min_path['distances'])):
	print(f"{min_path['points'][i + 1]}[{min_path['distances'][i]}] -> ", end='')
print(f"{min_path['distances'][-1]}")
