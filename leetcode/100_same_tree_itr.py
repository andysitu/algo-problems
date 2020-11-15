# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        node = p
        node2 = q
        stack1 = []
        stack2 = []

        while True:
            if node is not None:
                if node2 is None:
                    return False
                stack1.append(node)
                node = node.left
                stack2.append(node2)
                node2 = node2.left
            elif len(stack1) > 0:
                node = stack1.pop()
                if len(stack2) == 0 or node is not None:
                    return False
                node2 = stack2.pop()

                if node2.val != node.val:
                    return False
                print(node2.val, node.val)
                
                node = node.right
                node2 = node2.right
            else:
                if node2 is not None or len(stack2) > 0:
                    return False
                break
        return True