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
"""

from typing import Optional


class ListNode:
    """
    链表节点类
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    """
    根据列表创建链表
    
    参数:
        values: 列表
        
    返回:
        链表头节点
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """
    将链表转换为列表
    
    参数:
        head: 链表头节点
        
    返回:
        列表
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    """
    两数相加解法类
    
    解题思路：
        模拟加法过程，逐位相加，处理进位
        
    算法步骤：
        1. 创建虚拟头节点和当前节点
        2. 初始化进位为0
        3. 遍历两个链表，直到两个链表都为空且进位为0
        4. 计算当前位的和，包括进位
        5. 创建新节点存储当前位的结果
        6. 更新进位
        7. 移动指针
        8. 返回虚拟头节点的下一个节点
        
    时间复杂度：O(max(m, n))
    空间复杂度：O(max(m, n))
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
        # 创建虚拟头节点
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # 遍历两个链表
        while l1 or l2 or carry:
            # 获取当前位的值
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算当前位的和
            total = val1 + val2 + carry
            
            # 计算当前位的结果和进位
            current_val = total % 10
            carry = total // 10
            
            # 创建新节点
            current.next = ListNode(current_val)
            current = current.next
            
            # 移动指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


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
    solution2 = Solution()
    result2 = solution2.addTwoNumbers(l1, l2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: [0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    solution3 = Solution()
    result3 = solution3.addTwoNumbers(l1, l2)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [8, 9, 9, 9, 0, 0, 0, 1]")
