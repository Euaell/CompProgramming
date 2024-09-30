class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.inc_array = []
    
    def is_stack_full(self):
        return len(self.stack) >= self.max_size

    def push(self, x: int) -> None:
        if self.is_stack_full():
            return
        
        self.stack.append(x)
        self.inc_array.append(0)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        inc = self.inc_array.pop()
        if self.inc_array:
            self.inc_array[-1] += inc
        
        return self.stack.pop() + inc
        

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            if self.inc_array:
                self.inc_array[-1] += val
        else:
            self.inc_array[k - 1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)