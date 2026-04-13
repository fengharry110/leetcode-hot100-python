"""
148. 排序链表
中等
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围 [0, 5 * 10^4] 内
-10^5 <= Node.val <= 10^5

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序（自顶向下）
        if not head or not head.next:
            return head
        
        # 快慢指针找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 断开链表
        mid = slow.next
        slow.next = None
        
        # 递归排序
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并
        return self._merge(left, right)
    
    def _merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2
        return dummy.next


def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    head1 = list_to_linkedlist([4, 2, 1, 3])
    print("输入: head = [4,2,1,3]")
    result1 = solution.sortList(head1)
    print(f"输出: {linkedlist_to_list(result1)}")
    
    # 测试用例2
    head2 = list_to_linkedlist([-1, 5, 3, 4, 0])
    print("\n输入: head = [-1,5,3,4,0]")
    result2 = solution.sortList(head2)
    print(f"输出: {linkedlist_to_list(result2)}")
    
    # 测试用例3
    head3 = list_to_linkedlist([])
    print("\n输入: head = []")
    result3 = solution.sortList(head3)
    print(f"输出: {linkedlist_to_list(result3)}")
