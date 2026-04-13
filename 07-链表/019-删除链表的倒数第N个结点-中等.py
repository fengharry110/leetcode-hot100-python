"""
19. 删除链表的倒数第N个结点
中等
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 使用虚拟头节点，处理删除头节点的情况
        dummy = ListNode(0, head)
        
        # 快慢指针
        fast = dummy
        slow = dummy
        
        # 快指针先走n步
        for _ in range(n):
            fast = fast.next
        
        # 快慢指针同时移动，直到快指针到达末尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 删除倒数第n个节点
        slow.next = slow.next.next
        
        return dummy.next


def list_to_linkedlist(lst):
    """列表转链表"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """链表转列表"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    n1 = 2
    print(f"输入: head = [1,2,3,4,5], n = {n1}")
    result1 = solution.removeNthFromEnd(head1, n1)
    print(f"输出: {linkedlist_to_list(result1)}")
    
    # 测试用例2
    head2 = list_to_linkedlist([1])
    n2 = 1
    print(f"\n输入: head = [1], n = {n2}")
    result2 = solution.removeNthFromEnd(head2, n2)
    print(f"输出: {linkedlist_to_list(result2)}")
    
    # 测试用例3
    head3 = list_to_linkedlist([1, 2])
    n3 = 1
    print(f"\n输入: head = [1,2], n = {n3}")
    result3 = solution.removeNthFromEnd(head3, n3)
    print(f"输出: {linkedlist_to_list(result3)}")
