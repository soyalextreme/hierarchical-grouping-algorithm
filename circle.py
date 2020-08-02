
import random
from random_color import gen_random_color
from calculate_distances import euclidian_distance, manhathan_distance
from clean import clean


class CircleVector():

    def __init__(self, number_of_circle):
        self._position_x = random.random() * random.choice([1, -1])
        self._position_y = random.random() * random.choice([1, -1])
        self._name = f"Circle_{number_of_circle}"
        self._size = random.random() / 10
        self._color = gen_random_color()
        self._clusters = []

    def get_state(self):
        return (self._position_x, self._position_y, self._size, self._color)

    def calculate_distance(self, vector_array, memo):
        if(len(vector_array) == 0):
            print("Ya no hay mas elementos")
            return

          # print(vector_array)

          # print("calculating distances....")
        distances = []

        for vector in vector_array:
            if vector._name != self._name:
                # distance = euclidian_distance(
                # vector._position_x, vector._postion_y, self._position_x, self._postion_y)
                distance2 = euclidian_distance(
                    vector._position_x, vector._position_y, self._position_x, self._position_y)
                distances.append(distance2)
        return distances

        # print(distances)

        # i = 0
        # for distance in distances:

        #     lower_distance = distances[0]
        #     if lower_distance > distance:
        #         i += 1
        #         lower_distance = distance

        # name_cluster_1 = vector_array[i]._name

        # self._position_x = vector_array[i]._position_x
        # self._position_y = vector_array[i]._position_y
        # self._name = f"Cluster de {self._name} con {vector_array[i]._name}"
        # self._color = vector_array[i]._color

        # vector_array = clean(vector_array, i)
        # return vector_array, [self._name, name_cluster_1]

    def join_vectors(self, distances, vector_array):
        i = 0
        for distance in distances:
            lower_distance = distances[0]
            if lower_distance > distance:
                i += 1
                lower_distance = distance

        cluster = (self._name, vector_array[i]._name)

        self._position_x = vector_array[i]._position_x
        self._position_y = vector_array[i]._position_y
        self._name = f"{self._name} + {vector_array[i]._name}"
        self._color = vector_array[i]._color

        vector_array = clean(vector_array, i)
        return vector_array, cluster
