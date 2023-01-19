class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # holds the number of a specific modulo occured so far
        dict = {}
        
        dict[0] = 1
        
        ans = 0
        
        Sum = 0
        for i in range(n):
            Sum += nums[i]
            Sum %= k
            
            if Sum in dict:
                ans += dict[Sum]
                dict[Sum] += 1
            else:
                dict[Sum] = 1
            
        return ans
        