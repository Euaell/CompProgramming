class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        
        i = 0
        j = 0
        stk = []
        while i < n and j < n:
            if len(stk) > 0 and popped[j] == stk[-1]:
                stk.pop()
                j += 1
            else:
                stk.append(pushed[i])
                i += 1
            # print(stk)
            
        while j < n and len(stk) > 0 and popped[j] == stk[-1]:
            stk.pop()
            j += 1
            # print(stk)
        
        return i == n and j == n
    