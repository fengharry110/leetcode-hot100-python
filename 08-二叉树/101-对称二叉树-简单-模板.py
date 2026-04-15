"""
101. 对称二叉树
https://leetcode.cn/problems/symmetric-tree/description/

给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        判断二叉树是否对称
        
        参数:
            root: 二叉树根节点
            
        返回:
            是否轴对称
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: 对称二叉树
    print("=" * 50)
    print("测试用例1: 对称二叉树 [1,2,2,3,4,4,3]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    solution = Solution()
    result1 = solution.isSymmetric(root1)
    print(f"是否对称: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2: 非对称二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 非对称二叉树 [1,2,2,null,3,null,3]")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    result2 = solution.isSymmetric(root2)
    print(f"是否对称: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = None
    result3 = solution.isSymmetric(root3)
    print(f"是否对称: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = TreeNode(1)
    result4 = solution.isSymmetric(root4)
    print(f"是否对称: {result4}")
    print(f"期望结果: True")
