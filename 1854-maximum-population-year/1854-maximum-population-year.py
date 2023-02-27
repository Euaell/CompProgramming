class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = len(logs)
        
        pref = [0] * 101
        
        for log in logs:
            birth = log[0] - 1950
            det = log[1] - 1950
            
            pref[birth] += 1
            pref[det] -= 1
        
        for i in range(1, 101):
            pref[i] += pref[i - 1]
        
        ans = 0
        for i in range(101):
            if pref[i] > pref[ans]:
                ans = i
        # print(pref)
        return ans + 1950