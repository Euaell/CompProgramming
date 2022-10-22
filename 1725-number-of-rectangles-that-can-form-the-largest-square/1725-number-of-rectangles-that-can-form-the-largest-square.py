class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dict = {}
        
        m = 0
        
        for l, w in rectangles:
            tmp = min(l, w)
            if tmp not in dict:
                dict[tmp] = 0
            
            dict[tmp] += 1
        
        m = -inf
        for i in dict.keys():
            m = max(i, m)
        
        return dict[m]