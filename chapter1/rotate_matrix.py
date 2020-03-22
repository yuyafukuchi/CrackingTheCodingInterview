import unittest

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''

    N = len(matrix)
    layer = N-1

    i = 0
    j = 0
    while layer > 0:
        for k in range(layer):
            tmp_i = i
            tmp_j = j + k

            tmp = matrix[tmp_i][tmp_j]

            matrix[tmp_i][tmp_j] = matrix[N-1-tmp_j][tmp_i]
            matrix[N-1-tmp_j][tmp_i] = matrix[N-1-tmp_i][N-1-tmp_j]
            matrix[N-1-tmp_i][N-1-tmp_j] = matrix[tmp_j][N-1-tmp_i]
            matrix[tmp_j][N-1-tmp_i] = tmp

        i += 1
        j += 1
        layer -= 2

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]),
        ([
            [1, 2, 3, 4],
            [6, 7, 8, 9],
            [11, 12, 13, 14],
            [16, 17, 18, 19]
        ], [
            [16,11,6,1],
            [17, 12, 7, 2],
            [18, 13, 8, 3],
            [19, 14, 9, 4]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()