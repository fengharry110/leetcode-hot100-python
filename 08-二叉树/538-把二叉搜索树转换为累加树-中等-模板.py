"""
538. 把二叉搜索树转换为累加树
https://leetcode.cn/problems/convert-bst-to-greater-tree/description/

给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

示例 1：
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
输入：root = [0,null,1]
输出：[1,null,1]

提示：
树中的节点数在 [1, 100] 范围内。
0 <= Node.val <= 100
树中的所有值都 互不相同 。
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
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        把二叉搜索树转换为累加树
        
        参数:
            root: 二叉搜索树根节点
            
        返回:
            转换后的累加树根节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
    root1 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    root1.left.right.right = TreeNode(3)
    root1.right.right.right = TreeNode(8)
    result1 = solution.convertBST(root1)
    print(f"根节点值: {result1.val if result1 else None}")
    print(f"期望根节点值: 30")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,null,1]")
    root2 = TreeNode(0)
    root2.right = TreeNode(1)
    result2 = solution.convertBST(root2)
    print(f"根节点值: {result2.val if result2 else None}")
    print(f"期望根节点值: 1")
