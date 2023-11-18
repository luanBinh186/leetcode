# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if node is None:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count
            subtree_avg = subtree_sum // subtree_count
            if node.val == subtree_avg:
                count += 1
            return subtree_sum, subtree_count
        dfs(root)
        return count