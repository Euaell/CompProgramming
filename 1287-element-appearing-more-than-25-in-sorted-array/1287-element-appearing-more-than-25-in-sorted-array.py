class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        prevVal = arr[0]
        counter = 1
        
        ans = -1
        for i in range(1, n):
            if arr[i] == prevVal:
                counter += 1
            else:
                prevVal = arr[i]
                counter = 1
            
            if counter > n * 0.25:
                return arr[i]
        
        return prevVal
