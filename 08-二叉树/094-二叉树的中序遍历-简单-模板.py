"""
94. 二叉树的中序遍历
https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        二叉树的中序遍历
        
        参数:
            root: 二叉树根节点
            
        返回:
            中序遍历结果列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：构建二叉树 [1, null, 2, 3]
    print("=" * 50)
    print("测试用例1: [1, null, 2, 3]")
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(f"结果: {solution.inorderTraversal(root1)}")
    print(f"期望结果: [1, 3, 2]")
    
    # 测试用例2：空树
    print("\n" + "=" * 50)
    print("测试用例2: 空树")
    root2 = None
    print(f"结果: {solution.inorderTraversal(root2)}")
    print(f"期望结果: []")
    
    # 测试用例3：只有根节点的树
    print("\n" + "=" * 50)
    print("测试用例3: [1]")
    root3 = TreeNode(1)
    print(f"结果: {solution.inorderTraversal(root3)}")
    print(f"期望结果: [1]")
    
    # 测试用例4：构建二叉树 [1, 2, 3, 4, 5, 6, 7]
    print("\n" + "=" * 50)
    print("测试用例4: [1, 2, 3, 4, 5, 6, 7]")
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    print(f"结果: {solution.inorderTraversal(root4)}")
    print(f"期望结果: [4, 2, 5, 1, 6, 3, 7]")
