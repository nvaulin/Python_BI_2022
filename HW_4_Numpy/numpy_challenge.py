import numpy as np


def matrix_multiplication(a, b):
    '''
    Takes 2 matrices, multiplies them according to the
    rules of the matrix product, gives the resulting matrix

    :param a: 2D np.array with (x,y) shape
    :param b: 2D np.array with (y,z) shape
    :return: 2D np.array with (x,z) shape
    '''
    return np.matmul(a, b)


def multiplication_check(m_list):
    '''
    Takes a list of matrices, and returns True if they can be multiplied
    in the order they appear in the list, and False if they can't be multiplied
    :param m_list: list of np.arrays
    :return: bool
    '''
    for i in range(len(m_list) - 1):
        a = m_list[i]
        b = m_list[i + 1]
        if a.shape[1] != b.shape[0]:
            return False
    return True


def multiply_matrices(m_list):
    '''
    Takes a list of matrices, and returns the result
    of their consecutive multiplication if it can be obtained
    (according to the rules of the matrix product),
    or returns None if they cannot be multiplied.

    :param m_list: list of 2D np.arrays
    :return: 2D np.array or None
    '''
    if multiplication_check(m_list):
        return np.linalg.multi_dot(m_list)
    else:
        return None


def compute_2d_distance(a, b):
    '''
    Takes 2 one-dimensional arrays with a pair of elements
    (as the coordinates of a point on the plane)
    and calculates the Euclidean distance between them.

    Returns a single value - the distance.

    This function to calculate the distance
    makes a call to a more general function
    'compute_multidimensional_distance(a, b)'.

    :param a: 1D np.array with 2 elements
    :param b: 1D np.array with 2 elements
    :return: float
    '''
    return compute_multidimensional_distance(a, b)


def compute_multidimensional_distance(a, b):
    '''
        Takes 2 one-dimensional arrays with any (equal) number of elements
    (as the coordinates in multidimensional space)
    and calculates the Euclidean distance between them.

    Returns a single value - the distance.

    For any integer number n:

    :param a: 1D np.array with n elements
    :param b: 1D np.array with n elements
    :return: float
    '''
    return np.sqrt(np.sum(np.square(a - b)))


def compute_pair_distances(a):
    '''
    Takes a 2D array as a set of rows and calculates
    the matrix of pairwise distances (in terms of Euclidean distance)
    between rows and returns it.

    :param a: 2D np.array
    :return: 2D np.array
    '''
    a_rsh = a.reshape(a.shape[0], 1, a.shape[1])
    res_matr = np.sqrt(np.einsum('ijk, ijk->ij', a - a_rsh, a - a_rsh))
    return res_matr


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

    ziggurat_3 = np.ones([5, 5], dtype=int) - np.vander([0] * 5, 5, True) - np.vander([0] * 5, 5, False)
    ziggurat_3[[0, -1]] = 0
    ziggurat_3[2][2] = 2

    F = np.fromfunction(np.minimum, (5, 5))
    FR = np.rot90(F, k=2)
    T, TR = np.rot90(np.tri(5)), np.rot90(np.tri(5), k=3)
    ziggurat_4 = np.round(np.multiply(F, T + 1) * np.multiply(FR, TR + 1) / 8 + 0.1, 0).astype(np.int32)
