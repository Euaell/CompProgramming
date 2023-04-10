class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        
        dict = {
            ']' : '[', 
            '}' : '{',
            ')' : '('
        }
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if len(stk) == 0 or dict[c] != stk.pop():
                    return False
                
        return len(stk) == 0