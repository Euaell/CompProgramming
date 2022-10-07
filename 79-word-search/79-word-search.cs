
public class Solution {
    private (int, int)[] Directions { get; } = {(1, 0), (0, 1), (-1, 0), (0, -1)};
    public bool Exist(char[][] board, string word) {
        int n = board.Length;
        int m = board[0].Length;
        
        HashSet<(int, int)> path = new();
        
        bool rec(int row, int col, int ind) {
            if (row >= n || row < 0 || col >= m || col < 0) return false;
            
            if (ind == word.Length) return true;
            
            path.Add((row, col));
            
            bool tmp = false;
            foreach (var (r, c) in Directions.Select(p => (p.Item1 + row, p.Item2 + col)))
            {
                if (r >= n || r < 0 || c >= m || c < 0 || path.Contains((r, c))) continue;
                if (!tmp && board[r][c] == word[ind])
                    tmp |= rec(r, c, ind + 1);
                
            }
            
            path.Remove((row, col));

            return tmp;         
        }
        
        bool ans = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!ans && board[i][j] == word[0]) ans = rec(i, j, 1);
            }
        }
        
        return ans;
    }
}