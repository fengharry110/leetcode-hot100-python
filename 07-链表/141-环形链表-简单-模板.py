"""
141. 环形链表
https://leetcode.cn/problems/linked-list-cycle/description/

给你一个链表的头节点 head，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

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

提示：
- 链表中节点的数目范围是 [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos 为 -1 或链表中的一个有效索引
"""

from typing import Optional


class ListNode:
    """链表节点类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    请在此处实现你的解法
    """
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否有环
        
        参数:
            head: 链表头节点
            
        返回:
            是否有环
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
    result1 = solution.hasCycle(head1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2], pos=0")
    head2 = build_linked_list_with_cycle([1, 2], 0)
    result2 = solution.hasCycle(head2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1], pos=-1")
    head3 = build_linked_list_with_cycle([1], -1)
    result3 = solution.hasCycle(head3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
