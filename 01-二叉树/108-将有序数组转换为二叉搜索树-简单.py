"""
108. 将有序数组转换为二叉搜索树
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树
"""

from typing import Optional, List
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
        选择中间元素作为根节点，确保左右子树节点数平衡
        左半部分构建左子树，右半部分构建右子树
        
    算法步骤：
        1. 如果数组为空，返回None
        2. 选择中间元素作为根节点
        3. 递归构建左子树（左半部分数组）
        4. 递归构建右子树（右半部分数组）
        5. 返回根节点
        
    时间复杂度：O(n)
    空间复杂度：O(log n)，递归栈深度
    """
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        将有序数组转换为高度平衡二叉搜索树
        
        参数:
            nums: 升序排列的整数数组
            
        返回:
            高度平衡二叉搜索树的根节点
        """
        if not nums:
            return None
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            """
            递归构建二叉搜索树
            
            参数:
                left: 数组左边界索引
                right: 数组右边界索引
                
            返回:
                子树的根节点
            """
            # 递归终止条件：左边界大于右边界
            if left > right:
                return None
            
            # 选择中间位置左边的元素作为根节点
            mid = (left + right) // 2
            
            # 创建根节点
            root = TreeNode(nums[mid])
            
            # 递归构建左右子树
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(nums) - 1)


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
    # 测试用例1: 奇数个元素
    print("=" * 50)
    print("测试用例1: 奇数个元素 [-10,-3,0,5,9]")
    nums1 = [-10, -3, 0, 5, 9]
    solution = Solution()
    root1 = solution.sortedArrayToBST(nums1)
    result1 = tree_to_list(root1)
    print(f"结果: {result1}")
    print(f"期望结果: [0,-3,9,-10,null,5] 或类似的高度平衡BST")
    
    # 测试用例2: 偶数个元素
    print("\n" + "=" * 50)
    print("测试用例2: 偶数个元素 [1,3]")
    nums2 = [1, 3]
    solution2 = Solution()
    root2 = solution2.sortedArrayToBST(nums2)
    result2 = tree_to_list(root2)
    print(f"结果: {result2}")
    print(f"期望结果: [3,1] 或 [1,null,3]")
    
    # 测试用例3: 空数组
    print("\n" + "=" * 50)
    print("测试用例3: 空数组 []")
    nums3 = []
    solution3 = Solution()
    root3 = solution3.sortedArrayToBST(nums3)
    result3 = tree_to_list(root3)
    print(f"结果: {result3}")
    print(f"期望结果: []")
    
    # 测试用例4: 单元素
    print("\n" + "=" * 50)
    print("测试用例4: 单元素 [0]")
    nums4 = [0]
    solution4 = Solution()
    root4 = solution4.sortedArrayToBST(nums4)
    result4 = tree_to_list(root4)
    print(f"结果: {result4}")
    print(f"期望结果: [0]")
    
    # 测试用例5: 多个元素
    print("\n" + "=" * 50)
    print("测试用例5: 多个元素 [1,2,3,4,5,6,7]")
    nums5 = [1, 2, 3, 4, 5, 6, 7]
    solution5 = Solution()
    root5 = solution5.sortedArrayToBST(nums5)
    result5 = tree_to_list(root5)
    print(f"结果: {result5}")
    print(f"期望结果: 高度平衡的BST，根节点为4")
