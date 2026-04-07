"""
101. 对称二叉树
https://leetcode.cn/problems/symmetric-tree/description/

给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
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
        判断二叉树是否对称，等价于判断左右子树是否镜像对称
        两个树镜像对称的条件：
        1. 两个根节点的值相等
        2. 左树的左子树与右树的右子树对称
        3. 左树的右子树与右树的左子树对称
        
    算法步骤：
        1. 如果根节点为空，返回True
        2. 调用递归函数比较左右子树
        3. 递归比较两个节点是否镜像对称
        4. 返回比较结果
        
    时间复杂度：O(n)
    空间复杂度：O(h)
    """
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        递归判断二叉树是否对称
        
        参数:
            root: 二叉树根节点
            
        返回:
            是否轴对称
        """
        if not root:
            return True
        return self._isMirror(root.left, root.right)
    
    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        递归判断两个节点是否镜像对称
        
        参数:
            left: 左子节点
            right: 右子节点
            
        返回:
            是否镜像对称
        """
        # 递归终止条件1：两个都为空，对称
        if not left and not right:
            return True
        # 递归终止条件2：只有一个为空，不对称
        if not left or not right:
            return False
        # 值相等且子树对称
        return (left.val == right.val and 
                self._isMirror(left.left, right.right) and 
                self._isMirror(left.right, right.left))


class SolutionIterative:
    """
    迭代解法类（使用队列）
    
    解题思路：
        使用队列成对存储需要比较的节点，每次取出两个节点进行比较
        
    算法步骤：
        1. 如果根节点为空，返回True
        2. 将左右子节点成对加入队列
        3. 当队列不为空时：
           - 取出两个节点
           - 如果都为空，继续
           - 如果只有一个为空或值不相等，返回False
           - 将对应的子节点成对加入队列
        4. 返回True
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        迭代判断二叉树是否对称
        
        参数:
            root: 二叉树根节点
            
        返回:
            是否轴对称
        """
        if not root:
            return True
        
        queue = deque()
        queue.append((root.left, root.right))
        
        while queue:
            left, right = queue.popleft()
            
            # 都为空，继续
            if not left and not right:
                continue
            
            # 只有一个为空或值不相等，不对称
            if not left or not right or left.val != right.val:
                return False
            
            # 成对加入队列
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True


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
    # 测试用例1: 对称二叉树
    print("=" * 50)
    print("测试用例1: 对称二叉树 [1,2,2,3,4,4,3]")
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    solution = Solution()
    result1 = solution.isSymmetric(root1)
    print(f"是否对称: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2: 非对称二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 非对称二叉树 [1,2,2,null,3,null,3]")
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    solution2 = SolutionIterative()
    result2 = solution2.isSymmetric(root2)
    print(f"是否对称: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = build_tree([])
    solution3 = Solution()
    result3 = solution3.isSymmetric(root3)
    print(f"是否对称: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = build_tree([1])
    solution4 = Solution()
    result4 = solution4.isSymmetric(root4)
    print(f"是否对称: {result4}")
    print(f"期望结果: True")
