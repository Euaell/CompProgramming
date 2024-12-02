class TimeMap:

    def __init__(self):
        # initialize a dictionary with key str and value array of tuples (timestamp, value)
        self.content: dict[str, tuple[int, str]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.content:
            self.content[key] = []
        
        self.content[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.content:
            return ""
        
        arr = self.content[key]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return "" if right < 0 else arr[right][1]
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)