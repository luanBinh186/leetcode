# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, count_dict):
            if root is not None:
                inorder(root.left, count_dict)
                count_dict[root.val] = count_dict.get(root.val, 0) + 1
                inorder(root.right, count_dict)
        count_dict = {}
        inorder(root, count_dict)
        if not count_dict:
            return []
        max_freq = max(count_dict.values())
        modes = [k for k, v in count_dict.items() if v == max_freq]
        return modes