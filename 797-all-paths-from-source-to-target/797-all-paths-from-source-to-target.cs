public class Solution {
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {
        int n = graph.Length;
        
        IList<IList<int>> ans = new List<IList<int>>();
        List<int> path = new();
        void dfs(int curr) {
            if (curr == n - 1) {
                ans.Add(new List<int>(path) {curr});
                return;
            }
            path.Add(curr);
            foreach (var v in graph[curr])
                dfs(v);
            
            path.RemoveAt(path.Count - 1);
        }
        dfs(0);
        
        return ans;
    }
}