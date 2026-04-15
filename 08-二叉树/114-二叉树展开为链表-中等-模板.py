"""
114. 二叉树展开为链表
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/

给你二叉树的根结点 root ，请你将它展开为一个单链表：
- 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
- 展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]

提示：
树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        将二叉树展开为链表（原地修改）
        
        参数:
            root: 二叉树根节点
            
        返回:
            None（原地修改）
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,5,3,4,null,6]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    solution.flatten(root1)
    print("展开后（按right遍历）:")
    curr = root1
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.right
    print("None")
    print("期望结果: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: []")
    root2 = None
    solution.flatten(root2)
    print(f"结果: {root2}")
    print(f"期望结果: None")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0]")
    root3 = TreeNode(0)
    solution.flatten(root3)
    print(f"结果: {root3.val}")
    print(f"期望结果: 0")
