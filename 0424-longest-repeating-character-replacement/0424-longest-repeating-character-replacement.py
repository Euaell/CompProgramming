class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        dict = defaultdict(int)
        
        left = 0
        maxFreq = 0
        ans = 0
        for i in range(n):
            dict[s[i]] += 1
            maxFreq = max(maxFreq, dict[s[i]])
            
            # check if the rest of characters in the window except the most frequent character
            while (i - left + 1) - maxFreq > k:
                dict[s[left]] -= 1
                left += 1
            
            ans = max(ans, i - left + 1)
            
        return ans