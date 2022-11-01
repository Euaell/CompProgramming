
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        
        i = 0
        j = 0
        while j < len(secondList) and i < len(firstList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            if end1 >= start2 >= start1 or end1 >= end2 >= start1 or (end1 <= end2 and start1 >= start2) or (end1 >= end2 and start1 <= start2):
                answer.append([max(start1, start2), min(end1, end2)])
            
            if end1 > end2:
                j += 1
            elif end1 < end2:
                i += 1
            else:
                i += 1
                j += 1
                    
        return answer