from typing import List


def snail(array: List[List]) -> List:
    output_array = []
    x, y = 0, 0
    dif_x, dif_y = 1, 0
    string_len = len(array[0])
    element_count = len(array) * len(array[0])
    while len(output_array) < element_count:
        output_array.append(array[y][x])
        array[y][x] = None
        dif = x + dif_x if dif_x else y + dif_y
        if dif < 0 or dif == string_len or array[y + dif_y][x + dif_x] is None:
            dif_x, dif_y = -dif_y, dif_x
        x += dif_x
        y += dif_y
    return output_array
