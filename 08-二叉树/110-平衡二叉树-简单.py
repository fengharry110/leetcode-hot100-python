"""
110. 平衡二叉树
https://leetcode.cn/problems/balanced-binary-tree/description/

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true
"""

from typing import Optional


# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    平衡二叉树解法类
    
    解题思路：
        后序遍历，计算每个节点的高度，同时检查平衡
        
    算法步骤：
        1. 定义辅助函数，返回当前节点的高度，如果不平衡返回-1
        2. 递归计算左子树和右子树的高度
        3. 如果左右子树高度差超过1，返回-1
        4. 否则返回当前节点的高度
        5. 检查根节点的返回值是否为-1
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        判断二叉树是否平衡
        
        参数:
            root: 二叉树的根节点
            
        返回:
            是否平衡
        """
        def height(node):
            """
            计算节点的高度，如果不平衡返回-1
            
            参数:
                node: 当前节点
                
            返回:
                高度或-1
            """
            if not node:
                return 0
            
            left_height = height(node.left)
            if left_height == -1:
                return -1
            
            right_height = height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: root = [3,9,20,null,null,15,7]")
    # 构建二叉树
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    solution = Solution()
    result1 = solution.isBalanced(root1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: root = [1,2,2,3,3,null,null,4,4]")
    # 构建二叉树
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    
    solution2 = Solution()
    result2 = solution2.isBalanced(root2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: root = []")
    root3 = None
    solution3 = Solution()
    result3 = solution3.isBalanced(root3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: root = [1]")
    root4 = TreeNode(1)
    solution4 = Solution()
    result4 = solution4.isBalanced(root4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
