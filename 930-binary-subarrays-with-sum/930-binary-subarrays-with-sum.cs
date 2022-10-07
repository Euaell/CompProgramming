public class Solution {
    public int NumSubarraysWithSum(int[] nums, int goal) {
        int n = nums.Length;
        Dictionary<int, int> dict = new();
        
        dict[0] = 1;
        
        int ans = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            ans += dict.ContainsKey(sum - goal) ? dict[sum - goal] : 0;
            if (!dict.ContainsKey(sum)) dict.Add(sum, 0);
            dict[sum]++;
        }
        
        return ans;
    }
}