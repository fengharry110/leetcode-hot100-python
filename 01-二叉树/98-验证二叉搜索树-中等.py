"""
98. 验证二叉搜索树
https://leetcode.cn/problems/validate-binary-search-tree/description/

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
- 节点的左子树只包含 小于 当前节点的数。
- 节点的右子树只包含 大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        递归解法：
        - 每个节点有上下界限制
        - 左子树的所有节点值必须小于当前节点值
        - 右子树的所有节点值必须大于当前节点值
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            
            # 当前节点值必须在(min_val, max_val)范围内
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 左子树：上界变为当前节点值
            # 右子树：下界变为当前节点值
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        # 初始范围使用负无穷和正无穷
        return validate(root, float('-inf'), float('inf'))


class SolutionInorder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        中序遍历解法：
        - 二叉搜索树的中序遍历结果是递增的
        - 检查中序遍历结果是否严格递增
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        self.prev_val = float('-inf')
        
        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # 遍历左子树
            if not inorder(node.left):
                return False
            
            # 检查当前节点值是否大于前一个值
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            
            # 遍历右子树
            return inorder(node.right)
        
        return inorder(root)
