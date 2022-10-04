public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        int[] cand = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        
        IList<IList<int>> ans = new List<IList<int>>();
        
        void rec(int amount, int ind, int count, List<int> l) {
            if (amount > n || count > k) return;
            if (amount == n && count == k) {
                ans.Add(new List<int>(l));
                return;
            }
            
            for (int i = ind; i <= 9; i++) {
                l.Add(i);
                rec(amount + i, i + 1, count + 1, l);
                l.RemoveAt(l.Count - 1);
            }
        }
        rec(0, 1, 0, new List<int>());
        
        return ans;
    }
}