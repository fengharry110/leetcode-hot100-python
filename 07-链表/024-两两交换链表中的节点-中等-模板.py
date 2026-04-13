"""
24. 两两交换链表中的节点
https://leetcode.cn/problems/swap-nodes-in-pairs/description/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：
- 链表中节点的数目在范围 [0, 100] 内
- 0 <= Node.val <= 100
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
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        两两交换链表中的节点
        
        参数:
            head: 链表头节点
            
        返回:
            交换后的链表头节点
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
    print("测试用例1: head = [1,2,3,4]")
    head1 = create_linked_list([1, 2, 3, 4])
    solution = Solution()
    result1 = solution.swapPairs(head1)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [2, 1, 4, 3]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = []")
    head2 = create_linked_list([])
    result2 = solution.swapPairs(head2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = [1]")
    head3 = create_linked_list([1])
    result3 = solution.swapPairs(head3)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: [1]")
