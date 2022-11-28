class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # hold a dictionary of players with losing values
        lose = {}
        for w, l in matches:
            if w not in lose:
                lose[w] = 0
            if l not in lose:
                lose[l] = 0
            
            lose[l] += 1
        
        answer = [[], []]
        for key in lose.keys():
            if lose[key] < 2:
                answer[lose[key]].append(key)
                
        return [sorted(answer[0]), sorted(answer[1])]