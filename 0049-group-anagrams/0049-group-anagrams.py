class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            c = ''.join(sorted(s))

            result[c].append(s)
        
        answer = []
        for key, value in result.items():
            answer.append(value)
        
        return answer
