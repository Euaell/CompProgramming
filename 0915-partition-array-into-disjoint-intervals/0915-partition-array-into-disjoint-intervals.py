class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        
        minArr = [0] * n # backward
        maxArr = [0] * n # forward
        
        j = 0
        ma = 0
        for i in range(n):
            ma = max(ma, nums[i])
            maxArr[i] = ma
        
        mi = inf
        for i in range(n - 1, -1, -1):
            mi = min(mi, nums[i])
            minArr[i] = mi
        
        # print(maxArr)
        # print(minArr)
        
        for i in range(n - 1):
            if minArr[i + 1] >= maxArr[i]:
                return i + 1
        
        return 0