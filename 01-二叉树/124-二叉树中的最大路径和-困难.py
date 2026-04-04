"""
124. 二叉树中的最大路径和
https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
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
        对于每个节点，计算经过该节点的最大路径和
        经过节点的路径 = 节点值 + 左子树贡献 + 右子树贡献
        返回给父节点的贡献 = 节点值 + max(左贡献, 右贡献, 0)
        
    算法步骤：
        1. 初始化最大路径和为负无穷
        2. 递归计算每个节点对父节点的最大贡献
        3. 计算经过当前节点的最大路径和，更新全局最大值
        4. 返回当前节点对父节点的贡献
        5. 返回全局最大路径和
        
    时间复杂度：O(n)
    空间复杂度：O(h)
    """
    
    def __init__(self):
        """初始化最大路径和为负无穷"""
        self.max_sum = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树中的最大路径和
        
        参数:
            root: 二叉树根节点
            
        返回:
            最大路径和
        """
        def maxGain(node: Optional[TreeNode]) -> int:
            """
            递归计算当前节点对父节点的最大贡献
            
            参数:
                node: 当前节点
                
            返回:
                当前节点对父节点的最大贡献
            """
            # 递归终止条件：空节点贡献为0
            if not node:
                return 0
            
            # 递归计算左右子树的最大贡献值
            # 负数贡献视为0（表示不从该子树走）
            left_gain = max(maxGain(node.left), 0)
            right_gain = max(maxGain(node.right), 0)
            
            # 以当前节点为根的最大路径和
            price_newpath = node.val + left_gain + right_gain
            
            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, price_newpath)
            
            # 返回当前节点对父节点的最大贡献（只能走一边）
            return node.val + max(left_gain, right_gain)
        
        maxGain(root)
        return self.max_sum


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
    # 测试用例1: 简单二叉树
    print("=" * 50)
    print("测试用例1: 简单二叉树 [1,2,3]")
    root1 = build_tree([1, 2, 3])
    solution = Solution()
    result1 = solution.maxPathSum(root1)
    print(f"最大路径和: {result1}")
    print(f"期望结果: 6")
    print("解释: 最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6")
    
    # 测试用例2: 包含负数
    print("\n" + "=" * 50)
    print("测试用例2: 包含负数 [-10,9,20,null,null,15,7]")
    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    solution2 = Solution()
    result2 = solution2.maxPathSum(root2)
    print(f"最大路径和: {result2}")
    print(f"期望结果: 42")
    print("解释: 最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42")
    
    # 测试用例3: 单节点
    print("\n" + "=" * 50)
    print("测试用例3: 单节点 [-3]")
    root3 = build_tree([-3])
    solution3 = Solution()
    result3 = solution3.maxPathSum(root3)
    print(f"最大路径和: {result3}")
    print(f"期望结果: -3")
    print("解释: 路径至少包含一个节点")
    
    # 测试用例4: 全负数
    print("\n" + "=" * 50)
    print("测试用例4: 全负数 [-1,-2,-3]")
    root4 = build_tree([-1, -2, -3])
    solution4 = Solution()
    result4 = solution4.maxPathSum(root4)
    print(f"最大路径和: {result4}")
    print(f"期望结果: -1")
    print("解释: 选择最大的单个节点")
    
    # 测试用例5: 有一个负数分支
    print("\n" + "=" * 50)
    print("测试用例5: 有一个负数分支 [5,4,8,11,null,13,4,7,2,null,null,null,1]")
    root5 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    solution5 = Solution()
    result5 = solution5.maxPathSum(root5)
    print(f"最大路径和: {result5}")
    print(f"期望结果: 48")
