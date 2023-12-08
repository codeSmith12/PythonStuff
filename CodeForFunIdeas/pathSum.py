from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass

targetSum = 22
s = Solution()
s.hasPathSum([5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum)