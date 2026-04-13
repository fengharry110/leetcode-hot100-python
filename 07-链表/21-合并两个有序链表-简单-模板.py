"""
21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/description/

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
- 两个链表的节点数目范围是 [0, 50]
- -100 <= Node.val <= 100
- l1 和 l2 均按非递减顺序排列
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
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表
        
        参数:
            list1: 第一个有序链表的头节点
            list2: 第二个有序链表的头节点
            
        返回:
            合并后的有序链表头节点
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
    print("测试用例1: l1 = [1,2,4], l2 = [1,3,4]")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    solution = Solution()
    result1 = solution.mergeTwoLists(list1, list2)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [1, 1, 2, 3, 4, 4]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: l1 = [], l2 = []")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result2 = solution.mergeTwoLists(list1, list2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: l1 = [], l2 = [0]")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result3 = solution.mergeTwoLists(list1, list2)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [0]")
