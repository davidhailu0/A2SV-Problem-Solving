from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        print(result)
        print(matrix)
        for i in range(len(matrix)):
            for col in range(len(matrix[i])):
                result[col][i] = matrix[i][col]
        print(result)
        return result

sol = Solution()
sol.transpose([[1,2,3],[4,5,6],[7,8,9]])