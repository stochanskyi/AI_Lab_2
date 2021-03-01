from array_generation import *

def generate_sorted_float_array(left_bound, right_bound, size):
    array = float_array(0., 1., size)
    return sort_array(array)


def generate_sorted_int_array(left_bound, right_bound, size):
    array = int_array(left_bound, right_bound, size)
    return sort_array(array)


def sort_array(arr):
    new_array = np.copy(arr)

    iterator = np.nditer(new_array, flags=['f_index'])
    new_array[0] = iterator.value
    iterator.next()

    for x in iterator:
        key = x

        for i in range(iterator.index, 0, -1):
            if new_array[i] < new_array[i - 1]:
                new_array[i], new_array[i - 1] = new_array[i - 1], new_array[i]
            else:
                break

    return new_array
