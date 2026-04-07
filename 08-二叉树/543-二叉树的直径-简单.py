"""
543. 二叉树的直径
https://leetcode.cn/problems/diameter-of-binary-tree/description/

给你一棵二叉树的根节点 root ，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1
"""

from typing import Optional
from collections import deque


class TreeNode:
    """
    二叉树节点类
    
    属性:
        val: 节点值
        left: 左子节点
        right: 右子节点
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归解法类
    
    解题思路：
        直径 = 左子树最大深度 + 右子树最大深度
        在计算每个节点的深度时，更新全局最大直径
        注意：直径是边数，不是节点数
        
    算法步骤：
        1. 初始化直径为0
        2. 递归计算每个节点的深度
        3. 在计算深度时，更新直径（左深度 + 右深度）
        4. 返回直径
        
    时间复杂度：O(n)
    空间复杂度：O(h)
    """
    
    def __init__(self):
        """初始化直径为0"""
        self.diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树的直径
        
        参数:
            root: 二叉树根节点
            
        返回:
            二叉树的直径
        """
        self._depth(root)
        return self.diameter
    
    def _depth(self, root: Optional[TreeNode]) -> int:
        """
        递归计算以root为根的子树的最大深度
        
        参数:
            root: 子树根节点
            
        返回:
            子树的最大深度
        """
        # 递归终止条件：空节点深度为0
        if not root:
            return 0
        
        # 递归计算左右子树的深度
        left_depth = self._depth(root.left)
        right_depth = self._depth(root.right)
        
        # 更新直径：经过当前节点的最长路径 = 左深度 + 右深度
        self.diameter = max(self.diameter, left_depth + right_depth)
        
        # 返回当前节点的深度
        return 1 + max(left_depth, right_depth)


def build_tree(values):
    """
    根据列表构建二叉树（层序遍历顺序）
    
    参数:
        values: 节点值列表，None表示空节点
        
    返回:
        构建好的二叉树根节点
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # 左子节点
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # 右子节点
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


if __name__ == "__main__":
    # 测试用例1: 完整二叉树
    print("=" * 50)
    print("测试用例1: 完整二叉树 [1,2,3,4,5]")
    root1 = build_tree([1, 2, 3, 4, 5])
    solution = Solution()
    diameter1 = solution.diameterOfBinaryTree(root1)
    print(f"直径: {diameter1}")
    print(f"期望结果: 3")
    print("解释: 路径 [4,2,1,3] 或 [5,2,1,3] 的长度为3")
    
    # 测试用例2: 简单二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 简单二叉树 [1,2]")
    root2 = build_tree([1, 2])
    solution2 = Solution()
    diameter2 = solution2.diameterOfBinaryTree(root2)
    print(f"直径: {diameter2}")
    print(f"期望结果: 1")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = build_tree([])
    solution3 = Solution()
    diameter3 = solution3.diameterOfBinaryTree(root3)
    print(f"直径: {diameter3}")
    print(f"期望结果: 0")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = build_tree([1])
    solution4 = Solution()
    diameter4 = solution4.diameterOfBinaryTree(root4)
    print(f"直径: {diameter4}")
    print(f"期望结果: 0")
    
    # 测试用例5: 链状树
    print("\n" + "=" * 50)
    print("测试用例5: 链状树 [1,2,null,3,null,4]")
    root5 = build_tree([1, 2, None, 3, None, 4])
    solution5 = Solution()
    diameter5 = solution5.diameterOfBinaryTree(root5)
    print(f"直径: {diameter5}")
    print(f"期望结果: 3")
