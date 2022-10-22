class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.dict = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.arr))
        self.arr.append(val)        
        
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if len(self.dict[val]) == 0:
            return False
        
        valIndex = self.dict[val].pop()
        lastVal = self.arr[-1]
        
        self.dict[lastVal].add(valIndex)
        self.dict[lastVal].discard(len(self.arr) - 1)
        
        self.arr[valIndex], self.arr[-1] = self.arr[-1], self.arr[valIndex]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()