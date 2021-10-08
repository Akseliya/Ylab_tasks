# Задача 1 - поиск кратчайшего пути для почтальона

from itertools import permutations


def get_distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 +
            (point_2[1] - point_1[1]) ** 2) ** 0.5


def get_path(addresses):
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

print(
    f"{min_path['points'][0]} -> "
    f"{min_path['points'][1]}[{min_path['distances'][0]}] -> "
    f"{min_path['points'][2]}[{min_path['distances'][1]}] -> "
    f"{min_path['points'][3]}[{min_path['distances'][2]}] -> "
    f"{min_path['points'][4]}[{min_path['distances'][3]}] -> "
    f"{min_path['points'][5]}[{min_path['distances'][4]}] = "
    f"{min_path['distances'][4]}"
)
