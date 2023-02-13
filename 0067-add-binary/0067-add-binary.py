class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = [0] * max(len(a), len(b))
        
        newA = list(map(int, a[::-1]))
        newB = list(map(int, b[::-1]))
        
        carry = 0
        
        for i in range(len(ans)):
            if len(newA) > i and len(newB) > i:
                tmp = newA[i] + newB[i] + carry
                carry = tmp // 2
                tmp %= 2
                ans[i] = tmp
            elif len(newA) > i:
                tmp = newA[i] + carry
                carry = tmp // 2
                tmp %= 2
                ans[i] = tmp
            elif len(newB) > i:
                tmp = newB[i] + carry
                carry = tmp // 2
                tmp %= 2
                ans[i] = tmp
        
        if carry:
            ans.append(carry)
        
        ans = ans[::-1]
        
        return "".join(map(str, ans))
    