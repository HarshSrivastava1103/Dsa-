from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        queue = deque([root, 'n'])
        res = [root.val]
        while len(queue) != 1:
            R = queue.popleft()
            if R == 'n':
                res.append(queue[-1].val)
                queue.append('n')
            else:
                if R.left is not None:
                    queue.append(R.left)
                if R.right is not None:
                    queue.append(R.right)
        return res