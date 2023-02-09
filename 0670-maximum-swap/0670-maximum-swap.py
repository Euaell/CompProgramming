class Solution:
    def maximumSwap(self, num: int) -> int:
        listNum = list(map(int, list(str(num))))
        
        n = len(listNum)
        
        Max = -1
        MaxInd = 0
        
        lastMax = 0
        lastMin = 0
        
        for i in range(n - 1, -1, -1):
            if listNum[i] > Max:
                Max = listNum[i]
                MaxInd = i
            elif listNum[i] < Max:
                lastMin = i
                lastMax = MaxInd
        
        listNum[lastMax], listNum[lastMin] = listNum[lastMin], listNum[lastMax]
        
        return int(''.join([str(num) for num in listNum]))

    