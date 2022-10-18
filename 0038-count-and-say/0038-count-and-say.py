class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        y = self.countAndSay(n - 1)
        
        ans = ""
        
        i = 0
        while i < len(y):
                
            j = i
            while j < len(y) and y[j] == y[i]:
                j += 1

            count = j - i  

            ans += str(count) + str(y[i])
            i = j
            
        return ans