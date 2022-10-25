class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        
        currHash = 0
        t = k - 1
        right = n - 1
        ans = ""
        for left in range(n - 1, -1, -1):
            currHash = (currHash + ((ord(s[left]) - 96) % modulo) * pow(power, t, modulo)) % modulo
            
            if right - left + 1 == k:
                # check the hash
                if currHash % modulo == hashValue:
                    ans = s[left: right + 1]
                
                #substract the right
                currHash -= ((ord(s[right]) - 96) * pow(power, k - 1, modulo)) % modulo
                currHash = (currHash * power) % modulo
                right -= 1
            else:
                t -= 1
                
        return ans