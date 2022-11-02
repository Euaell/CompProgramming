class Solution:
    def findComplement(self, num: int) -> int:
        shift = 1
        # count the number of digit in binary
        digits = floor(log2(num)) + 1
        
        shift <<= digits
        
        num ^= shift - 1
            
        return num