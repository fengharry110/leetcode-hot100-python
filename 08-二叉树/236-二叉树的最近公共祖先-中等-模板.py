"""
236. 二叉树的最近公共祖先
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为："对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。"

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
树中节点数目范围在 [2, 10^5] 内
-10^9 <= Node.val <= 10^9
所有 Node.val 互不相同
p != q
p 和 q 均存在于给定的二叉树中
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
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        找到二叉树中两个节点的最近公共祖先
        
        参数:
            root: 二叉树根节点
            p: 第一个目标节点
            q: 第二个目标节点
            
        返回:
            最近公共祖先节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 构建测试树
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: p = 5, q = 1")
    p1 = root.left  # 节点5
    q1 = root.right  # 节点1
    result1 = solution.lowestCommonAncestor(root, p1, q1)
    print(f"最近公共祖先: {result1.val}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: p = 5, q = 4")
    p2 = root.left  # 节点5
    q2 = root.left.right.right  # 节点4
    result2 = solution.lowestCommonAncestor(root, p2, q2)
    print(f"最近公共祖先: {result2.val}")
    print(f"期望结果: 5")
