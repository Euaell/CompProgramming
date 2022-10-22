class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = defaultdict(self.default_Val)
    
    def default_Val(self):
        return -1
    
    def insert(self, val: int) -> bool:
        if self.dict[val] != -1:
            return False
        
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if self.dict[val] == -1:
            return False
        
        index = self.dict[val]
        self.dict[self.arr[-1]] = index
        
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        self.arr.pop()
        
        self.dict[val] = -1
        
        return True

    def getRandom(self) -> int:
        rnd = randint(0, len(self.arr) - 1)
        return self.arr[rnd]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()