class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # first find (missing ^ duplicate)
        xor = 0
        for i in range(n):
            xor ^= nums[i]
            xor ^= (i + 1)
        print(bin(xor))
        # find the duplicate
        vis = set()
        duplicate = 0
        for num in nums:
            if num in vis:
                duplicate = num
                break
            
            vis.add(num)
        
        return [duplicate, xor ^ duplicate]