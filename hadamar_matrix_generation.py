import numpy as np


def hadamar_matrix(n):
    """
    Функция генерации матрицы Адамара размерности n.
    Возвращает матрицу типа np.array.
    """
    # Создание матрицы с единицами в левом верхнем углу
    hadamard = np.array([1])

    # Увеличение матрицы до нужной размерности n
    while hadamard.shape[0] < n:
        # Расширение матрицы из левого верхнего угла
        hadamard = np.vstack([np.hstack([hadamard, hadamard]), np.hstack([hadamard, -hadamard])])

    return hadamard
