from hadamar_matrix_generation import hadamar_matrix
import numpy as np


# функция, выполняющая прямое преобразование Уолша-Адамара
def WHT(matrix):
    hadamar = hadamar_matrix(4)
    return 0.25 * np.matmul(hadamar, matrix)


# функция, выполняющая обратное пеобразование Уолша-Адамара
def inverse_WHT(matrix):
    hadamar = hadamar_matrix(4)
    return np.matmul(hadamar, matrix)

