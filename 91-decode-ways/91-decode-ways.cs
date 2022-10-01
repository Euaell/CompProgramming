public class Solution {
    public int NumDecodings(string s) {
        int n = s.Length;
        
        Dictionary<string, int> dict = new();
        
        int rec(string x) {
            if (string.IsNullOrEmpty(x)) return 1;
            if (x[0] == '0') return 0;
            if (!dict.ContainsKey(x)) {
                if (x.Length == 1) dict[x] = 1;
                else {
                    int ans = 0;

                    if (x[0] == '1' || x[0] == '2' && x[1] != '7' && x[1] != '8' && x[1] != '9') {
                        ans += rec(x[2..]);
                    }

                    ans += rec(x[1..]);
                    dict[x] = ans;
                }
            }
            
            return dict[x];
        }
        
        return rec(s);        
    }
}