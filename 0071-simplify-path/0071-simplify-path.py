class Solution:
    def simplifyPath(self, path: str) -> str:
        
        x = path.split('/')
        
        ans = []
        for c in x:
            if c == "..": 
                if len(ans) > 0:
                    ans.pop()
            elif c == "" or c == ".":
                continue
            else:
                ans.append(c)
        
        return "/" + "/".join(ans)
    