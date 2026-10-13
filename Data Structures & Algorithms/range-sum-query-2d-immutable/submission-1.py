class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_store=[]
        self.sum_store.append([0]*(len(matrix[0])+1))

        for i, line in enumerate(matrix):
            self.sum_store.append([0])
            sum_line=0
            for j, digit in enumerate(line):
                sum_line+=digit
                if i>0:
                    self.sum_store[-1].append(sum_line+self.sum_store[i][j+1])
                else:
                    self.sum_store[-1].append(sum_line)

        print(self.sum_store)        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       
        return (self.sum_store[row1][col1]
        +self.sum_store[row2+1][col2+1]
        -self.sum_store[row1][col2+1]
        -self.sum_store[row2+1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)