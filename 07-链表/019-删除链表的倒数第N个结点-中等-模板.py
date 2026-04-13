"""
19. 删除链表的倒数第N个结点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

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
- 链表中结点的数目为 sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？
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
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        删除链表的倒数第n个结点
        
        参数:
            head: 链表头节点
            n: 倒数第n个
            
        返回:
            删除后的链表头节点
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
    print("测试用例1: head = [1,2,3,4,5], n = 2")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    result1 = solution.removeNthFromEnd(head1, 2)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [1, 2, 3, 5]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = [1], n = 1")
    head2 = create_linked_list([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = [1,2], n = 1")
    head3 = create_linked_list([1, 2])
    result3 = solution.removeNthFromEnd(head3, 1)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [1]")
