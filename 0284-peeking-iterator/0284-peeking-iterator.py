class PeekingIterator:
    def __init__(self, iterator):
        self.ind = iterator
        self.c = 1
        self.current = self.ind.next()
        
    def peek(self):     
        return self.current        

    def next(self):
        num = self.current
        self.current = self.ind.next()
        return num
    
    def hasNext(self) -> bool:
        return self.current and 1 <= self.current <= 1000
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].