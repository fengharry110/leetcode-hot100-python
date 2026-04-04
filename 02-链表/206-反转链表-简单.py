"""
206. 反转链表
https://leetcode.cn/problems/reverse-linked-list/description/

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
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
        使用三个指针：prev（前一个节点）、current（当前节点）、next（下一个节点）
        遍历链表，将当前节点的next指向前一个节点
        
    算法步骤：
        1. 初始化prev为None，current为head
        2. 遍历链表：
           - 保存current的下一个节点
           - 将current的next指向prev
           - prev移动到current
           - current移动到下一个节点
        3. 返回prev（新的头节点）
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
            # 保存下一个节点
            next_node = current.next
            # 反转当前节点的指向
            current.next = prev
            # 移动指针
            prev = current
            current = next_node
        
        return prev


class SolutionRecursive:
    """
    递归解法类
    
    解题思路：
        递归到链表末尾，然后逐层返回时反转指针
        
    算法步骤：
        1. 递归终止条件：空节点或只有一个节点
        2. 递归反转后续链表
        3. 将当前节点的下一个节点的next指向当前节点
        4. 将当前节点的next置空
        5. 返回新的头节点
        
    时间复杂度：O(n)
    空间复杂度：O(n)，递归栈深度
    """
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归反转链表
        
        参数:
            head: 链表头节点
            
        返回:
            反转后的链表头节点
        """
        # 递归终止条件
        if not head or not head.next:
            return head
        
        # 递归反转后续链表
        new_head = self.reverseList(head.next)
        
        # 反转当前节点与下一个节点的指针
        head.next.next = head
        head.next = None
        
        return new_head


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
    # 测试用例1: 正常链表
    print("=" * 50)
    print("测试用例1: 正常链表 [1,2,3,4,5]")
    head1 = build_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    reversed1 = solution.reverseList(head1)
    print(f"反转后: {linked_list_to_list(reversed1)}")
    print(f"期望结果: [5,4,3,2,1]")
    
    # 测试用例2: 两个节点
    print("\n" + "=" * 50)
    print("测试用例2: 两个节点 [1,2]")
    head2 = build_linked_list([1, 2])
    solution2 = SolutionRecursive()
    reversed2 = solution2.reverseList(head2)
    print(f"反转后: {linked_list_to_list(reversed2)}")
    print(f"期望结果: [2,1]")
    
    # 测试用例3: 空链表
    print("\n" + "=" * 50)
    print("测试用例3: 空链表 []")
    head3 = build_linked_list([])
    solution3 = Solution()
    reversed3 = solution3.reverseList(head3)
    print(f"反转后: {linked_list_to_list(reversed3)}")
    print(f"期望结果: []")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    head4 = build_linked_list([1])
    solution4 = Solution()
    reversed4 = solution4.reverseList(head4)
    print(f"反转后: {linked_list_to_list(reversed4)}")
    print(f"期望结果: [1]")
