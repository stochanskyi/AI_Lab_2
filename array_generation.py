import numpy as np


def float_array(from_value, to_value, size):
    return np.random.uniform(from_value, to_value, size)


def int_array(from_value, to_value, size):
    return np.random.randint(from_value, to_value, size)
