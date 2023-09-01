class Solution:
    def countBitsOfNum(self, x: int) -> int:
            ans = 0
            while x != 0:
                # check the least significant position to check for '1'
                tmp = x & 1
                if tmp != 0:
                    ans += 1
                # shift the bits to the left
                x >>= 1
                
            return ans
                
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(self.countBitsOfNum(i))
        
        return ans
        