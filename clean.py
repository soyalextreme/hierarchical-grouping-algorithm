

def clean(vector_array, i_to_delete):

    new_vector = []
    i = 0
    for vector in vector_array:
        if i_to_delete != i:
            new_vector.append(vector)
        i += 1

    return new_vector
