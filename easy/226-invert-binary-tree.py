# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    stack = [root]

    while stack:
        node = stack.pop()

        # handle children
        left = node.left
        right = node.right
        if left:
            stack.append(left)
        if right:
            stack.append(right)

        # swap values
        node.left = right if right else None
        node.right = left if left else None
        """
        if left and right:
            node.left = right
            node.right = left
        """

    return root


if __name__ == '__main__':
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(7, TreeNode(6), TreeNode(9))
    root = TreeNode(4, left, right)

    stack = [root]
    while stack:
        node = stack.pop()

        left = node.left
        right = node.right

        print("\ncurrent root {}".format(node.val))

        if left:
            print("left node {}".format(left.val))
            stack.append(left)

        if right:
            print("right node {}".format(right.val))
            stack.append(right)

    print("INVERT")
    root2 = invertTree(root)
    print("AFTER INVERTING")
    stack = [root2]
    while stack:
        node = stack.pop()

        left = node.left
        right = node.right

        print("\ncurrent root {}".format(node.val))

        if left:
            print("left node {}".format(left.val))
            stack.append(left)

        if right:
            print("right node {}".format(right.val))
            stack.append(right)
