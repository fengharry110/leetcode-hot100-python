"""
142. 环形链表II
https://leetcode.cn/problems/linked-list-cycle-ii/description/

给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
不允许修改链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点

示例 3：
输入：head = [1], pos = -1
输出：返回 null

提示：
- 链表中节点的数目范围在 [0, 10^4] 内
- -10^5 <= Node.val <= 10^5
- pos 为 -1 或者链表中的一个有效索引
"""

from typing import Optional


class ListNode:
    """链表节点类"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    请在此处实现你的解法
    """
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        找出环形链表的入环点
        
        参数:
            head: 链表头节点
            
        返回:
            入环点节点，如果无环返回None
        """
        # TODO: 在此实现你的解法
        pass


def build_linked_list_with_cycle(values, pos):
    """根据列表和环的位置构建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]
    
    return head


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [3,2,0,-4], pos=1")
    head1 = build_linked_list_with_cycle([3, 2, 0, -4], 1)
    solution = Solution()
    result1 = solution.detectCycle(head1)
    print(f"入环点值: {result1.val if result1 else None}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2], pos=0")
    head2 = build_linked_list_with_cycle([1, 2], 0)
    result2 = solution.detectCycle(head2)
    print(f"入环点值: {result2.val if result2 else None}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1], pos=-1")
    head3 = build_linked_list_with_cycle([1], -1)
    result3 = solution.detectCycle(head3)
    print(f"入环点: {result3}")
    print(f"期望结果: None")
