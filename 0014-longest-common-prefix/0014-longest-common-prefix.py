class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def checker(s: str, ans: list) -> None:
            i = 0
            j = 0
            while i < len(s) and j < len(ans):
                if s[i] != ans[j]:
                    del ans[j:]
                i += 1
                j += 1
        
        
        strs.sort(key=len)
        
        ans = list(strs[0])
        
        for s in strs:
            checker(s, ans)
            if len(ans) == 0:
                break
        
        return "".join(ans)
    