class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = inf
        
        black = 0
        left = 0
        for i in range(n):
            if blocks[i] == 'B':
                black += 1
            if i - left + 1 == k:
                ans = min(ans, (i - left + 1) - black)
                
                if blocks[left] == 'B':
                    black -= 1
                
                left += 1
            
        return ans            
            