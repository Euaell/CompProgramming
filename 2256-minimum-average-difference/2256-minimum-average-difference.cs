public class Solution {
    public int MinimumAverageDifference(int[] nums) {
        int n = nums.Length;
        long[] preF = new long[n + 1];
        for (int i = 0; i < n; i++)
            preF[i + 1] = nums[i] + preF[i];
        
        long min = long.MaxValue;
        int ans = 0;
        
        for (int i = 1; i <= n; i++) {
            long lowerAvg = (preF[i] - preF[0]) / i;
            long upperAvg = (preF[n] - preF[i]) / (n - i != 0 ? (n - i) : 1);
            if (min > Math.Abs(upperAvg - lowerAvg)) {
                min = Math.Abs(upperAvg - lowerAvg);
                ans = i - 1;
            }
        }            
        
        return ans;
    }
}