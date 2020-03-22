import unittest
# O(1)の空間計算量で！

def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullify_colomn(matrix,column):
    for i in range(len(matrix)):
        matrix[i][column] = 0

def zero_matrix(matrix):
    H = len(matrix)
    W = len(matrix[0])

    first_row_has_zero = False
    first_col_has_zero = False
    for i in range(H):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    for j in range(W):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break

    for i in range(1,H):
        for j in range(1,W):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for j in range(W):
        if matrix[0][j] == 0:
            nullify_colomn(matrix,j)
    
    for i in range(H):
        if matrix[i][0] == 0:
            nullify_row(matrix,i)
    
    if first_row_has_zero:
        nullify_row(matrix,0)
    if first_col_has_zero:
        nullify_colomn(matrix,0)

    
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()