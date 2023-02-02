class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        output = [[0]*A]
        for i in range(A-1): 
            output.append([0]*A)        
        row_start, row_end = 0, A
        column_start, column_end = 0, A
        count = 1
        while row_start < row_end: 
            
            #Move left to right
            for j in range (column_start, column_end): 
                count += 1
                output[row_start][j] = count
            row_start += 1
            
            #Move top to bottom
            for i in range(row_start, row_end): 
                count += 1
                output[i][column_end-1] = count
            column_end -= 1
            
            #Move right to left
            for j in range (column_end, column_start, -1): 
                count += 1
                output[row_end-1][j] = count
            row_end -= 1
            
            #Move bottom to top
            for i in range(row_end, row_start, -1): 
                count += 1
                output[i][column_start] = count
            column_start += 1
            
        return output
    
A = 80

ans = Solution.generateMatrix(A,A)
print(ans)
