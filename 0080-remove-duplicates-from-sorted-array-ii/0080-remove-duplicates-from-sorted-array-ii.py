class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        c = 1
        last = nums[0]
        for i in range(1, n):
            if nums[i] == last:
                c += 1
            else:
                last = nums[i]
                c = 1
            
            if c > 2:
                nums[i] = '$'
        
        # using 2 pointer
        left = 0
        for i in range(n):
            while nums[left] != '$' and left < i:
                left += 1
            nums[i], nums[left] = nums[left], nums[i]
            
        k = 0
        for i in range(n):
            if nums[i] != '$':
                k += 1
        return k