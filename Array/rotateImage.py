# LeetCode 48. Rotate Image

from typing import List

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)

printMatrix(matrix)

class RotateMatrix:
    def rotate(self, matrix: List[List[int]]) -> None:
        self._length = len(matrix)
        
        for y in range(0,int(self._length/2)):
            for x in range(0,int((self._length+1)/2)):
                newX1,newY1 = self._newCoord(x,y)
                newX2,newY2 = self._newCoord(newX1,newY1)
                newX3,newY3 = self._newCoord(newX2,newY2)

                tmpPixel = matrix[y][x]
                matrix[y][x] = matrix[newY3][newX3]
                matrix[newY3][newX3] = matrix[newY2][newX2]
                matrix[newY2][newX2] = matrix[newY1][newX1]
                matrix[newY1][newX1] = tmpPixel        
                    
    
    def _newCoord(self,oldX,oldY):
        newX = -oldY + self._length -1
        newY = oldX
        return newX,newY
    
rotateMatrix = RotateMatrix()

rotateMatrix.rotate(matrix)
printMatrix(matrix)