"""
160. 相交链表
https://leetcode.cn/problems/intersection-of-two-linked-lists/description/

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'

示例 2：
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
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
    双指针解法类
    
    解题思路：
        使用双指针法，让两个指针分别遍历两个链表
        当一个指针到达链表末尾时，将其重定位到另一个链表的头部
        这样两个指针走过的总长度相等，最终会同时到达相交节点
        
    算法步骤：
        1. 初始化两个指针pA和pB分别指向headA和headB
        2. 同时遍历两个链表
        3. 当pA到达末尾时，将其指向headB
        4. 当pB到达末尾时，将其指向headA
        5. 当pA == pB时，即为相交节点
        6. 返回相交节点或null
        
    时间复杂度：O(m + n)，m和n分别为两个链表的长度
    空间复杂度：O(1)
    """
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        找到两个链表的相交节点
        
        参数:
            headA: 链表A的头节点
            headB: 链表B的头节点
            
        返回:
            相交节点，如果不存在则返回None
        """
        # 如果任一链表为空，直接返回None
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # 双指针遍历
        while pA != pB:
            # pA到达末尾时，重定位到headB
            pA = pA.next if pA else headB
            # pB到达末尾时，重定位到headA
            pB = pB.next if pB else headA
        
        # pA和pB相等时，即为相交节点（或都为None）
        return pA


class SolutionHash:
    """
    哈希表解法类
    
    解题思路：
        使用哈希表存储链表A的所有节点，然后遍历链表B检查是否有节点在哈希表中
        
    算法步骤：
        1. 遍历链表A，将所有节点存入哈希表
        2. 遍历链表B，检查当前节点是否在哈希表中
        3. 如果在，返回该节点；如果遍历完都没找到，返回None
        
    时间复杂度：O(m + n)
    空间复杂度：O(m)
    """
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        使用哈希表找到相交节点
        
        参数:
            headA: 链表A的头节点
            headB: 链表B的头节点
            
        返回:
            相交节点，如果不存在则返回None
        """
        if not headA or not headB:
            return None
        
        # 存储链表A的所有节点
        nodes_in_A = set()
        current = headA
        while current:
            nodes_in_A.add(current)
            current = current.next
        
        # 遍历链表B，检查是否有节点在A中
        current = headB
        while current:
            if current in nodes_in_A:
                return current
            current = current.next
        
        return None


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


def create_intersection(listA_vals, listB_vals, skipA, skipB):
    """
    创建相交链表
    
    参数:
        listA_vals: 链表A的值列表
        listB_vals: 链表B的值列表
        skipA: 链表A中相交前的节点数
        skipB: 链表B中相交前的节点数
        
    返回:
        (headA, headB, intersect_node)
    """
    # 构建相交部分
    intersect_vals = listA_vals[skipA:]
    intersect_head = build_linked_list(intersect_vals)
    
    # 构建链表A的前半部分
    headA = build_linked_list(listA_vals[:skipA])
    if headA:
        current = headA
        while current.next:
            current = current.next
        current.next = intersect_head
    else:
        headA = intersect_head
    
    # 构建链表B的前半部分
    headB = build_linked_list(listB_vals[:skipB])
    if headB:
        current = headB
        while current.next:
            current = current.next
        current.next = intersect_head
    else:
        headB = intersect_head
    
    return headA, headB, intersect_head


if __name__ == "__main__":
    # 测试用例1: 有相交节点
    print("=" * 50)
    print("测试用例1: 有相交节点")
    headA1, headB1, intersect1 = create_intersection(
        [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3
    )
    solution = Solution()
    result1 = solution.getIntersectionNode(headA1, headB1)
    print(f"相交节点值: {result1.val if result1 else None}")
    print(f"期望结果: 8")
    
    # 测试用例2: 有相交节点（不同长度）
    print("\n" + "=" * 50)
    print("测试用例2: 有相交节点（不同长度）")
    headA2, headB2, intersect2 = create_intersection(
        [1, 9, 1, 2, 4], [3, 2, 4], 3, 1
    )
    solution2 = SolutionHash()
    result2 = solution2.getIntersectionNode(headA2, headB2)
    print(f"相交节点值: {result2.val if result2 else None}")
    print(f"期望结果: 2")
    
    # 测试用例3: 无相交节点
    print("\n" + "=" * 50)
    print("测试用例3: 无相交节点")
    headA3 = build_linked_list([2, 6, 4])
    headB3 = build_linked_list([1, 5])
    solution3 = Solution()
    result3 = solution3.getIntersectionNode(headA3, headB3)
    print(f"相交节点: {result3}")
    print(f"期望结果: None")
    
    # 测试用例4: 其中一个为空
    print("\n" + "=" * 50)
    print("测试用例4: 其中一个为空")
    headA4 = build_linked_list([1, 2, 3])
    headB4 = None
    solution4 = Solution()
    result4 = solution4.getIntersectionNode(headA4, headB4)
    print(f"相交节点: {result4}")
    print(f"期望结果: None")
