"""
226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/description/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    """
    二叉树节点类
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        翻转二叉树
        
        参数:
            root: 二叉树根节点
            
        返回:
            翻转后的二叉树根节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: 完整二叉树
    print("=" * 50)
    print("测试用例1: 完整二叉树 [4,2,7,1,3,6,9]")
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    solution = Solution()
    inverted1 = solution.invertTree(root1)
    print(f"翻转后根节点: {inverted1.val}")
    print(f"翻转后左子节点: {inverted1.left.val}")
    print(f"翻转后右子节点: {inverted1.right.val}")
    print(f"期望: 根=4, 左=7, 右=2")
    
    # 测试用例2: 简单二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 简单二叉树 [2,1,3]")
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    inverted2 = solution.invertTree(root2)
    print(f"翻转后根节点: {inverted2.val}")
    print(f"翻转后左子节点: {inverted2.left.val}")
    print(f"翻转后右子节点: {inverted2.right.val}")
    print(f"期望: 根=2, 左=3, 右=1")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = None
    inverted3 = solution.invertTree(root3)
    print(f"翻转后: {inverted3}")
    print(f"期望结果: None")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = TreeNode(1)
    inverted4 = solution.invertTree(root4)
    print(f"翻转后根节点: {inverted4.val}")
    print(f"期望结果: 1")
