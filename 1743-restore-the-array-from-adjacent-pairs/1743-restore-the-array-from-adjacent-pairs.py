class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        uniqueNums = {}
        dict = {}
        nums = []
        
        for item in adjacentPairs:
            if item[0] not in uniqueNums:
                uniqueNums[item[0]] = 0
            
            if item[1] not in uniqueNums:
                uniqueNums[item[1]] = 0
            
            uniqueNums[item[0]] += 1
            uniqueNums[item[1]] += 1
            
            if item[0] not in dict:
                dict[item[0]] = []
            
            if item[1] not in dict:
                dict[item[1]] = []
            
            dict[item[0]].append(item[1])
            dict[item[1]].append(item[0])
        
        num = [key for key,value in uniqueNums.items() if value == 1][0]
        
        self.dfs(dict,num, set(),nums)
        
        return nums
    
    def dfs(self,dict,num,visited,nums):
        if num in visited:
            return
        
        visited.add(num)
        nums.append(num)
        
        for item in dict[num]:
            self.dfs(dict,item,visited,nums)