import numpy as np


def matrix_multiplication(a, b):
    return np.matmul(a, b)


def multiplication_check(m_list):
    for i in range(len(m_list) - 1):
        A = m_list[i]
        B = m_list[i + 1]
        print(B)
        if A.shape[1] != B.shape[0]:
            return False
    return True


def multiply_matrices(m_list):
    if multiplication_check(m_list):
        return np.linalg.multi_dot(m_list)
    else:
        return None


def compute_2d_distance(A, B):
    return compute_multidimensional_distance(A, B)


def compute_multidimensional_distance(A, B):
    return np.sqrt(np.sum(np.square(A - B)))


if __name__ == "__main__":
    # First array - let's start from basic 10 ones
    ones_1 = np.ones(10, dtype=int)
    ones_2 = np.zeros(10, dtype=int) + 1
    ones_3 = np.array([10] * 10) - 9
    ones_4 = np.array([10] * 10) ** 0
    ones_5 = np.array([[1] * 5] * 2).ravel()
    ones_6 = np.array(np.array([[[[[[[[[[1]]]]]]]]]]).shape)

    # Second array - 8x8 chessboard
    chessboard_1 = np.zeros((8, 8), dtype=int)
    chessboard_1[1::2, ::2], chessboard_1[::2, 1::2] = 1, 1

    chessboard_2 = np.ones(35, dtype=int)
    chessboard_2[::2] = 0
    chessboard_2 = np.delete(chessboard_2, [8, 17, 26])
    chessboard_2 = np.stack((chessboard_2, chessboard_2))
    chessboard_2 = chessboard_2.reshape((8, 8))

    chessboard_3 = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))

    # third array - We need to build a ziggurat!
    ziggurat_1 = np.array([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 2, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]])

    ziggurat_2 = np.zeros(12, dtype=int)
    ziggurat_2[-6:-3:], ziggurat_2[-1::] = 1, 1
    ziggurat_2 = np.concatenate((ziggurat_2, [2], ziggurat_2[::-1])).reshape(5, 5)

    ziggurat_3 = np.ones([5, 5], dtype=int) - np.vander([0] * 5, 5, 5) - np.vander([0] * 5, 5, 0)
    ziggurat_3[[0, -1]] = 0
    ziggurat_3[2][2] = 2

    F = np.fromfunction(np.minimum, (5, 5))
    FR = np.rot90(F, k=2)
    T, TR = np.rot90(np.tri(5)), np.rot90(np.tri(5), k=3)
    ziggurat_4 = np.round(np.multiply(F, T + 1) * np.multiply(FR, TR + 1) / 8 + 0.1, 0).astype(np.int32)
