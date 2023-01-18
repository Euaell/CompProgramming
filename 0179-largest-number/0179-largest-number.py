class Solution:
    
    def comp(self, x: str, y: str):
        a = x + y
        b = y + x
        for i in range(len(a)):
            if a[i] != b[i]:
                return ord(b[i]) - ord(a[i])
        return 0
        
    def largestNumber(self, nums: List[int]) -> str:
        newArr = [str(d) for d in nums]
        newArr_sorted = sorted(newArr, key=functools.cmp_to_key(self.comp))
        
        ans = "".join(newArr_sorted)
        if ans[0] == '0':
            return '0'
        
        return ans
    