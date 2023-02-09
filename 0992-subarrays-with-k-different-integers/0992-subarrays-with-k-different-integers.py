class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            left = 0
            count = Counter()
            res = 0
            for right, num in enumerate(nums):
                if count[num] == 0:
                    k -= 1
                count[num] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res
        return atMostK(k) - atMostK(k - 1)