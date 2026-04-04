"""
199. 二叉树的右视图
https://leetcode.cn/problems/binary-tree-right-side-view/description/

给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]

示例 2：
输入：root = [1,null,3]
输出：[1,3]

示例 3：
输入：root = []
输出：[]
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS层序遍历解法：
        - 层序遍历，每层取最后一个节点
        时间复杂度：O(n)
        空间复杂度：O(w)，w为树的最大宽度
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # 当前层的最后一个节点
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result


class SolutionDFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS解法：
        - 优先遍历右子树，记录每个深度第一个访问的节点
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        result = []
        
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            
            # 当前深度的第一个节点（从右边看能看到的）
            if depth == len(result):
                result.append(node.val)
            
            # 先遍历右子树，再遍历左子树
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
