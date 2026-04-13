"""
206. 反转链表
https://leetcode.cn/problems/reverse-linked-list/description/

给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]

提示：
- 链表中节点的数目范围是 [0, 5000]
- -5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
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
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表
        
        参数:
            head: 链表头节点
            
        返回:
            反转后的链表头节点
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
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: head = [1,2,3,4,5]")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result1 = solution.reverseList(head1)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [5, 4, 3, 2, 1]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = [1,2]")
    head2 = create_linked_list([1, 2])
    result2 = solution.reverseList(head2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: [2, 1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = []")
    head3 = create_linked_list([])
    result3 = solution.reverseList(head3)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: []")
