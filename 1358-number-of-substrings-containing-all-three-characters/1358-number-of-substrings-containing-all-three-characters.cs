public class Solution {
    public int NumberOfSubstrings(string s) {
        int n = s.Length;
        int[] dict = new int[3];
        
        bool check() {
            return dict[0] > 0 && dict[1] > 0 && dict[2] > 0;
        }
        
        int ans = 0;
        
        int left = 0;
        for (int i = 0; i < n; i++) {
            dict[s[i] - 'a']++;
            while (check()) { 
                ans += n - i;
                dict[s[left++] - 'a']--;
            }
        }
        
        return ans;
    }
}