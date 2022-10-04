public class Solution {
    public int[] FinalPrices(int[] prices) {
        int n = prices.Length;
        int[] ans = new int[n];
        
        // for (int i = 0; i < n; i++) {
        //     int tmp = prices[i];
        //     for (int j = i + 1; j < n; j++) 
        //         if (prices[j] <= prices[i]) {
        //             tmp -= prices[j];
        //             break;
        //         }
        //     ans[i] = tmp;
        // }
        
        
        // Using monotonic stack
        
        Stack<int> stk = new(); 
        
        for (int i = n - 1; i >= 0; i--) {
            int tmp = prices[i];
            
            while (stk.Any() && prices[i] < stk.Peek()) 
                stk.Pop();
            
            if (stk.Any()) tmp -= stk.Peek();
            
            ans[i] = tmp;
            stk.Push(prices[i]);
        }
        
        return ans;
    }
}