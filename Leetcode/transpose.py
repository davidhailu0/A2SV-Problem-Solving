from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for col in range(len(matrix[i])):
                result[col][i] = matrix[i][col]
        return result