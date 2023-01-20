class Solution:
    def backTracker(self, nums, path: List[int], i: int, ans) -> None:
        if i < 0:
            return
        tmp = []
        for y, s in ans:
            if nums[i] not in s and (len(y) == 0 or nums[i] <= y[0]):
                tmp.append([[nums[i]] + y, set()])
                s.add(nums[i])
        ans.extend(tmp)
        self.backTracker(nums, path, i - 1, ans)
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = [[[], set()]]
        
        self.backTracker(nums, [], len(nums) - 1, ans)
        
        finalAns = []
        for x, s in ans:
            if len(x) > 1:
                finalAns.append(x)
        
        return finalAns