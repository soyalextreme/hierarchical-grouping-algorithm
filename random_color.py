import random


def gen_random_color():
    return f"rgb({random.randint(1,255)}, {random.randint(1,255)}, {random.randint(1,255)})"
