class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = [1, i, i] # freq, start, end
            else:
                freq[num][0] += 1
                freq[num][2] = i
        max_freq, min_length = 0, len(nums)
        for num in freq:
            if freq[num][0] > max_freq:
                max_freq = freq[num][0]
                min_length = freq[num][2] - freq[num][1] + 1
            elif freq[num][0] == max_freq:
                min_length = min(min_length, freq[num][2] - freq[num][1] + 1)
        return min_length