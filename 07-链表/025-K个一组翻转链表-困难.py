# 25. K 个一组翻转链表
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
# 那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
# 提示：
# 链表节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            # 检查剩余是否有k个节点
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            
            # 记录下一组的头节点
            next_head = tail.next
            
            # 翻转当前组
            cur = head
            prev_node = None
            for i in range(k):
                next_node = cur.next
                cur.next = prev_node
                prev_node = cur
                cur = next_node
            
            # 连接翻转后的链表
            prev.next = tail
            head.next = next_head
            prev = head
            head = next_head
        
        return dummy.next


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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseKGroup(head1, 2)
    print(f"测试1结果: {linked_list_to_list(result1)}")  # 期望输出: [2, 1, 4, 3, 5]
    
    # 测试2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = solution.reverseKGroup(head2, 3)
    print(f"测试2结果: {linked_list_to_list(result2)}")  # 期望输出: [3, 2, 1, 4, 5]
