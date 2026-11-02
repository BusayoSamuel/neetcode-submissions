/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        function dfs(node){
            if(node === null){
                return [0, true]
            }

            const [lHeight, lBal] = dfs(node.left)
            const [rHeight, rBal] = dfs(node.right)

            if(Math.abs(lHeight - rHeight) > 1){
                return [1 + Math.max(lHeight, rHeight), false]
            }else{
                return [1 + Math.max(lHeight, rHeight), lBal && rBal]
            }
        }

        return dfs(root)[1]
    }
}
