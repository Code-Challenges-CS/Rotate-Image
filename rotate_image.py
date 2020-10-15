
class Solution:

    def rotate(self, matrix: []):
        row = len(matrix)
        col = row

        # Transpose the matrix
        for i in range(row):
            for j in range(i, col):  # [[1, 2], [4, 3]]
                temp = matrix[i][j]  # 1
                matrix[i][j] = matrix[j][i]  # 1 = 4 now [[1, 4], [4, 3]]
                matrix[j][i] = temp  # 3 = 2 now [[1, 4], [2, 3]]
                #Result = [[1, 4], [2, 3]]

        # Swap the values of each row
        for i in range(row):
            for j in range(int(col/2)):  # Devide to swap once
                temp = matrix[i][j]  # 4 -> [[1, 4], [2, 3]]
                matrix[i][j] = matrix[i][col-1-j]  # [[1, 1], [2, 3]]
                matrix[i][col-1-j] = temp  # [[4, 1], [2, 3]]
                #Result = [[4, 1], [3, 2]]

# Process
# [4, 1] -> [1, 4] -> [4, 1]
# [3, 2] -> [2, 3] -> [3, 2]


image = [[1, 2], [4, 3]]


solution = Solution()

solution.rotate(image)
