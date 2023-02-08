class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one = -inf
        two = -inf
        three = -inf
        
        for num in nums:
            if num > one:
                three = two
                two = one
                one = num
            elif one > num > two  :
                three = two
                two = num
            elif two > num > three:
                three = num
        
        if three != -inf:
            return three
        
        return one