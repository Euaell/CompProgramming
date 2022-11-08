class Solution:
    def backTrack(self, turnedOn, arr, answer):
        if turnedOn == 0:
            minute = 0
            for i in range(6):
                if arr[i]:
                    minute += 2 ** i
            if minute >= 60:
                return
            hour = 0
            for i in range(6, 10):
                if arr[i]:
                    hour += 2 ** (i - 6)
            if hour >= 12:
                return

            ans = str(hour) + ":" + str(minute).rjust(2, '0')
            answer.add(ans)
            return
        
        for i in range(10):
            if 10 - i < turnedOn:
                return
            if arr[i]: 
                continue
            arr[i] = 1
            self.backTrack(turnedOn - 1, arr, answer)
            arr[i] = 0

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        
        answer = set()
        array = [0] * 10

        self.backTrack(turnedOn, array, answer)

        return answer
