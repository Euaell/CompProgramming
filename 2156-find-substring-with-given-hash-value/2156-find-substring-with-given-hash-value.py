class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        
        currHash = 0
        
        t = k - 1
        right = n - 1
        
        ans = ""
        
        lastPower = pow(power, k - 1, modulo)
        
        for left in range(n - 1, -1, -1):
            currHash = (currHash + ((ord(s[left]) - 96) % modulo) * pow(power, t, modulo)) % modulo
            
            if right - left + 1 == k:
                # check the hash
                if currHash % modulo == hashValue:
                    ans = s[left: right + 1]
                
                #substract the right
                currHash -= ((ord(s[right]) - 96) * lastPower) % modulo
                currHash = (currHash * power) % modulo
                right -= 1
            else:
                # decrease the power until we find the right window length which is k
                t -= 1
                
        return ans