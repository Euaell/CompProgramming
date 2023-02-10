class Solution:
    def mergeCount(self, n1, n2):
        n = len(n1) + len(n2)
        
        tmp = [0] * n
        j1 = 0
        j2 = 0
        for i in range(n):
            if j1 < len(n1) and j2 < len(n2):
                if n1[j1] < n2[j2]:
                    tmp[i] = n1[j1]
                    j1 += 1
                else:
                    tmp[i] = n2[j2]
                    j2 += 1
            elif j1 < len(n1):
                tmp[i] = n1[j1]
                j1 += 1
            else:
                tmp[i] = n2[j2]
                j2 += 1
        
        if n % 2 == 1:
            return tmp[n // 2]
        
        left = math.floor(n / 2 - 1)
        right = math.ceil(n / 2)
        
        return (tmp[left] + tmp[right]) / 2
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        return self.mergeCount(nums1, nums2)
        
        