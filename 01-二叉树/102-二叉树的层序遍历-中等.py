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
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS层序遍历：
        - 使用队列，每次处理一层的所有节点
        - 将每层节点的值存入一个列表
        时间复杂度：O(n)
        空间复杂度：O(w)，w为树的最大宽度
        """
        if not root:
            return []
        
        from collections import deque
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_nodes)
        
        return result


class SolutionDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        DFS解法：
        - 使用深度优先搜索，记录每个节点的深度
        - 将节点值放入对应深度的列表中
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        result = []
        self._dfs(root, 0, result)
        return result
    
    def _dfs(self, root: Optional[TreeNode], depth: int, result: List[List[int]]):
        if not root:
            return
        
        # 如果当前深度还没有列表，创建一个
        if depth == len(result):
            result.append([])
        
        result[depth].append(root.val)
        
        self._dfs(root.left, depth + 1, result)
        self._dfs(root.right, depth + 1, result)
