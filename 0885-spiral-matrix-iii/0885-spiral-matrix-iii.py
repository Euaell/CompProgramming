class Solution:
    
    def isValid(self,row,col,rows,cols):
        
        return 0 <= row < rows and 0 <= col < cols
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        direction = {0 : (0, 1), 1 : (1, 0), 2: (0, -1), 3 : (-1, 0)}
        return self.rec(rStart,cStart,rows,cols,[],0,0,0,direction)
    
    def rec(self,row, col, rows, cols, path, arrow, step, count,direction):
        if len(path)==rows*cols:
            return path
        count %= 2
        if count == 0:
            step += 1
        count += 1
        r,c = direction[arrow]
        
        for i in range(step):
            if self.isValid(row,col,rows,cols):
                path.append((row,col))
            row+=r
            col+=c
        new_arrow = (arrow + 1)% 4
        return self.rec(row,col,rows,cols,path,new_arrow,step,count,direction)
        
        
        
        
        
        