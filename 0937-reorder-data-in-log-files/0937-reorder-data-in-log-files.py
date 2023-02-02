class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letr = []
        dig = []
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                letr.append(log)
        letr.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letr + dig