import math


def euclidian_distance(pos_x_1, pos_y_1, pos_x_2, pos_y_2):
    return math.sqrt((pos_x_1 - pos_x_2)**2 + (pos_y_1 - pos_y_2)**2)


def manhathan_distance(pos_x_1, pos_y_1, pos_x_2, pos_y_2):
    return abs(pos_x_1 - pos_x_2) + abs(pos_y_1 - pos_y_2)
