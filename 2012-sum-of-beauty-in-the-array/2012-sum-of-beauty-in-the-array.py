class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        
        minArr = [0] * n # backward
        maxArr = [0] * n # forward
        
        ma = nums[0]
        for i in range(n):
            ma = max(ma, nums[i])
            maxArr[i] = ma
        
        mi = nums[n - 1]
        for i in range(n - 1, -1, -1):
            mi = min(mi, nums[i])
            minArr[i] = mi
        
        score = 0
        for i in range(1, n - 1):
            if maxArr[i - 1] < nums[i] < minArr[i + 1]:
                score += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                score += 1
            
        # print(maxArr)
        # print(minArr)
        
        return score
    