"""
138. 随机链表的复制
https://leetcode.cn/problems/copy-list-with-random-pointer/description/

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random，
该指针可以指向链表中的任何节点或空节点。构造这个链表的深拷贝。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

提示：
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random 为 null 或指向链表中的节点
"""

from typing import Optional


class Node:
    """随机链表节点类"""
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    请在此处实现你的解法
    """
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        复制随机链表
        
        参数:
            head: 随机链表头节点
            
        返回:
            复制后的链表头节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    print("=" * 50)
    print("测试用例1: [[7,null],[13,0],[11,4],[10,2],[1,0]]")
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1
    
    solution = Solution()
    result = solution.copyRandomList(n1)
    cur = result
    while cur:
        random_val = cur.random.val if cur.random else None
        print(f"val: {cur.val}, random: {random_val}")
        cur = cur.next
