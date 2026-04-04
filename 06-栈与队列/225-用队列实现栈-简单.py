"""
225. 用队列实现栈
https://leetcode.cn/problems/implement-stack-using-queues/description/

请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：
- void push(int x) 将元素 x 压入栈顶。
- int pop() 移除并返回栈顶元素。
- int top() 返回栈顶元素。
- boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

注意：
- 你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
- 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

示例 1：
输入：
["MyStack","push","push","top","pop","empty"]
[[],[1],[2],[],[],[]]

输出：
[null,null,null,2,2,false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
"""

from typing import Optional
from collections import deque


class MyStack:
    """
    用两个队列实现栈
    
    解题思路：
        使用两个队列，主队列和辅助队列
        每次push时，将元素加入辅助队列，然后将主队列的元素全部倒入辅助队列，最后交换两个队列
        
    算法步骤：
        1. 初始化两个队列：queue1和queue2
        2. push操作：
           - 将元素加入queue2
           - 将queue1的所有元素倒入queue2
           - 交换queue1和queue2
        3. pop操作：直接从queue1弹出元素
        4. top操作：返回queue1的队首元素
        5. empty操作：检查queue1是否为空
        
    时间复杂度：
        - push: O(n)
        - pop: O(1)
        - top: O(1)
        - empty: O(1)
    空间复杂度：O(n)
    """
    
    def __init__(self):
        """初始化栈"""
        # 主队列
        self.queue1 = deque()
        # 辅助队列
        self.queue2 = deque()
    
    def push(self, x: int) -> None:
        """
        将元素压入栈顶
        
        参数:
            x: 要压入的元素
        """
        # 将元素加入辅助队列
        self.queue2.append(x)
        # 将主队列的所有元素倒入辅助队列
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # 交换两个队列
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def pop(self) -> int:
        """
        移除并返回栈顶元素
        
        返回:
            栈顶元素
        """
        return self.queue1.popleft()
    
    def top(self) -> int:
        """
        返回栈顶元素
        
        返回:
            栈顶元素
        """
        return self.queue1[0]
    
    def empty(self) -> bool:
        """
        检查栈是否为空
        
        返回:
            栈是否为空
        """
        return not self.queue1


class MyStackSingleQueue:
    """
    用单个队列实现栈
    
    解题思路：
        使用单个队列，每次push后将前面的元素重新入队
        
    算法步骤：
        1. 初始化一个队列
        2. push操作：
           - 将元素加入队列
           - 将队列中除最后一个元素外的所有元素重新入队
        3. pop操作：直接从队列弹出元素
        4. top操作：返回队列的队首元素
        5. empty操作：检查队列是否为空
        
    时间复杂度：
        - push: O(n)
        - pop: O(1)
        - top: O(1)
        - empty: O(1)
    空间复杂度：O(n)
    """
    
    def __init__(self):
        """初始化栈"""
        self.queue = deque()
    
    def push(self, x: int) -> None:
        """
        将元素压入栈顶
        
        参数:
            x: 要压入的元素
        """
        # 将元素加入队列
        self.queue.append(x)
        # 将队列中除最后一个元素外的所有元素重新入队
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self) -> int:
        """
        移除并返回栈顶元素
        
        返回:
            栈顶元素
        """
        return self.queue.popleft()
    
    def top(self) -> int:
        """
        返回栈顶元素
        
        返回:
            栈顶元素
        """
        return self.queue[0]
    
    def empty(self) -> bool:
        """
        检查栈是否为空
        
        返回:
            栈是否为空
        """
        return not self.queue


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: 标准操作")
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(f"top: {myStack.top()}")    # 应该返回 2
    print(f"pop: {myStack.pop()}")    # 应该返回 2
    print(f"empty: {myStack.empty()}")  # 应该返回 False
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: 单队列实现")
    myStack2 = MyStackSingleQueue()
    myStack2.push(3)
    myStack2.push(4)
    myStack2.push(5)
    print(f"top: {myStack2.top()}")    # 应该返回 5
    print(f"pop: {myStack2.pop()}")    # 应该返回 5
    print(f"top: {myStack2.top()}")    # 应该返回 4
    print(f"pop: {myStack2.pop()}")    # 应该返回 4
    print(f"empty: {myStack2.empty()}")  # 应该返回 False
    print(f"pop: {myStack2.pop()}")    # 应该返回 3
    print(f"empty: {myStack2.empty()}")  # 应该返回 True
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: 空栈操作")
    myStack3 = MyStack()
    print(f"empty: {myStack3.empty()}")  # 应该返回 True
    myStack3.push(6)
    print(f"empty: {myStack3.empty()}")  # 应该返回 False
    print(f"pop: {myStack3.pop()}")    # 应该返回 6
    print(f"empty: {myStack3.empty()}")  # 应该返回 True
