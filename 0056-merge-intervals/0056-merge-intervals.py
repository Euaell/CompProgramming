class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by start time
        intervals.sort(key = lambda x: x[0])
        
        last = -1
        start = 0
        
        answer = []
        
        for i in intervals:
            if i[0] > last:
                answer.append([start, last])
                start = i[0]
                last = i[1]
            else: 
                last = max(last, i[1])
        
        answer.append([start, last])
        
        return answer[1:]