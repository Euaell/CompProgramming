class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for j in range(m):
            last = 'a'
            for i in range(n):
                if strs[i][j] >= last:
                    last = strs[i][j]
                else:
                    count += 1
                    break
        
        return count