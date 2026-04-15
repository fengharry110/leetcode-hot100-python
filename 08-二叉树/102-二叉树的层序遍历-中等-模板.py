"""
102. 二叉树的层序遍历
https://leetcode.cn/problems/binary-tree-level-order-traversal/description/

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        二叉树的层序遍历
        
        参数:
            root: 二叉树根节点
            
        返回:
            层序遍历结果，每层节点值组成的列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [3,9,20,null,null,15,7]")
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    result1 = solution.levelOrder(root1)
    print(f"结果: {result1}")
    print(f"期望结果: [[3], [9, 20], [15, 7]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1]")
    root2 = TreeNode(1)
    result2 = solution.levelOrder(root2)
    print(f"结果: {result2}")
    print(f"期望结果: [[1]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: []")
    root3 = None
    result3 = solution.levelOrder(root3)
    print(f"结果: {result3}")
    print(f"期望结果: []")
