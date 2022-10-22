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
        
        # remove the last position of val in the array from the dictionary
        valIndex = self.dict[val].pop()
        # get the last value
        lastVal = self.arr[-1]
            
        # place the last value in the array at (position = valIndex)
        # first add the valIndex to the set cause if they are some edge cases
        self.dict[lastVal].add(valIndex)
        # remove the index it was at before by using DISCARD(instead of remove) cause it might have been deleted in the pop in the above code(which happens if there is only one element in the array)
        self.dict[lastVal].discard(len(self.arr) - 1)
        
        # swap the position of the value to be deleted and the last value in the array
        self.arr[valIndex], self.arr[-1] = self.arr[-1], self.arr[valIndex]
        # pop the value from the array
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        # same as the below code
        # rnd = randint(0, len(self.arr) - 1)
        # return self.arr[rnd]
        
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()