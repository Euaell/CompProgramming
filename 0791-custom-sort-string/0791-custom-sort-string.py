class Solution:
    def customSortString(self, order: str, s: str) -> str:
        n = len(order)
        counterS = Counter(s)
        
        ans = []
        
        for c in order:
            if c in counterS:
                ans.append(c * counterS[c])
                del counterS[c]
                # counterS.pop(c)
        
        for key, value in counterS.items():
            ans.append(key*value)
        
        return "".join(ans)