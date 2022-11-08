class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # first find the xor of the two numbers
        xor = 0
        for num in nums:
            xor ^= num
        
        # find the least significant bit of the xor
        # # usually
        # k = 0
        # while k < 31:
        #     # check if the kth bit is on starting from the right
        #     if (1 << k) & xor == 1:
        #         break
        #     k += 1
        # 
        # lsd = 1 << k
        # just perform a bitwise and with its negative
        d = xor & -xor

        # partition the array in two places
        left = 0
        right = 0

        for num in nums:
            if num & d == 0:
                left ^= num
            else:
                right ^= num
        
        return [left, right]
        