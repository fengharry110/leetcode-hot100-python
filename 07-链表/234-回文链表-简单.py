"""
234. 回文链表
https://leetcode.cn/problems/palindrome-linked-list/description/

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：
输入：head = [1,2,2,1]
输出：true

示例 2：
输入：head = [1,2]
输出：false
"""

from typing import Optional


class ListNode:
    """
    链表节点类
    
    属性:
        val: 节点值
        next: 下一个节点
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    快慢指针 + 反转链表解法类
    
    解题思路：
        1. 使用快慢指针找到链表的中点
        2. 反转后半部分链表
        3. 比较前半部分和反转后的后半部分
        
    算法步骤：
        1. 找到链表中点（快慢指针）
        2. 反转后半部分链表
        3. 比较前半部分和反转后的后半部分
        4. 恢复链表（可选）
        5. 返回比较结果
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        判断链表是否为回文链表
        
        参数:
            head: 链表头节点
            
        返回:
            是否为回文链表
        """
        if not head or not head.next:
            return True
        
        # 步骤1: 找到链表中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 步骤2: 反转后半部分链表
        second_half = self._reverseList(slow)
        # 保存反转后的头节点，用于恢复
        second_half_head = second_half
        
        # 步骤3: 比较前半部分和反转后的后半部分
        first_half = head
        is_palindrome = True
        while second_half:
            if first_half.val != second_half.val:
                is_palindrome = False
                break
            first_half = first_half.next
            second_half = second_half.next
        
        # 步骤4: 恢复链表（可选）
        self._reverseList(second_half_head)
        
        return is_palindrome
    
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表
        
        参数:
            head: 链表头节点
            
        返回:
            反转后的链表头节点
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


class SolutionList:
    """
    转换为列表解法类
    
    解题思路：
        将链表转换为列表，然后使用双指针判断是否回文
        
    算法步骤：
        1. 遍历链表，将值存入列表
        2. 使用双指针判断列表是否回文
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        将链表转换为列表判断是否回文
        
        参数:
            head: 链表头节点
            
        返回:
            是否为回文链表
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # 双指针判断
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True


def build_linked_list(values):
    """
    根据列表构建链表
    
    参数:
        values: 节点值列表
        
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
        节点值列表
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,2,1]")
    head1 = build_linked_list([1, 2, 2, 1])
    solution = Solution()
    result1 = solution.isPalindrome(head1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2]")
    head2 = build_linked_list([1, 2])
    solution2 = SolutionList()
    result2 = solution2.isPalindrome(head2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,2,3,2,1]")
    head3 = build_linked_list([1, 2, 3, 2, 1])
    solution3 = Solution()
    result3 = solution3.isPalindrome(head3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1]")
    head4 = build_linked_list([1])
    solution4 = SolutionList()
    result4 = solution4.isPalindrome(head4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
