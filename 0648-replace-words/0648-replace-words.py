class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isCompleteWord = True
    
    def search(self, word: str) -> str:
        curr = self.root
        
        ans = ""        
        for c in word:
            if c not in curr.children:
                return ""
            ans += c
            curr = curr.children[c]
            if curr.isCompleteWord:
                return ans
            
            
        if curr.isCompleteWord:
            return ans
        return ""
    
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        
        given = sentence.split(' ')
        
        for i in range(len(given)):
            tmp = trie.search(given[i])
            if tmp != "":
                given[i] = tmp
        
        return " ".join(given)
        