"""
2. 两数相加
https://leetcode.cn/problems/add-two-numbers/description/

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
- 每个链表中的节点数在范围 [1, 100] 内
- 0 <= Node.val <= 9
- 题目数据保证列表表示的数字不含前导零
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
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        两数相加
        
        参数:
            l1: 第一个链表
            l2: 第二个链表
            
        返回:
            结果链表
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
    print("测试用例1: l1 = [2,4,3], l2 = [5,6,4]")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print(f"结果: {linked_list_to_list(result)}")
    print(f"期望结果: [7, 0, 8]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: l1 = [0], l2 = [0]")
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result2 = solution.addTwoNumbers(l1, l2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: [0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result3 = solution.addTwoNumbers(l1, l2)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [8, 9, 9, 9, 0, 0, 0, 1]")
