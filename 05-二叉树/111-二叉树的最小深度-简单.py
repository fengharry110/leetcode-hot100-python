# 111. 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        """
        计算二叉树的最小深度
        方法1：递归
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(h)，h是二叉树的高度，最坏情况下为O(n)
        """
        if not root:
            return 0
        
        # 如果左子树为空，返回右子树的最小深度 + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # 如果右子树为空，返回左子树的最小深度 + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # 左右子树都不为空，返回左右子树最小深度的较小值 + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    def minDepthBFS(self, root):
        """
        计算二叉树的最小深度
        方法2：广度优先搜索（BFS）
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(n)，队列的空间
        """
        if not root:
            return 0
        
        from collections import deque
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # 如果当前节点是叶子节点，返回当前深度
                if not node.left and not node.right:
                    return depth
                
                # 将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                
                # 将右子节点加入队列
                if node.right:
                    queue.append(node.right)
        
        return depth


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：构建二叉树 [3, 9, 20, null, null, 15, 7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("测试用例1:")
    print("递归方法:", solution.minDepth(root1))
    print("BFS方法:", solution.minDepthBFS(root1))
    print()
    
    # 测试用例2：空树
    root2 = None
    print("测试用例2:")
    print("递归方法:", solution.minDepth(root2))
    print("BFS方法:", solution.minDepthBFS(root2))
    print()
    
    # 测试用例3：只有根节点的树
    root3 = TreeNode(1)
    print("测试用例3:")
    print("递归方法:", solution.minDepth(root3))
    print("BFS方法:", solution.minDepthBFS(root3))
    print()
    
    # 测试用例4：构建二叉树 [1, 2]
    #     1
    #    /
    #   2
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    print("测试用例4:")
    print("递归方法:", solution.minDepth(root4))
    print("BFS方法:", solution.minDepthBFS(root4))
    print()
    
    # 测试用例5：构建二叉树 [1, 2, 3, 4, 5]
    #       1
    #      / \
    #     2   3
    #    / 
    #   4   
    #  /
    # 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.left.left = TreeNode(4)
    root5.left.left.left = TreeNode(5)
    print("测试用例5:")
    print("递归方法:", solution.minDepth(root5))
    print("BFS方法:", solution.minDepthBFS(root5))