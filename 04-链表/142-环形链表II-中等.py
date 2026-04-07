# 142. 环形链表 II
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        """
        找出环形链表的入环点
        方法：Floyd's Tortoise and Hare算法（快慢指针）
        时间复杂度：O(n)，其中n是链表的长度
        空间复杂度：O(1)，只使用常数级额外空间
        """
        # 步骤1：使用快慢指针判断链表是否有环
        slow = head
        fast = head
        
        # 快指针每次走两步，慢指针每次走一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # 如果快慢指针相遇，说明链表有环
            if slow == fast:
                break
        else:
            # 链表无环，返回None
            return None
        
        # 步骤2：找到入环点
        # 当快慢指针相遇后，将其中一个指针移到链表头部，然后两个指针以相同速度移动
        # 再次相遇的点就是入环点
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    
    def detectCycleHash(self, head):
        """
        找出环形链表的入环点
        方法：哈希表
        时间复杂度：O(n)，其中n是链表的长度
        空间复杂度：O(n)，哈希表的空间
        """
        seen = set()
        current = head
        
        while current:
            if current in seen:
                return current
            seen.add(current)
            current = current.next
        
        return None


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：有环链表
    # 构建链表：1 -> 2 -> 3 -> 4 -> 5 -> 3（环）
    head1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # 形成环，入环点是node3
    print("测试用例1:")
    print("有环链表，入环点值:", solution.detectCycle(head1).val)
    print("哈希表方法，入环点值:", solution.detectCycleHash(head1).val)
    print()
    
    # 测试用例2：无环链表
    # 构建链表：1 -> 2 -> 3 -> 4 -> 5
    head2 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head2.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print("测试用例2:")
    print("无环链表:", solution.detectCycle(head2))
    print("哈希表方法:", solution.detectCycleHash(head2))
    print()
    
    # 测试用例3：空链表
    head3 = None
    print("测试用例3:")
    print("空链表:", solution.detectCycle(head3))
    print("哈希表方法:", solution.detectCycleHash(head3))
    print()
    
    # 测试用例4：只有一个节点的链表（无环）
    head4 = ListNode(1)
    print("测试用例4:")
    print("只有一个节点的链表:", solution.detectCycle(head4))
    print("哈希表方法:", solution.detectCycleHash(head4))