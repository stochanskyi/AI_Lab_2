import numpy as np


def float_array(from_value, to_value, size):
    return np.random.uniform(from_value, to_value, size)


def int_array(from_value, to_value, size, inclusive=True):
    if inclusive:
        to_value += 1
    return np.random.randint(from_value, to_value, size)


def int_matrix(from_value, to_value, n, m, inclusive=True):
    if inclusive:
        to_value += 1
    return np.random.randint(from_value, to_value, size=(n, m))


def float_matrix(from_value, to_value, n, m):
    return np.random.uniform(from_value, to_value, size=(n, m))
