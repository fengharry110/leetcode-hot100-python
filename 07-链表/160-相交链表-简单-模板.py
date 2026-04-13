"""
160. 相交链表
https://leetcode.cn/problems/intersection-of-two-linked-lists/description/

给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。
如果两个链表不存在相交节点，返回 null。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'

示例 2：
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null

提示：
- listA 中节点数目为 m
- listB 中节点数目为 n
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
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
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        找到两个链表的相交节点
        
        参数:
            headA: 链表A的头节点
            headB: 链表B的头节点
            
        返回:
            相交节点，如果不存在则返回None
        """
        # TODO: 在此实现你的解法
        pass


def create_linked_list(values):
    """根据列表创建链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def create_intersection(listA_vals, listB_vals, skipA, skipB):
    """创建相交链表"""
    # 构建相交部分
    intersect_vals = listA_vals[skipA:]
    intersect_head = create_linked_list(intersect_vals)
    
    # 构建链表A的前半部分
    headA = create_linked_list(listA_vals[:skipA])
    if headA:
        current = headA
        while current.next:
            current = current.next
        current.next = intersect_head
    else:
        headA = intersect_head
    
    # 构建链表B的前半部分
    headB = create_linked_list(listB_vals[:skipB])
    if headB:
        current = headB
        while current.next:
            current = current.next
        current.next = intersect_head
    else:
        headB = intersect_head
    
    return headA, headB, intersect_head


if __name__ == "__main__":
    # 测试用例1: 有相交节点
    print("=" * 50)
    print("测试用例1: 有相交节点")
    headA1, headB1, intersect1 = create_intersection([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3)
    solution = Solution()
    result1 = solution.getIntersectionNode(headA1, headB1)
    print(f"相交节点值: {result1.val if result1 else None}")
    print(f"期望结果: 8")
    
    # 测试用例2: 无相交节点
    print("\n" + "=" * 50)
    print("测试用例2: 无相交节点")
    headA2 = create_linked_list([2, 6, 4])
    headB2 = create_linked_list([1, 5])
    result2 = solution.getIntersectionNode(headA2, headB2)
    print(f"相交节点: {result2}")
    print(f"期望结果: None")
