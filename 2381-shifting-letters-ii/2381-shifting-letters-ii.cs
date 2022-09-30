public class Solution {
    public string ShiftingLetters(string s, int[][] shifts) {
        int n = s.Length;
        char[] chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

        int[] preF = new int[n + 1];
        foreach (var (st, ed, dir) in shifts.Select(x => (x[0], x[1], x[2])))
        {
            int tmp = dir == 0 ? -1 : 1;
            preF[st] += tmp;
            preF[ed + 1] -= tmp;
        }

        char[] ans = new char[n];
        int prev = 0;
        for (int i = 0; i < n; i++)
        {
            prev = (prev + preF[i]) % 26;
            ans[i] = chars[(26 + s[i] - 'a' + prev) % 26];
        }

        return string.Join("", ans);

    }
}