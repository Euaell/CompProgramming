public class Solution {
    public IList<IList<int>> CombinationSum2(int[] c, int target) {
        Array.Sort(c);
        
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach(var v in c) {
            if (!dict.ContainsKey(v)) dict.Add(v, 0);
            dict[v]++;
        }
        var arr = dict.Keys.ToArray();
        int n = arr.Length;
        
        IList<IList<int>> ans = new List<IList<int>>();
        
        void rec(int amount, int ind, List<int> l) { 
            if (amount > target) return;
            if (amount == target) {
                ans.Add(new List<int>(l));
                return;
            }
            
            for (int i = ind; i < n; i++) {
                
                for (int j = 1; j <= dict[arr[i]]; j++) {
                    l.Add(arr[i]);
                    rec(amount + (arr[i] * j), i + 1, l);
                }
                for (int j = 0; j < dict[arr[i]]; j++)
                    l.RemoveAt(l.Count - 1);
            }
        }
        rec(0, 0, new List<int>());
        
        return ans;
    }
}