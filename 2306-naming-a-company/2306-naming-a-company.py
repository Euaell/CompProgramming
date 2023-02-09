class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        
        arr = [set() for _ in range(26)]
        
        for idea in ideas:
            arr[ord(idea[0]) - ord('a')].add(idea[1:])
         
        ans = 0
        for i in range(26):
            for j in range(i + 1, 26):
                intNo = len(arr[i].intersection(arr[j]))
                ans += 2 * (len(arr[i]) - intNo) * (len(arr[j]) - intNo)
        
        return ans
        