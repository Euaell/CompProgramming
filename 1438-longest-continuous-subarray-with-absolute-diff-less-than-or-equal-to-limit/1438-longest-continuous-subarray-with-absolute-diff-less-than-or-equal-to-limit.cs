public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        int n = nums.Length;
        
        LinkedList<int> min = new();
        LinkedList<int> max = new();

        int ans = 0;
        
        int left = 0;
        for (int i = 0; i < n; i++)
        {
            while (max.Count > 0 && nums[i] > max.Last.Value) max.RemoveLast();
            while (min.Count > 0 && nums[i] < min.Last.Value) min.RemoveLast();
            
            min.AddLast(nums[i]);
            max.AddLast(nums[i]);

            while (max.First.Value - min.First.Value > limit)
            {
                if (max.First.Value == nums[left]) max.RemoveFirst();
                if (min.First.Value == nums[left]) min.RemoveFirst();
                left++;
            }

            ans = Math.Max(ans, i - left + 1);
        }

        return ans;
    }
}