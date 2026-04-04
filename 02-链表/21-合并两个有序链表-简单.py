"""
21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/description/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
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
    迭代解法类
    
    解题思路：
        使用一个虚拟头节点简化操作，比较两个链表的当前节点，将较小的节点接到结果链表
        
    算法步骤：
        1. 创建一个虚拟头节点dummy
        2. 使用current指针指向dummy
        3. 同时遍历两个链表：
           - 比较当前节点的值
           - 将较小的节点接到current后面
           - 移动较小节点的指针和current指针
        4. 将剩余部分接到结果链表
        5. 返回dummy.next
        
    时间复杂度：O(m + n)
    空间复杂度：O(1)
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
        # 创建虚拟头节点
        dummy = ListNode(0)
        current = dummy
        
        # 同时遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 连接剩余部分
        current.next = list1 if list1 else list2
        
        return dummy.next


class SolutionRecursive:
    """
    递归解法类
    
    解题思路：
        递归比较两个链表的当前节点，将较小节点的next指向合并后的剩余部分
        
    算法步骤：
        1. 递归终止条件：任一链表为空
        2. 比较当前节点的值
        3. 较小节点的next指向递归合并的结果
        4. 返回较小节点
        
    时间复杂度：O(m + n)
    空间复杂度：O(m + n)，递归栈深度
    """
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归合并两个有序链表
        
        参数:
            list1: 第一个有序链表的头节点
            list2: 第二个有序链表的头节点
            
        返回:
            合并后的有序链表头节点
        """
        # 递归终止条件
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 比较当前节点值
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


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
    # 测试用例1: 正常合并
    print("=" * 50)
    print("测试用例1: 正常合并 [1,2,4] + [1,3,4]")
    list1_1 = build_linked_list([1, 2, 4])
    list2_1 = build_linked_list([1, 3, 4])
    solution = Solution()
    merged1 = solution.mergeTwoLists(list1_1, list2_1)
    print(f"合并后: {linked_list_to_list(merged1)}")
    print(f"期望结果: [1,1,2,3,4,4]")
    
    # 测试用例2: 都为空
    print("\n" + "=" * 50)
    print("测试用例2: 都为空 [] + []")
    list1_2 = build_linked_list([])
    list2_2 = build_linked_list([])
    solution2 = SolutionRecursive()
    merged2 = solution2.mergeTwoLists(list1_2, list2_2)
    print(f"合并后: {linked_list_to_list(merged2)}")
    print(f"期望结果: []")
    
    # 测试用例3: 一个为空
    print("\n" + "=" * 50)
    print("测试用例3: 一个为空 [] + [0]")
    list1_3 = build_linked_list([])
    list2_3 = build_linked_list([0])
    solution3 = Solution()
    merged3 = solution3.mergeTwoLists(list1_3, list2_3)
    print(f"合并后: {linked_list_to_list(merged3)}")
    print(f"期望结果: [0]")
    
    # 测试用例4: 无重叠
    print("\n" + "=" * 50)
    print("测试用例4: 无重叠 [1,2,3] + [4,5,6]")
    list1_4 = build_linked_list([1, 2, 3])
    list2_4 = build_linked_list([4, 5, 6])
    solution4 = Solution()
    merged4 = solution4.mergeTwoLists(list1_4, list2_4)
    print(f"合并后: {linked_list_to_list(merged4)}")
    print(f"期望结果: [1,2,3,4,5,6]")
