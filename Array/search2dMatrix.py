# LeetCode 74. Search a 2D Matrix

from typing import List

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

printMatrix(matrix)

class Search2dMatrix:
    def searchTarget(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

answer = Search2dMatrix()
print("answer is :", answer.searchTarget(matrix,target=3))