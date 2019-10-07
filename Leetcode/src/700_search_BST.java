/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null){return null;}
        else if(root.val == val){return root;}
        else{TreeNode ans = searchBST(root.left, val);
            if(ans == null){return searchBST(root.right, val);}
             else{return ans;}
            }
        
    }
}