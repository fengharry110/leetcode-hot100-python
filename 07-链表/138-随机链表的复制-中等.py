# 138. 随机链表的复制
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random，
# 该指针可以指向链表中的任何节点或空节点。构造这个链表的深拷贝。
#
# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
# 提示：
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一步：在原节点后面插入复制节点
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        
        # 第二步：设置复制节点的random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 第三步：拆分链表
        dummy = Node(0)
        copy_cur = dummy
        cur = head
        while cur:
            copy_cur.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            copy_cur = copy_cur.next
        
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # 构建测试链表
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
    
    result = solution.copyRandomList(n1)
    # 打印结果
    cur = result
    while cur:
        random_val = cur.random.val if cur.random else None
        print(f"val: {cur.val}, random: {random_val}")
        cur = cur.next
