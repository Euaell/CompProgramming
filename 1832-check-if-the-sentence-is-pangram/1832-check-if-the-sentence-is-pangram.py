class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        vis = set(sentence)
        return len(vis) == 26
            