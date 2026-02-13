from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        i = j = 0
        up = True
        
        while len(result) < m * n:
            result.append(mat[i][j])
            
            if up:
                if j == n - 1:   # hit right boundary
                    i += 1
                    up = False
                elif i == 0:     # hit top boundary
                    j += 1
                    up = False
                else:            # move up-right
                    i -= 1
                    j += 1
            else:
                if i == m - 1:   # hit bottom boundary
                    j += 1
                    up = True
                elif j == 0:     # hit left boundary
                    i += 1
                    up = True
                else:            # move down-left
                    i += 1
                    j -= 1
                    
        return result