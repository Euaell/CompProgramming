public class Solution {
    public string ShiftingLetters(string s, int[] shifts) {
        int n = s.Length;
            
        char[] chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

        int[] preF = new int[n + 1];
        for (int i = n - 1; i >= 0; i--)
            preF[i] = (preF[i + 1] + shifts[i]) % 26;

        char[] ans = new char[n];

        for (int i = 0; i < n; i++)
            ans[i] = chars[(s[i] - 'a' + preF[i]) % 26];

        return string.Join("", ans);
    }
}