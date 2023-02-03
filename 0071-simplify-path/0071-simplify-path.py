class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_list = path.split('/')
        
        stack = []
        
        for p in path_list:
            if p == '' or p == '.':
                continue    
            elif p == '..':
                if stack:
                    stack.pop()    
            else:
                stack.append(p)
                
        return '/' + '/'.join(stack)