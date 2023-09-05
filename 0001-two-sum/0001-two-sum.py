class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict = {}
        
        for i in range(n):
            x = target - nums[i]
            if x in dict:
                return [dict[x], i]
            
            dict[nums[i]] = i