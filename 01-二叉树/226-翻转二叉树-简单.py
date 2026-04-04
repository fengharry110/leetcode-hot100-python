"""
226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/description/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]
"""

from typing import Optional


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
        使用递归的思想，先递归翻转左右子树，然后交换当前节点的左右子树
        
    算法步骤：
        1. 如果当前节点为空，返回None
        2. 递归翻转左子树
        3. 递归翻转右子树
        4. 交换当前节点的左右子树
        5. 返回当前节点
        
    时间复杂度：O(n)，每个节点访问一次
    空间复杂度：O(h)，递归栈深度，h为树的高度
    """
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归翻转二叉树
        
        参数:
            root: 二叉树根节点
            
        返回:
            翻转后的二叉树根节点
        """
        # 递归终止条件：空节点直接返回
        if not root:
            return None
        
        # 递归翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        # 交换左右子树
        root.left = right
        root.right = left
        
        return root


class SolutionIterative:
    """
    迭代解法类（使用栈）
    
    解题思路：
        使用栈模拟递归过程，每次弹出节点，交换其左右子树
        
    算法步骤：
        1. 如果根节点为空，返回None
        2. 将根节点压入栈
        3. 当栈不为空时：
           - 弹出节点
           - 交换该节点的左右子节点
           - 将非空的左右子节点压入栈
        4. 返回根节点
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        迭代翻转二叉树
        
        参数:
            root: 二叉树根节点
            
        返回:
            翻转后的二叉树根节点
        """
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            # 交换左右子节点
            node.left, node.right = node.right, node.left
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root


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
    
    from collections import deque
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


def tree_to_list(root):
    """
    将二叉树转换为列表（层序遍历）
    
    参数:
        root: 二叉树根节点
        
    返回:
        层序遍历的节点值列表
    """
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 去除末尾的None
    while result and result[-1] is None:
        result.pop()
    
    return result


if __name__ == "__main__":
    # 测试用例1: 完整二叉树
    print("=" * 50)
    print("测试用例1: 完整二叉树 [4,2,7,1,3,6,9]")
    root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    solution = Solution()
    inverted1 = solution.invertTree(root1)
    print(f"翻转后: {tree_to_list(inverted1)}")
    print(f"期望结果: [4,7,2,9,6,3,1]")
    
    # 测试用例2: 简单二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 简单二叉树 [2,1,3]")
    root2 = build_tree([2, 1, 3])
    solution2 = SolutionIterative()
    inverted2 = solution2.invertTree(root2)
    print(f"翻转后: {tree_to_list(inverted2)}")
    print(f"期望结果: [2,3,1]")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = build_tree([])
    solution3 = Solution()
    inverted3 = solution3.invertTree(root3)
    print(f"翻转后: {tree_to_list(inverted3)}")
    print(f"期望结果: []")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = build_tree([1])
    solution4 = Solution()
    inverted4 = solution4.invertTree(root4)
    print(f"翻转后: {tree_to_list(inverted4)}")
    print(f"期望结果: [1]")
