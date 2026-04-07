"""
617. 合并二叉树
https://leetcode.cn/problems/merge-two-binary-trees/description/

给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。

示例 1：
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]

示例 2：
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
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
    合并二叉树解法类
    
    解题思路：
        递归合并两个二叉树
        
    算法步骤：
        1. 如果root1为空，返回root2
        2. 如果root2为空，返回root1
        3. 将root1和root2的值相加
        4. 递归合并左子树
        5. 递归合并右子树
        6. 返回root1
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        合并两个二叉树
        
        参数:
            root1: 第一棵二叉树的根节点
            root2: 第二棵二叉树的根节点
            
        返回:
            合并后的二叉树
        """
        if not root1:
            return root2
        if not root2:
            return root1
        
        # 合并当前节点
        root1.val += root2.val
        
        # 递归合并左子树
        root1.left = self.mergeTrees(root1.left, root2.left)
        
        # 递归合并右子树
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]")
    # 构建root1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    
    # 构建root2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)
    
    solution = Solution()
    merged_root = solution.mergeTrees(root1, root2)
    
    # 验证结果
    print("合并后的二叉树结构:")
    print(f"根节点: {merged_root.val}")
    print(f"左子节点: {merged_root.left.val}")
    print(f"右子节点: {merged_root.right.val}")
    print(f"左左子节点: {merged_root.left.left.val}")
    print(f"左右子节点: {merged_root.left.right.val}")
    print(f"右右子节点: {merged_root.right.right.val}")
    print(f"期望结果: [3,4,5,5,4,null,7]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: root1 = [1], root2 = [1,2]")
    # 构建root1
    root1_2 = TreeNode(1)
    
    # 构建root2
    root2_2 = TreeNode(1)
    root2_2.left = TreeNode(2)
    
    solution2 = Solution()
    merged_root_2 = solution2.mergeTrees(root1_2, root2_2)
    
    # 验证结果
    print("合并后的二叉树结构:")
    print(f"根节点: {merged_root_2.val}")
    print(f"左子节点: {merged_root_2.left.val}")
    print(f"期望结果: [2,2]")
