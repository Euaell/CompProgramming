class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in hs:
                return [hs[diff], i]
            
            hs[num] = i
            
        return [-1, -1]
        
