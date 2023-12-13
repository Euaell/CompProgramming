class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column_count = {}
        row_count = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    column_count[j] = 1 if j not in column_count else column_count[j] + 1
                    row_count[i] = 1 if i not in row_count else row_count[i] + 1
        
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and column_count[j] == 1 and row_count[i] == 1:
                    ans += 1
        
        return ans
        