#leetcode:Spiral Matrix 
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return matrix
        
        rowBegin = 0
        rowEnd = len(matrix) - 1
        columnBegin = 0
        columnEnd = len(matrix[0]) - 1
        array = []
        
        while rowBegin <=rowEnd and columnBegin <= columnEnd:
            
            for currentColumn in range(columnBegin,columnEnd+1):
                array.append(matrix[rowBegin][currentColumn])
            rowBegin = rowBegin + 1
            
            for currentRow in range(rowBegin,rowEnd+1):
                array.append(matrix[currentRow][columnEnd])
            columnEnd = columnEnd - 1
            
            if rowBegin <= rowEnd:
                for currentColumn in range(columnEnd,columnBegin-1,-1):
                    array.append(matrix[rowEnd][currentColumn])
                rowEnd = rowEnd - 1
            
            if columnBegin <=columnEnd:
                for currentRow in range(rowEnd,rowBegin-1,-1):
                    array.append(matrix[currentRow][columnBegin])
                columnBegin = columnBegin + 1
            
        return array

#leetcode:Permutations
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        solutions = []
        if num is None:
            return []
        if len(num) == 1:
            return [num]
        for i in range(len(num)):
            for j in self.permute(num[:i]+num[i+1:]):
                solutions.append([num[i]]+j)
        return solutions
                
        