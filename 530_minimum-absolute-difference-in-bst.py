# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev = None

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            nonlocal min_diff
            nonlocal prev
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev.val))
            prev = node
            dfs(node.right)
        dfs(root)

        return min_diff