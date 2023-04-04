class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        dict = {}
        
        ans = 0
        left = 0
        for i in range(n):
            if s[i] in dict:
                ans += 1
                left = i
                dict.clear()
            
            dict[s[i]] = 0
        
        ans += 1
        
        # for key, value in sDict.items():         
        #     print("key: ", key, "value: ", value)
        
        return ans