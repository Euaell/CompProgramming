public class Solution {
    public long CountSubarrays(int[] nums, long k) {
        int n = nums.Length;
        
        long ans = 0;
        int left = 0;
        
        long sum = 0;
        long score = 0;
        
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            score = sum * (i - left + 1);
            while (score >= k) {
                sum -= nums[left];
                left++;
                score = sum * (i - left + 1);
            }
            ans += i - left + 1;
            
        }
        
        return ans;
    }
}