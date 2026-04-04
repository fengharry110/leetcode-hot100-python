"""
232. 用栈实现队列
https://leetcode.cn/problems/implement-queue-using-stacks/description/

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：
- void push(int x) 将元素 x 推到队列的末尾
- int pop() 从队列的开头移除并返回元素
- int peek() 返回队列开头的元素
- boolean empty() 如果队列为空，返回 true ；否则，返回 false

说明：
- 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

示例 1：
输入：
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]

输出：
[null,null,null,1,1,false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2]
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""

from typing import Optional


class MyQueue:
    """
    用两个栈实现队列
    
    解题思路：
        使用两个栈，一个输入栈，一个输出栈
        输入栈用于push操作，输出栈用于pop和peek操作
        当输出栈为空时，将输入栈的元素全部倒入输出栈
        
    算法步骤：
        1. 初始化两个栈：in_stack和out_stack
        2. push操作：将元素压入in_stack
        3. pop操作：如果out_stack为空，将in_stack的元素倒入out_stack，然后弹出out_stack的栈顶
        4. peek操作：如果out_stack为空，将in_stack的元素倒入out_stack，然后返回out_stack的栈顶
        5. empty操作：检查in_stack和out_stack是否都为空
        
    时间复杂度：
        - push: O(1)
        - pop: 均摊O(1)
        - peek: 均摊O(1)
        - empty: O(1)
    空间复杂度：O(n)
    """
    
    def __init__(self):
        """初始化队列"""
        # 输入栈，用于push操作
        self.in_stack = []
        # 输出栈，用于pop和peek操作
        self.out_stack = []
    
    def push(self, x: int) -> None:
        """
        将元素推到队列的末尾
        
        参数:
            x: 要推入的元素
        """
        self.in_stack.append(x)
    
    def pop(self) -> int:
        """
        从队列的开头移除并返回元素
        
        返回:
            队列开头的元素
        """
        # 如果输出栈为空，将输入栈的元素倒入输出栈
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # 弹出输出栈的栈顶元素
        return self.out_stack.pop()
    
    def peek(self) -> int:
        """
        返回队列开头的元素
        
        返回:
            队列开头的元素
        """
        # 如果输出栈为空，将输入栈的元素倒入输出栈
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # 返回输出栈的栈顶元素
        return self.out_stack[-1]
    
    def empty(self) -> bool:
        """
        检查队列是否为空
        
        返回:
            队列是否为空
        """
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: 标准操作")
    myQueue = MyQueue()
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2]
    print(f"peek: {myQueue.peek()}")  # 应该返回 1
    print(f"pop: {myQueue.pop()}")    # 应该返回 1, queue is [2]
    print(f"empty: {myQueue.empty()}")  # 应该返回 False
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: 连续操作")
    myQueue2 = MyQueue()
    myQueue2.push(3)
    myQueue2.push(4)
    myQueue2.push(5)
    print(f"pop: {myQueue2.pop()}")    # 应该返回 3
    myQueue2.push(6)
    print(f"pop: {myQueue2.pop()}")    # 应该返回 4
    print(f"peek: {myQueue2.peek()}")  # 应该返回 5
    print(f"pop: {myQueue2.pop()}")    # 应该返回 5
    print(f"pop: {myQueue2.pop()}")    # 应该返回 6
    print(f"empty: {myQueue2.empty()}")  # 应该返回 True
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: 空队列操作")
    myQueue3 = MyQueue()
    print(f"empty: {myQueue3.empty()}")  # 应该返回 True
    myQueue3.push(7)
    print(f"empty: {myQueue3.empty()}")  # 应该返回 False
    print(f"pop: {myQueue3.pop()}")    # 应该返回 7
    print(f"empty: {myQueue3.empty()}")  # 应该返回 True
