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
"""

from typing import List, Optional
import heapq


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
    合并K个升序链表解法类
    
    解题思路：
        使用最小堆，每次取出最小的节点
        
    算法步骤：
        1. 初始化最小堆
        2. 将所有链表的头节点加入堆中
        3. 取出堆顶节点，作为新链表的节点
        4. 如果该节点有下一个节点，将下一个节点加入堆中
        5. 重复步骤3-4，直到堆为空
        6. 返回合并后的链表头
        
    时间复杂度：O(n log k)
    空间复杂度：O(k)
    """
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合并K个升序链表
        
        参数:
            lists: 链表数组
            
        返回:
            合并后的链表
        """
        # 自定义比较函数
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        heap = []
        # 将所有链表的头节点加入堆中
        for head in lists:
            if head:
                heapq.heappush(heap, head)
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # 取出堆顶节点
            node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # 如果有下一个节点，加入堆中
            if node.next:
                heapq.heappush(heap, node.next)
        
        return dummy.next


class SolutionDivideConquer:
    """
    分治解法类
    
    解题思路：
        分治法，将链表数组分成两部分，分别合并后再合并
        
    算法步骤：
        1. 递归函数：合并从left到right的链表
        2. 如果left == right，返回该链表
        3. 计算中间位置mid
        4. 递归合并左半部分和右半部分
        5. 合并两个有序链表
        6. 返回合并后的链表
        
    时间复杂度：O(n log k)
    空间复杂度：O(log k)
    """
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合并K个升序链表（分治版本）
        
        参数:
            lists: 链表数组
            
        返回:
            合并后的链表
        """
        def merge_two_lists(l1, l2):
            """
            合并两个有序链表
            """
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2
            return dummy.next
        
        def merge(left, right):
            """
            递归合并链表数组
            """
            if left == right:
                return lists[left]
            if left > right:
                return None
            mid = (left + right) // 2
            l1 = merge(left, mid)
            l2 = merge(mid + 1, right)
            return merge_two_lists(l1, l2)
        
        return merge(0, len(lists) - 1)


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: lists = [[1,4,5],[1,3,4],[2,6]]")
    lists1 = [create_linked_list([1,4,5]), create_linked_list([1,3,4]), create_linked_list([2,6])]
    solution = Solution()
    result1 = solution.mergeKLists(lists1)
    print(f"结果: {linked_list_to_list(result1)}")
    print(f"期望结果: [1,1,2,3,4,4,5,6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: lists = []")
    lists2 = []
    solution2 = SolutionDivideConquer()
    result2 = solution2.mergeKLists(lists2)
    print(f"结果: {linked_list_to_list(result2)}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: lists = [[]]")
    lists3 = [create_linked_list([])]
    solution3 = Solution()
    result3 = solution3.mergeKLists(lists3)
    print(f"结果: {linked_list_to_list(result3)}")
    print(f"期望结果: []")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: lists = [[3], [1,2], [4,5,6]]")
    lists4 = [create_linked_list([3]), create_linked_list([1,2]), create_linked_list([4,5,6])]
    solution4 = SolutionDivideConquer()
    result4 = solution4.mergeKLists(lists4)
    print(f"结果: {linked_list_to_list(result4)}")
    print(f"期望结果: [1,2,3,4,5,6]")
