public class Solution {
    
    private (int, int)[] directions = {(1, 0), (0, 1), (-1, 0), (0, -1)};
    
    public int NearestExit(char[][] maze, int[] e) {
        int n = maze.Length;
        int m = maze[0].Length;
        
        var que = new Queue<(int, int)>();
        
        bool IsValid((int, int) p) {
            return p.Item1 < n && p.Item1 >= 0 && p.Item2 < m && p.Item2 >= 0 && maze[p.Item1][p.Item2] == '.';
        }

        bool IsExit((int, int) p)
        {
            return p != (e[0], e[1]) && (p.Item1 == 0 || p.Item1 == n - 1 || p.Item2 == 0 || p.Item2 == m - 1);
        }
        
        que.Enqueue((e[0], e[1]));
        int ans = 0;
        while (que.Any())
        {
            for (int size = que.Count; size > 0; size--)
            {
                var (row, col) = que.Dequeue();
                if (!IsValid((row, col))) continue;
                maze[row][col] = '+';
                if (IsExit((row, col))) return ans;
                foreach (var point in directions.Select(p => (p.Item1 + row, p.Item2 + col)))
                    if (IsValid(point)) que.Enqueue(point);
            }
            ans++;
        }
        
        return -1;
    }
}