public class TimeMap {
    private Dictionary<string, List<(int, string)>> dict;
    public TimeMap() {
        dict = new();
    }
    
    public void Set(string key, string value, int timestamp) {
        if (!dict.ContainsKey(key)) dict.Add(key, new());
        dict[key].Add((timestamp, value));
    }
    
    public string Get(string key, int timestamp) {
        if (!dict.ContainsKey(key)) return "";
        int left = 0;
        int right = dict[key].Count - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (dict[key][mid].Item1 > timestamp) 
                right = mid - 1;
            else left = mid + 1;
        }
        if (right < 0) return "";
        
        return dict[key][right].Item2;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.Set(key,value,timestamp);
 * string param_2 = obj.Get(key,timestamp);
 */