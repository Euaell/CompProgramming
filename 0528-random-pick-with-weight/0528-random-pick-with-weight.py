class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.w_sum = sum(w)
        self.w_cumsum = list(accumulate(w))       

    def pickIndex(self) -> int:
        rand = random.randint(1, self.w_sum)
        return bisect.bisect_left(self.w_cumsum, rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()