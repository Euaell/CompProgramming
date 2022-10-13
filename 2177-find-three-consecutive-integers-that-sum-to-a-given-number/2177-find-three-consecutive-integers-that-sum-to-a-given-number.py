class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        tmp = num // 3
        
        arr = [tmp - 1, tmp, tmp + 1]
        
        return arr if sum(arr)==num else []