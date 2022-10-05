/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode AddOneRow(TreeNode root, int val, int depth) {
        
        if (depth == 1)
            return new TreeNode(val, root);
        
        Queue<TreeNode> que = new();
        que.Enqueue(root);
        
        while (que.Any()) {
            depth--;
            for (int size = que.Count; size > 0; size--) {
                var tmp = que.Dequeue();
                if (depth == 1) {
                    tmp.left = new TreeNode(val, tmp.left);
                    tmp.right = new TreeNode(val, null, tmp.right);
                }
                if (tmp.left != null) que.Enqueue(tmp.left);
                if (tmp.right != null) que.Enqueue(tmp.right);
            }
        }
        
        return root;
    }
}