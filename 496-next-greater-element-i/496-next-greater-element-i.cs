public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] ans = new int[n];
        
        Stack<int> stk = new();
        Dictionary<int, int> dict = new Dictionary<int, int>(nums1.Select((v, i) => new KeyValuePair<int, int>(v, i)));

        for (int i = nums2.Length - 1; i >= 0; i--)
        {
            var elem = nums2[i];
            while (stk.Any() && stk.Peek() < elem)
                stk.Pop();
            if (dict.ContainsKey(elem))
                ans[dict[elem]] = stk.Any() ? stk.Peek() : -1;
            
            stk.Push(elem);
        }
        
        return ans;
        
    }
}