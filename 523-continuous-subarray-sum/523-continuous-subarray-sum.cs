public class Solution {
    public bool CheckSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        Dictionary<int, int> dict = new Dictionary<int, int>();
        dict.Add(0, -1);
        
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];  
            int tmp = sum % k;
            if (!dict.ContainsKey(tmp)) dict.Add(tmp, i);
            else if (i - dict[tmp] >= 2) return true; 
        }
        
        return false;
    }
}