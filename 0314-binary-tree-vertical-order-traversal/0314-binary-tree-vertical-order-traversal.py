# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columns = defaultdict(list)
        queue = deque([(root, 0)]) #O(n) for node
        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)
            
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        low = min(columns.keys()) 
        high = max(columns.keys()) + 1 # dont use len(columns.keys()) because it will consider nulls on the output

        return [columns[col] for col in range(low, high)]

#: T: O(n) where n is the nodes
#: S: O(n) where n is the nodes