# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        """
        二叉树的中序遍历
        方法1：递归
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(n)，递归栈的深度
        """
        result = []
        
        def inorder(node):
            if not node:
                return
            # 中序遍历：左 -> 根 -> 右
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
    
    def inorderTraversalIterative(self, root):
        """
        二叉树的中序遍历
        方法2：迭代
        时间复杂度：O(n)，其中n是二叉树的节点数
        空间复杂度：O(n)，栈的空间
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # 遍历左子树，将所有左节点入栈
            while current:
                stack.append(current)
                current = current.left
            
            # 处理当前节点
            current = stack.pop()
            result.append(current.val)
            
            # 处理右子树
            current = current.right
        
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：构建二叉树 [1, null, 2, 3]
    #     1
    #      \n    #       2
    #      /
    #     3
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print("测试用例1:")
    print("递归方法:", solution.inorderTraversal(root1))
    print("迭代方法:", solution.inorderTraversalIterative(root1))
    print()
    
    # 测试用例2：空树
    root2 = None
    print("测试用例2:")
    print("递归方法:", solution.inorderTraversal(root2))
    print("迭代方法:", solution.inorderTraversalIterative(root2))
    print()
    
    # 测试用例3：只有根节点的树
    root3 = TreeNode(1)
    print("测试用例3:")
    print("递归方法:", solution.inorderTraversal(root3))
    print("迭代方法:", solution.inorderTraversalIterative(root3))
    print()
    
    # 测试用例4：构建二叉树 [1, 2, 3, 4, 5, 6, 7]
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    print("测试用例4:")
    print("递归方法:", solution.inorderTraversal(root4))
    print("迭代方法:", solution.inorderTraversalIterative(root4))