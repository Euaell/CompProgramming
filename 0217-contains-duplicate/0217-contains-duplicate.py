class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vis = set()
        
        for i in range(len(nums)):
            if nums[i] in vis:
                return True
            
            vis.add(nums[i])
        
        return False