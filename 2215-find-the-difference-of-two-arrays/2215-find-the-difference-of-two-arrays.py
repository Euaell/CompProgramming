class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        
        for x in nums2:
            if x in n1:
                n1.remove(x)
        
        for x in nums1:
            if x in n2:
                n2.remove(x)
        
        return [list(n1), list(n2)]        
        