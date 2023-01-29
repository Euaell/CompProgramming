class Solution:
    def maximumTime(self, time: str) -> str:
        tmp = time.split(':')
        
        hour = list(tmp[0])
        minute = list(tmp[1])
        
        if hour[0] == '?':
            if hour[1] == '?' or ord(hour[1]) < ord('4'):
                hour[0] = '2'
            else:
                hour[0] = '1'
                
        
        if hour[1] == '?':
            if hour[0] == '2':
                hour[1] = '3'
            else:
                hour[1] = '9'
        
        if minute[0] == '?':
            minute[0] = '5'
        
        if minute[1] == '?':
            minute[1] = '9'
        
        
        return "".join(hour) + ":" + "".join(minute)