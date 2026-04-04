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
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        O(1)空间复杂度解法（寻找前驱节点）：
        - 对于当前节点，如果左子树不为空
        - 找到左子树的最右节点（前驱）
        - 将右子树接到前驱的右边
        - 将左子树移到右边
        - 左子树置空
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # 将当前节点的右子树接到前驱的右边
                predecessor.right = curr.right
                
                # 将左子树移到右边
                curr.right = curr.left
                curr.left = None
            
            # 移动到下一个节点
            curr = curr.right


class SolutionRecursive:
    def __init__(self):
        self.prev = None
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        递归解法（后序遍历）：
        - 先递归展开右子树，再展开左子树
        - 将当前节点的右指针指向前一个处理的节点
        - 左指针置空
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        if not root:
            return
        
        # 先递归处理右子树和左子树
        self.flatten(root.right)
        self.flatten(root.left)
        
        # 将当前节点的右指针指向前一个节点
        root.right = self.prev
        root.left = None
        
        # 更新prev
        self.prev = root
