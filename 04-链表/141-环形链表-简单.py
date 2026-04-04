"""
141. 环形链表
https://leetcode.cn/problems/linked-list-cycle/description/

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
"""

from typing import Optional


class ListNode:
    """
    链表节点类
    
    属性:
        val: 节点值
        next: 下一个节点
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    快慢指针解法类
    
    解题思路：
        使用快慢指针，快指针每次走两步，慢指针每次走一步
        如果有环，快指针会追上慢指针
        
    算法步骤：
        1. 初始化快指针和慢指针都指向头节点
        2. 快指针每次走两步，慢指针每次走一步
        3. 如果快指针到达链表末尾，说明没有环
        4. 如果快指针追上慢指针，说明有环
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否有环
        
        参数:
            head: 链表头节点
            
        返回:
            是否有环
        """
        if not head or not head.next:
            return False
        
        # 初始化快慢指针
        slow = head
        fast = head.next
        
        while slow != fast:
            # 快指针到达末尾，无环
            if not fast or not fast.next:
                return False
            # 慢指针走一步
            slow = slow.next
            # 快指针走两步
            fast = fast.next.next
        
        # 快慢指针相遇，有环
        return True


class SolutionHash:
    """
    哈希表解法类
    
    解题思路：
        使用哈希表存储已经访问过的节点
        如果再次遇到相同节点，说明有环
        
    算法步骤：
        1. 初始化哈希表
        2. 遍历链表：
           - 如果当前节点在哈希表中，返回True
           - 否则，将当前节点加入哈希表
        3. 遍历结束，返回False
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        使用哈希表判断链表是否有环
        
        参数:
            head: 链表头节点
            
        返回:
            是否有环
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        return False


def build_linked_list(values, pos):
    """
    根据列表和环的位置构建链表
    
    参数:
        values: 节点值列表
        pos: 环的位置（-1表示无环）
        
    返回:
        链表头节点
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    # 构建链表
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # 创建环
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]
    
    return head


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [3,2,0,-4], pos=1")
    head1 = build_linked_list([3, 2, 0, -4], 1)
    solution = Solution()
    result1 = solution.hasCycle(head1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2], pos=0")
    head2 = build_linked_list([1, 2], 0)
    solution2 = SolutionHash()
    result2 = solution2.hasCycle(head2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1], pos=-1")
    head3 = build_linked_list([1], -1)
    solution3 = Solution()
    result3 = solution3.hasCycle(head3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [], pos=-1")
    head4 = build_linked_list([], -1)
    solution4 = SolutionHash()
    result4 = solution4.hasCycle(head4)
    print(f"结果: {result4}")
    print(f"期望结果: False")
