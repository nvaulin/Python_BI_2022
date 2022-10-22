import numpy as np

if __name__ == "__main__":
    # First array
    array_one = np.ones(10)

    # Second array

    # Third array - 8x8 chessboard
    chessboard_1 = np.zeros((8, 8), dtype=int)
    chessboard_1[1::2, ::2], chessboard_1[::2, 1::2] = 1, 1

    chessboard_2 = np.ones(35, dtype=int)
    chessboard_2[::2] = 0
    chessboard_2 = np.delete(chessboard_2, [8, 17, 26])
    chessboard_2 = np.stack((chessboard_2, chessboard_2))
    chessboard_2 = chessboard_2.reshape((8, 8))

    chessboard_3 = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))

    print((chessboard_1 == chessboard_2).all() and (chessboard_2 == chessboard_3).all())
    print(chessboard_1)  # Checkig all 3 is equal and printing only one
