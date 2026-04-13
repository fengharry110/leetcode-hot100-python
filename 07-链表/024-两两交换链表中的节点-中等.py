# 24. 两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
# 示例 1：
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#
# 示例 2：
# 输入：head = []
# 输出：[]
#
# 示例 3：
# 输入：head = [1]
# 输出：[1]
#
# 提示：
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # 要交换的两个节点
            first = head
            second = head.next
            
            # 交换
            prev.next = second
            first.next = second.next
            second.next = first
            
            # 移动指针
            prev = first
            head = first.next
        
        return dummy.next
    
    def swapPairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """递归版本"""
        if not head or not head.next:
            return head
        
        # 交换前两个节点
        first = head
        second = head.next
        
        first.next = self.swapPairs_recursive(second.next)
        second.next = first
        
        return second


if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for val in arr[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head
    
    def linked_list_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    solution = Solution()
    
    # 测试1
    head1 = create_linked_list([1, 2, 3, 4])
    result1 = solution.swapPairs(head1)
    print(f"测试1结果: {linked_list_to_list(result1)}")  # 期望输出: [2, 1, 4, 3]
    
    # 测试2
    head2 = create_linked_list([])
    result2 = solution.swapPairs(head2)
    print(f"测试2结果: {linked_list_to_list(result2)}")  # 期望输出: []
    
    # 测试3
    head3 = create_linked_list([1])
    result3 = solution.swapPairs(head3)
    print(f"测试3结果: {linked_list_to_list(result3)}")  # 期望输出: [1]
