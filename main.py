from circle import CircleVector
from bokeh.plotting import figure, show
from random_color import gen_random_color


def gen_vector_circles(number_circles):
    circles_vector = []

    for i in range(number_circles):
        circle = CircleVector(i)
        circles_vector.append(circle)
    return circles_vector


def graph(vectors):

    x = []
    y = []
    colors = []
    for vector in vectors:
        position_x, position_y, size, color = vector.get_state()
        x.append(position_x)
        y.append(position_y)
        colors.append(color)
        # sizes.append(size)

    p = figure(plot_width=800, plot_height=800)
    p.annulus(x=x, y=y, inner_radius=size,
              color=colors, alpha=0.5)
    show(p)


def implement(vectors):
    clusters = []
    distances = []
    for vector in vectors:
        distances.append(vector.calculate_distance(vectors, memo={}))

    min_distances = []
    index_min_object = 0
    for distance in distances:
        min_distances.append(min(distance))

    min_distance = min(min_distances)
    for i in min_distances:
        if i == min_distance:
            break
        else:
            index_min_object += 1

    new_vector, cluster = vectors[index_min_object].join_vectors(
        distances[index_min_object], vectors)
    clusters.append(cluster)

    print(clusters)

    # print(index_min_object)
    # print(min_distances)
    # print(min_distance)
    # print(new_vector)
    # print(distances)

    graph(new_vector)
    return new_vector


def run():
    number_circles = int(input("How many vectors do you wanna create:  "))
    circle_vectors = gen_vector_circles(number_circles)
    size = 0.04
    graph(circle_vectors)

    while number_circles > 1:
        new_vector = implement(circle_vectors)
        circle_vectors = new_vector
        number_circles -= 1


if __name__ == "__main__":
    run()
