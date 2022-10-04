public class Solution {
    public int[] FinalPrices(int[] prices) {
        int n = prices.Length;
        int[] ans = new int[n];
        
        for (int i = 0; i < n; i++) {
            int tmp = prices[i];
            for (int j = i + 1; j < n; j++) 
                if (prices[j] <= prices[i]) {
                    tmp -= prices[j];
                    break;
                }
            ans[i] = tmp;
        }
        
        return ans;
    }
}