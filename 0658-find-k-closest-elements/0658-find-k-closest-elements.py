class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # binary search for the positions of x (or insert position) in nums
        
        left = 0
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
            
            if arr[mid] >= x:
                right = mid - 1
            else:
                left = mid + 1
        
        # use two pointers to find the range in arr with size = k, that are close to x
        l = left
        r = right
        while l < n and r >= 0 and k > 0:
            if arr[l] - x >= x - arr[r]:
                r -= 1
            else:
                l += 1
            
            k -= 1
        
        while l < n and k > 0:
            l += 1
            k -= 1
        
        while r >= 0 and k > 0:
            r -= 1
            k -= 1
        
        # both r and l finish the loop just outside the range we want. 
        # so we leave l as is, because the second argument is not inclusive
        # and we increment r to not include an element outside the window
        return arr[r + 1:l]