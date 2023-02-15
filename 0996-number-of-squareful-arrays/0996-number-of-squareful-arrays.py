class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        res = []
        visited = [0] * len(A)
        A.sort()
        def helper(nums,out, res):
            if len(out) == len(nums):
                res.append(out[:])
                return
            else:

                for i in range(len(A)):
                    if visited[i]:
                        continue
                    if i > 0 and A[i] == A[i-1] and visited[i -1]:
                        continue                   
       
                    if (len(out) >= 2 and sqrt(out[-1] + out[-2]) != int(sqrt(out[-1] + out[-2]))) or (len(out) >= 1 and sqrt(out[-1] +A[i]) != int(sqrt(out[-1] +A[i]))):
                        continue
                    
                    visited[i] = 1
                    
                    out.append(A[i])
                    
                    helper(nums,out, res)
                    out.pop()
                    visited[i] = 0
                    
        helper(A, [], res)
        
        return len(res)
    
    