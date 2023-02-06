class DetectSquares():
    def __init__(self):
        self.data = defaultdict(int)
    
    def add(self, point):
        self.data[tuple(point)]+=1
    
    def count(self, point):
        a=point[0]
        b=point[1]
        
        count=0 
        for i in range(1,1001): 
            if (a+i,b) in self.data and (a,b+i) in self.data and (a+i,b+i) in self.data:
                count+=(self.data[(a+i,b)]*self.data[(a,b+i)]*self.data[(a+i,b+i)])
                
            if (a+i,b) in self.data and (a,b-i) in self.data and (a+i,b-i) in self.data:
                count+=(self.data[(a+i,b)]*self.data[(a,b-i)]*self.data[(a+i,b-i)])
                
            if (a-i,b) in self.data and (a,b+i) in self.data and (a-i,b+i) in self.data:
                count+=(self.data[(a-i,b)]*self.data[(a,b+i)]*self.data[(a-i,b+i)])
                
            if (a-i,b) in self.data and (a,b-i) in self.data and (a-i,b-i) in self.data:
                count+=(self.data[(a-i,b)]*self.data[(a,b-i)]*self.data[(a-i,b-i)])
        
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)