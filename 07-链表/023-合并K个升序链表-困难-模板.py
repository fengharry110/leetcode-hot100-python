"""
23. 合并K个升序链表
https://leetcode.cn/problems/merge-k-sorted-lists/description/

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] 按 升序 排列
- lists[i].length 的总和不超过 10^4
"""

from typing import List, Optional


class ListNode:
    """链表节点类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    请在此处实现你的解法
    """
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合并K个升序链表
        
        参数:
            lists: 链表数组
            
        返回:
            合并后的链表
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
    print("测试用例1: lists = [[1,4,5],[1,3,4],[2,6]]")
    lists1 = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
    solution = Solution()
    result1 = solution.mergeKLists(lists1)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [1, 1, 2, 3, 4, 4, 5, 6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: lists = []")
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: lists = [[]]")
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: []")
