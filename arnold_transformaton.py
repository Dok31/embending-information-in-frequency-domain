import numpy as np


def arnold_transform(x, y, matr, n):
    xy = np.array([x, y])
    a = np.array(matr)
    xy_transformed = np.matmul(xy, a) % n
    return xy_transformed[0], xy_transformed[1]


def invers_arnold_transform(x_transformed, y_transformed, matr, n):
    inversed_matr = np.linalg.matrix_power(matr, -1)
    xy_transformed = np.array([x_transformed, y_transformed])
    xy = np.matmul(xy_transformed, inversed_matr) % n
    return xy[0], xy[1]


