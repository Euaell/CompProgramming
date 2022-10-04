public class Solution {
    private readonly KeyValuePair<int, int> _df = new KeyValuePair<int, int>(0, 0);
    public int LongestSubarray(int[] nums, int limit) {
        int n = nums.Length;
        
        int ans = 0;

        SortedDictionary<int, int> min = new();
        SortedDictionary<int, int> max = new();
        
        int left = 0;
        for (int i = 0; i < n; i++)
        {
            var elem = nums[i];
            if (!min.ContainsKey(elem)) min.Add(elem, 0);
            min[elem]++;
            if (!max.ContainsKey(-elem)) max.Add(-elem, 0);
            max[-elem]++;

            while (-max.FirstOrDefault(_df).Key - min.FirstOrDefault(_df).Key > limit)
            {
                if (--min[nums[left]] == 0) min.Remove(nums[left]);
                if (--max[-nums[left]] == 0) max.Remove(-nums[left]);
                left++;
            }
            
            ans = Math.Max(ans, i - left + 1);
        }
        
        return ans;
    }
}