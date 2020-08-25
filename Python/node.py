# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode):
        node = root
        # print(node.val)
        min_diff = 0
        queue = []
        visited = set()

        queue.append(node.val)
        visited.add(node.val)

        while queue != None:
            p = queue.pop()
            print('this is p', p)

            if p not in visited:
                visited.add(p)

                diff = node.val - p
                # print(node.val)

                if diff <= -1:
                    diff * -1

                if diff <= min_diff:
                    min_diff = diff

                node = p.val

            if node.right:
                queue.append(node.right.val)

            if node.left:
                queue.append(node.left.val)

        return min_diff
