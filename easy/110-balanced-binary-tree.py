from idlelib.tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return [True, 0]

        left = dfs(root.left)
        right = dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, max(left[1], right[1]) + 1]

    return dfs(root)[0]


if __name__ == '__main__':
    # example 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(isBalanced(root))