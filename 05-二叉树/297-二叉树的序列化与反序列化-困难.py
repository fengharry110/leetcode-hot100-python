"""
297. 二叉树的序列化与反序列化
https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例 1：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]
"""

from typing import Optional, List


class TreeNode:
    """
    二叉树节点类
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    根据列表构建二叉树
    
    参数:
        values: 列表
        
    返回:
        根节点
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """
    将二叉树转换为列表
    
    参数:
        root: 根节点
        
    返回:
        列表
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
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


class Codec:
    """
    二叉树序列化与反序列化类
    
    解题思路：
        使用前序遍历进行序列化和反序列化
        
    序列化算法步骤：
        1. 前序遍历二叉树
        2. 遇到None时记录为"null"
        3. 用逗号分隔节点值
        
    反序列化算法步骤：
        1. 将字符串按逗号分割为列表
        2. 前序遍历构建二叉树
        3. 遇到"null"时返回None
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        序列化二叉树
        
        参数:
            root: 二叉树根节点
            
        返回:
            序列化后的字符串
        """
        def dfs(node):
            """
            深度优先搜索序列化
            """
            if not node:
                return "null"
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        
        return dfs(root)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        反序列化二叉树
        
        参数:
            data: 序列化后的字符串
            
        返回:
            二叉树根节点
        """
        values = data.split(",")
        self.index = 0
        
        def dfs():
            """
            深度优先搜索反序列化
            """
            if self.index >= len(values) or values[self.index] == "null":
                self.index += 1
                return None
            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: root = [1,2,3,null,null,4,5]")
    root1 = build_tree([1,2,3,None,None,4,5])
    codec = Codec()
    serialized1 = codec.serialize(root1)
    print(f"序列化结果: {serialized1}")
    deserialized1 = codec.deserialize(serialized1)
    print(f"反序列化结果: {tree_to_list(deserialized1)}")
    print(f"期望结果: [1, 2, 3, 4, 5]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: root = []")
    root2 = build_tree([])
    codec2 = Codec()
    serialized2 = codec2.serialize(root2)
    print(f"序列化结果: {serialized2}")
    deserialized2 = codec2.deserialize(serialized2)
    print(f"反序列化结果: {tree_to_list(deserialized2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: root = [1]")
    root3 = build_tree([1])
    codec3 = Codec()
    serialized3 = codec3.serialize(root3)
    print(f"序列化结果: {serialized3}")
    deserialized3 = codec3.deserialize(serialized3)
    print(f"反序列化结果: {tree_to_list(deserialized3)}")
    print(f"期望结果: [1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: root = [1,2]")
    root4 = build_tree([1,2])
    codec4 = Codec()
    serialized4 = codec4.serialize(root4)
    print(f"序列化结果: {serialized4}")
    deserialized4 = codec4.deserialize(serialized4)
    print(f"反序列化结果: {tree_to_list(deserialized4)}")
    print(f"期望结果: [1, 2]")
