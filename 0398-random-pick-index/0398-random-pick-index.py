class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] not in self.dict:
                self.dict[nums[i]] = []
            
            self.dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        n = len(self.dict[target])
        ans = randint(0, n - 1)
        
        return self.dict[target][ans]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)