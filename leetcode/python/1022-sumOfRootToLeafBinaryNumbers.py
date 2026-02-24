from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def make_tree(values: List[Optional[int]]) -> Optional["TreeNode"]:
        if not values:
            return None
        
        root = TreeNode(values[0]) #type: ignore
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i]) #type: ignore
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i]) #type: ignore
                queue.append(node.right)
            i += 1
        
        return root   
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traversal(node: Optional[TreeNode], curVal: int) -> int:
            if not node:
                return 0
            curVal = (curVal << 1) + node.val
            
            if not node.left and not node.right:
                return curVal
            
            return traversal(node.left, curVal) + traversal(node.right, curVal)
        return traversal(root, 0)
    
def main():
    s = Solution()
    root = TreeNode.make_tree([1, 0, 1, 0, 1, 0, 1])
    print(s.sumRootToLeaf(root))
    
if __name__ == "__main__":
    main()
    