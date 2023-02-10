class Solution:  
    def shiftCount(self, x_shift, y_shift, M, R, n):
            leftShift = 0
            rightShift = 0
            
            for r_row, m_row in enumerate(range(y_shift, n)):
                for r_col, m_col in enumerate(range(x_shift, n)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        leftShift += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        rightShift += 1

            return max(leftShift, rightShift)
    
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)        

        ans = 0
        for y in range(n):
            for x in range(n):
                ans = max(ans, self.shiftCount(x, y, img1, img2, n))
                ans = max(ans, self.shiftCount(x, y, img2, img1, n))

        return ans