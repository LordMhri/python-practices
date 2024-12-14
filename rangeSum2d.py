class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.pre = [[0] * col for _ in range(row)]
        #compute the prefix sum here
        for i in range(row):
            for j in range(col):
                self.pre[i][j] = (self.pre[i][j-1] if j > 0 else 0) + (self.pre[i-1][j] if i > 0 else 0) + matrix[i][j] - (self.pre[i-1][j-1] if (i>0 and j>0) else 0)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
         return (
        self.pre[row2][col2]
        - (self.pre[row1-1][col2] if row1 > 0 else 0)
        - (self.pre[row2][col1-1] if col1 > 0 else 0)
        + (self.pre[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0))