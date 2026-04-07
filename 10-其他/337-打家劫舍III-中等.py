"""
337. 打家劫舍 III
https://leetcode.cn/problems/house-robber-iii/description/

小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个 "父" 房子与之相连。一番侦察之后，聪明的小偷意识到 "这个地方的所有房屋的排列类似于一棵二叉树"。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
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
    打家劫舍III解法类
    
    解题思路：
        后序遍历，返回每个节点的两种状态：偷或不偷
        
    算法步骤：
        1. 定义辅助函数，返回一个元组 (偷当前节点的最大金额, 不偷当前节点的最大金额)
        2. 递归处理左右子树
        3. 计算偷当前节点的最大金额：当前节点值 + 左子树不偷的金额 + 右子树不偷的金额
        4. 计算不偷当前节点的最大金额：max(左子树偷或不偷的最大值) + max(右子树偷或不偷的最大值)
        5. 返回两种状态的最大值
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        计算最大盗窃金额
        
        参数:
            root: 二叉树的根节点
            
        返回:
            最大盗窃金额
        """
        def dfs(node):
            """
            后序遍历，返回偷或不偷当前节点的最大金额
            
            参数:
                node: 当前节点
                
            返回:
                (偷当前节点的金额, 不偷当前节点的金额)
            """
            if not node:
                return (0, 0)
            
            # 递归处理左右子树
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            
            # 偷当前节点
            rob_current = node.val + left_not_rob + right_not_rob
            
            # 不偷当前节点
            not_rob_current = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            
            return (rob_current, not_rob_current)
        
        return max(dfs(root))


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: root = [3,2,3,null,3,null,1]")
    # 构建二叉树
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(1)
    
    solution = Solution()
    result1 = solution.rob(root1)
    print(f"结果: {result1}")
    print(f"期望结果: 7")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: root = [3,4,5,1,3,null,1]")
    # 构建二叉树
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(1)
    
    solution2 = Solution()
    result2 = solution2.rob(root2)
    print(f"结果: {result2}")
    print(f"期望结果: 9")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: root = [1]")
    root3 = TreeNode(1)
    solution3 = Solution()
    result3 = solution3.rob(root3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: root = [2,1,3,null,4]")
    # 构建二叉树
    root4 = TreeNode(2)
    root4.left = TreeNode(1)
    root4.right = TreeNode(3)
    root4.left.right = TreeNode(4)
    
    solution4 = Solution()
    result4 = solution4.rob(root4)
    print(f"结果: {result4}")
    print(f"期望结果: 7")
