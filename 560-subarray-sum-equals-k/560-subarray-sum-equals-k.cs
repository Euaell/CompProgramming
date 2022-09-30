public class Solution {
    public int SubarraySum(int[] nums, int k) {
        int n = nums.Length;;
        Dictionary<int, int> dict = new Dictionary<int, int>();
        dict.Add(0, 1);
        
        int ans = 0;
        int preSum = 0;
        
        for (int i = 0; i < n; i++) {
            preSum += nums[i];
            ans += (dict.ContainsKey(preSum - k) ? dict[preSum - k] : 0);
            if (!dict.ContainsKey(preSum)) dict.Add(preSum, 0);
            dict[preSum]++;
        }
        
        return ans;
    }
}