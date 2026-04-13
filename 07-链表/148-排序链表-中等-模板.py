"""
148. 排序链表
https://leetcode.cn/problems/sort-list/description/

给你链表的头结点 head，请将其按升序排列并返回排序后的链表。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
- 链表中节点的数目在范围 [0, 5 * 10^4] 内
- -10^5 <= Node.val <= 10^5

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
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
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        排序链表
        
        参数:
            head: 链表头节点
            
        返回:
            排序后的链表头节点
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
    print("测试用例1: head = [4,2,1,3]")
    head1 = create_linked_list([4, 2, 1, 3])
    solution = Solution()
    result1 = solution.sortList(head1)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [1, 2, 3, 4]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: head = [-1,5,3,4,0]")
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    result2 = solution.sortList(head2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: [-1, 0, 3, 4, 5]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: head = []")
    head3 = create_linked_list([])
    result3 = solution.sortList(head3)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: []")
