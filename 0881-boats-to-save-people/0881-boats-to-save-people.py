class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        
        ans = 0
        
        left = 0
        right = n - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                
            ans += 1
            right -= 1
        return ans