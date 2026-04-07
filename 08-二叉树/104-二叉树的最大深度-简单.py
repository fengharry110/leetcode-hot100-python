"""
104. 二叉树的最大深度
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2
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
        使用递归的思想，二叉树的最大深度等于左右子树最大深度的较大值加1
        
    算法步骤：
        1. 如果当前节点为空，返回深度0
        2. 递归计算左子树的最大深度
        3. 递归计算右子树的最大深度
        4. 返回左右子树深度的较大值加1
        
    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(h)，递归栈深度，h为树的高度
    """
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        递归计算二叉树的最大深度
        
        参数:
            root: 二叉树根节点
            
        返回:
            二叉树的最大深度
        """
        # 递归终止条件：空节点深度为0
        if not root:
            return 0
        
        # 递归计算左右子树的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 返回较大深度加1（当前节点）
        return 1 + max(left_depth, right_depth)


class SolutionBFS:
    """
    BFS层序遍历解法类
    
    解题思路：
        使用队列进行层序遍历，每遍历一层，深度加1
        
    算法步骤：
        1. 如果根节点为空，返回深度0
        2. 初始化队列，将根节点加入队列
        3. 初始化深度为0
        4. 当队列不为空时：
           - 深度加1
           - 处理当前层的所有节点
           - 将下一层的节点加入队列
        5. 返回深度
        
    时间复杂度：O(n)
    空间复杂度：O(w)，w为树的最大宽度
    """
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS计算二叉树的最大深度
        
        参数:
            root: 二叉树根节点
            
        返回:
            二叉树的最大深度
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            # 处理当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                
                # 将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


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
    print("测试用例1: 完整二叉树 [3,9,20,null,null,15,7]")
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    solution = Solution()
    depth1 = solution.maxDepth(root1)
    print(f"最大深度: {depth1}")
    print(f"期望结果: 3")
    
    # 测试用例2: 只有右子树的二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 只有右子树 [1,null,2]")
    root2 = build_tree([1, None, 2])
    solution2 = SolutionBFS()
    depth2 = solution2.maxDepth(root2)
    print(f"最大深度: {depth2}")
    print(f"期望结果: 2")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = build_tree([])
    solution3 = Solution()
    depth3 = solution3.maxDepth(root3)
    print(f"最大深度: {depth3}")
    print(f"期望结果: 0")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = build_tree([1])
    solution4 = Solution()
    depth4 = solution4.maxDepth(root4)
    print(f"最大深度: {depth4}")
    print(f"期望结果: 1")
    
    # 测试用例5: 链状树
    print("\n" + "=" * 50)
    print("测试用例5: 链状树 [1,2,null,3,null,4]")
    root5 = build_tree([1, 2, None, 3, None, 4])
    solution5 = Solution()
    depth5 = solution5.maxDepth(root5)
    print(f"最大深度: {depth5}")
    print(f"期望结果: 4")
