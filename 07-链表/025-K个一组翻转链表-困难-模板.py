"""
25. K个一组翻转链表
https://leetcode.cn/problems/reverse-nodes-in-k-group/description/

给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

提示：
- 链表节点数目为 n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
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
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        K个一组翻转链表
        
        参数:
            head: 链表头节点
            k: 每组节点数
            
        返回:
            翻转后的链表头节点
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


def linked_list_to_list(head):
    """将链表转换为列表"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: head = [1,2,3,4,5], k = 2")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result1 = solution.reverseKGroup(head1, 2)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [2, 1, 4, 3, 5]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = [1,2,3,4,5], k = 3")
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = solution.reverseKGroup(head2, 3)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: [3, 2, 1, 4, 5]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = [1,2], k = 2")
    head3 = create_linked_list([1, 2])
    result3 = solution.reverseKGroup(head3, 2)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [2, 1]")
