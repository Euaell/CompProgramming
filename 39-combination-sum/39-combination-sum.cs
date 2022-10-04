public class Solution {
    public IList<IList<int>> CombinationSum(int[] c, int target) {
        int n = c.Length;
        
        IList<IList<int>> ans = new List<IList<int>>();
        void rec(int amount, int index, List<int> l) {
            if (amount > target) return;
            if (amount == target) {
                ans.Add(new List<int>(l));
                return;
            }
            
            for (int i = index; i < n; i++) {
                l.Add(c[i]);
                rec(amount + c[i], i, l);
                l.RemoveAt(l.Count - 1);
            }
        }
        rec(0, 0, new List<int>());
        
        return ans;
    }
}