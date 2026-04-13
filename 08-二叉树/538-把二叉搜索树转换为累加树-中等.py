"""
538. 把二叉搜索树转换为累加树
中等
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

示例 1：
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
输入：root = [0,null,1]
输出：[1,null,1]

提示：
树中的节点数在 [1, 100] 范围内。
0 <= Node.val <= 100
树中的所有值都 互不相同 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 反向中序遍历（右-根-左）
        self.total = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)
        
        dfs(root)
        return root


def list_to_tree(lst):
    """列表转二叉树"""
    if not lst:
        return None
    from collections import deque
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """二叉树转列表"""
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
    # 移除末尾的None
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    root1 = list_to_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    print("输入: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
    result1 = solution.convertBST(root1)
    print(f"输出: {tree_to_list(result1)}")
