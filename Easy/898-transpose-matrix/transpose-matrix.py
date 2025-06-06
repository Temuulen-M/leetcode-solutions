class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    """
    # mathmatical procedure
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transposed = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed
    """
