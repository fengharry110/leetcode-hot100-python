# 112. 路径总和
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
# 叶子节点 是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        """
        判断是否存在根节点到叶子节点的路径和等于目标和
        方法1：递归
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(h)，h是二叉树的高度，最坏情况下为O(n)
        """
        if not root:
            return False
        
        # 如果当前节点是叶子节点，判断剩余目标和是否等于当前节点值
        if not root.left and not root.right:
            return root.val == targetSum
        
        # 递归检查左子树和右子树
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
    def hasPathSumIterative(self, root, targetSum):
        """
        判断是否存在根节点到叶子节点的路径和等于目标和
        方法2：迭代（深度优先搜索）
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(n)，栈的空间
        """
        if not root:
            return False
        
        stack = [(root, targetSum)]
        
        while stack:
            node, current_sum = stack.pop()
            
            # 如果当前节点是叶子节点，判断剩余目标和是否等于当前节点值
            if not node.left and not node.right:
                if node.val == current_sum:
                    return True
            
            # 将右子节点入栈（因为栈是后进先出，所以先处理左子节点）
            if node.right:
                stack.append((node.right, current_sum - node.val))
            
            # 将左子节点入栈
            if node.left:
                stack.append((node.left, current_sum - node.val))
        
        return False


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：构建二叉树 [5,4,8,11,null,13,4,7,2,null,null,null,1]
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /       \
    # 7    2      1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(1)
    print("测试用例1:")
    print("递归方法:", solution.hasPathSum(root1, 22))
    print("迭代方法:", solution.hasPathSumIterative(root1, 22))
    print()
    
    # 测试用例2：构建二叉树 [1,2,3]
    #     1
    #    / \
    #   2   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print("测试用例2:")
    print("递归方法:", solution.hasPathSum(root2, 5))
    print("迭代方法:", solution.hasPathSumIterative(root2, 5))
    print()
    
    # 测试用例3：空树
    root3 = None
    print("测试用例3:")
    print("递归方法:", solution.hasPathSum(root3, 0))
    print("迭代方法:", solution.hasPathSumIterative(root3, 0))
    print()
    
    # 测试用例4：只有根节点的树
    root4 = TreeNode(1)
    print("测试用例4:")
    print("递归方法:", solution.hasPathSum(root4, 1))
    print("迭代方法:", solution.hasPathSumIterative(root4, 1))
    print()
    
    # 测试用例5：构建二叉树 [1,2]
    #     1
    #    /
    #   2
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    print("测试用例5:")
    print("递归方法:", solution.hasPathSum(root5, 1))
    print("迭代方法:", solution.hasPathSumIterative(root5, 1))