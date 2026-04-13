"""
234. 回文链表
https://leetcode.cn/problems/palindrome-linked-list/description/

给你一个单链表的头节点 head，请你判断该链表是否为回文链表。如果是，返回 true；否则，返回 false。

示例 1：
输入：head = [1,2,2,1]
输出：true

示例 2：
输入：head = [1,2]
输出：false

提示：
- 链表中节点数目在 [1, 10^5] 内
- 0 <= Node.val <= 9

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否为回文链表
        
        参数:
            head: 链表头节点
            
        返回:
            是否为回文链表
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
    print("测试用例1: head = [1,2,2,1]")
    head1 = create_linked_list([1, 2, 2, 1])
    solution = Solution()
    result1 = solution.isPalindrome(head1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = [1,2]")
    head2 = create_linked_list([1, 2])
    result2 = solution.isPalindrome(head2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = [1,2,3,2,1]")
    head3 = create_linked_list([1, 2, 3, 2, 1])
    result3 = solution.isPalindrome(head3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
