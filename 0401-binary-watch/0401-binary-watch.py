class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        
        for hour in range(12):
            for minute in range(60):
                # change hour and string then count their on bits
                onCount = bin(hour).count('1') + bin(minute).count('1')
                if onCount == turnedOn:
                    ans = str(hour) + ":" + str(minute).rjust(2, '0')
                    answer.append(ans)
                    
        return answer
                