class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        
        h = []
        
        for i in freq:
            heapq.heappush(h, (-freq[i], i))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(h)[1])
        
        return ans