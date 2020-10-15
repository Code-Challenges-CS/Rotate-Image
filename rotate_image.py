
class Solution:

    def rotate(self, matrix: []):
        row = len(matrix)
        col = row

        # Transpose the matrix
        for i in range(row):
            for j in range(i, col):  # [[1, 2], [4, 3]]
                temp = matrix[i][j]  # 1
                matrix[i][j] = matrix[j][i]  # 1 = 4 now [[4, 2], [4, 3]]
                matrix[j][i] = temp  # 3 = 2 now [[4, 2], [1, 4]]
                #Result = [[3, 2], [1, 4]]
        # Swap the values of each row
        for i in range(row):
            for j in range(int(col/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][col-1-j]
                matrix[i][col-1-j] = temp
            


#[4, 1]
#[3, 2]
image = [[1, 2], [4, 3]]


solution = Solution()

c = solution.rotate(image)

print(image)
