class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordDict = defaultdict(int)
        for word in words:
            wordDict[word] += 1
        
        flag = False
        answer = 0
        for word in words:
            rev = word[::-1]
            if (rev == word and wordDict[rev] > 1) or (rev != word and wordDict[rev] > 0 and wordDict[word] > 0):
                wordDict[word] -= 1
                wordDict[rev] -= 1
                answer += 4
            elif word == word[::-1] and wordDict[word] > 0 and not flag:
                answer += 2
                wordDict[word] -= 1
                flag = True
        return answer