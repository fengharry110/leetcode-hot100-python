"""
404. 左叶子之和
https://leetcode.cn/problems/sum-of-left-leaves/description/

给定二叉树的根节点 root ，返回所有左叶子之和。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：24
解释：在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

示例 2：
输入：root = [1]
输出：0
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
    左叶子之和解法类
    
    解题思路：
        递归遍历二叉树，判断是否是左叶子节点
        
    算法步骤：
        1. 递归遍历二叉树
        2. 对于每个节点，检查其左子节点是否是叶子节点
        3. 如果是，将值加到总和中
        4. 递归处理左右子树
        5. 返回总和
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        计算左叶子之和
        
        参数:
            root: 二叉树的根节点
            
        返回:
            左叶子之和
        """
        if not root:
            return 0
        
        sum_left = 0
        
        # 检查左子节点是否是叶子节点
        if root.left and not root.left.left and not root.left.right:
            sum_left += root.left.val
        
        # 递归处理左右子树
        sum_left += self.sumOfLeftLeaves(root.left)
        sum_left += self.sumOfLeftLeaves(root.right)
        
        return sum_left


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
    result1 = solution.sumOfLeftLeaves(root1)
    print(f"结果: {result1}")
    print(f"期望结果: 24")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: root = [1]")
    root2 = TreeNode(1)
    solution2 = Solution()
    result2 = solution2.sumOfLeftLeaves(root2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: root = [1,2,3,4,5]")
    # 构建二叉树
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    
    solution3 = Solution()
    result3 = solution3.sumOfLeftLeaves(root3)
    print(f"结果: {result3}")
    print(f"期望结果: 4")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: root = []")
    root4 = None
    solution4 = Solution()
    result4 = solution4.sumOfLeftLeaves(root4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
