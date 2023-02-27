# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.rec(nestedList)
        
        self.arr = self.arr[::-1]
    
    def rec(self, nestedList):
        
        if(type(nestedList) == list):
            for i in nestedList:
                self.rec(i)
            return
        
        if(nestedList.isInteger()):
            self.arr.append(nestedList.getInteger())

        res = nestedList.getList()
        if(res):
            self.rec(res)
    
    def next(self) -> int:
        return self.arr.pop()
    
    def hasNext(self) -> bool:
         return len(self.arr) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())