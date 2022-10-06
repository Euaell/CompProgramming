public class TimeMap {
   Dictionary<string, List<(int, string)>> map;
    
    public TimeMap() {
        map = new Dictionary<string, List<(int, string)>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        if(map.TryGetValue(key, out var list)) {
            list.Add((timestamp, value));
        } else {
            var newList = new List<(int, string)>();
            newList.Add((timestamp, value));
            map.Add(key,newList);
        }
    }
    
    public string Get(string key, int timestamp) {
        if(map.TryGetValue(key, out var list)) {
           return BinarySearch(0, list.Count - 1, list, timestamp);
        } else {
            return string.Empty;
        }
    }
    
    private string BinarySearch(int start, int end, List<(int, string)> list, int target) {
        var lastMid = -1;
        
        while(start <= end) {
            var mid = (end - start) / 2 + start;
            lastMid = mid;
            
            if(list[mid].Item1 == target) {
                return list[mid].Item2;
            } else if(list[mid].Item1 > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        if(list.Count != 0 && end >= 0 && end < list.Count) return list[end].Item2;
        
        return string.Empty;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.Set(key,value,timestamp);
 * string param_2 = obj.Get(key,timestamp);
 */