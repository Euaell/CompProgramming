class Solution:
    def merge(self, x, y) -> List[int]:
        j = 0
        n = len(x)
        
        k = 0
        m = len(y)
        arr = []
        while j < n and k < m:
            if x[j] < y[k]:
                arr.append(x[j])
                j += 1
            else:
                arr.append(y[k])
                k += 1
        
        while j < n:
            arr.append(x[j])
            j += 1
        while k < m:
            arr.append(y[k])
            k += 1
        
        return arr
    
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        
        return self.merge(left, right)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)