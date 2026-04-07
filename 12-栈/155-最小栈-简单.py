"""
155. 最小栈
https://leetcode.cn/problems/min-stack/description/

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
- MinStack() 初始化堆栈对象。
- void push(int val) 将元素 val 推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

示例 1:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""

from typing import Optional


class MinStack:
    """
    最小栈实现类
    
    解题思路：
        使用两个栈，一个存储所有元素，一个存储当前最小值
        
    算法步骤：
        1. 初始化两个栈：data_stack存储所有元素，min_stack存储当前最小值
        2. push操作：将元素压入data_stack，将当前最小值压入min_stack
        3. pop操作：同时弹出两个栈的栈顶元素
        4. top操作：返回data_stack的栈顶元素
        5. getMin操作：返回min_stack的栈顶元素
        
    时间复杂度：O(1) 所有操作
    空间复杂度：O(n)
    """
    
    def __init__(self):
        """初始化最小栈"""
        # 存储所有元素
        self.data_stack = []
        # 存储当前最小值
        self.min_stack = []
    
    def push(self, val: int) -> None:
        """
        将元素推入堆栈
        
        参数:
            val: 要推入的元素
        """
        self.data_stack.append(val)
        # 计算当前最小值并推入min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)
    
    def pop(self) -> None:
        """删除堆栈顶部的元素"""
        if self.data_stack:
            self.data_stack.pop()
            self.min_stack.pop()
    
    def top(self) -> int:
        """
        获取堆栈顶部的元素
        
        返回:
            栈顶元素
        """
        if self.data_stack:
            return self.data_stack[-1]
        raise IndexError("Stack is empty")
    
    def getMin(self) -> int:
        """
        获取堆栈中的最小元素
        
        返回:
            最小元素
        """
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")


class MinStackOptimized:
    """
    空间优化的最小栈实现
    
    解题思路：
        只使用一个栈，存储元素和当前最小值的元组
        
    算法步骤：
        1. 初始化栈，每个元素是 (current_value, current_min)
        2. push操作：计算当前最小值，将元组压入栈
        3. pop操作：弹出栈顶元素
        4. top操作：返回栈顶元素的第一个值
        5. getMin操作：返回栈顶元素的第二个值
        
    时间复杂度：O(1) 所有操作
    空间复杂度：O(n)
    """
    
    def __init__(self):
        """初始化最小栈"""
        self.stack = []
    
    def push(self, val: int) -> None:
        """
        将元素推入堆栈
        
        参数:
            val: 要推入的元素
        """
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])
        self.stack.append((val, current_min))
    
    def pop(self) -> None:
        """删除堆栈顶部的元素"""
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        """
        获取堆栈顶部的元素
        
        返回:
            栈顶元素
        """
        if self.stack:
            return self.stack[-1][0]
        raise IndexError("Stack is empty")
    
    def getMin(self) -> int:
        """
        获取堆栈中的最小元素
        
        返回:
            最小元素
        """
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("Stack is empty")


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: 标准操作")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"getMin: {minStack.getMin()}")  # 应该返回 -3
    minStack.pop()
    print(f"top: {minStack.top()}")       # 应该返回 0
    print(f"getMin: {minStack.getMin()}")  # 应该返回 -2
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: 空间优化版本")
    minStack2 = MinStackOptimized()
    minStack2.push(-2)
    minStack2.push(0)
    minStack2.push(-3)
    print(f"getMin: {minStack2.getMin()}")  # 应该返回 -3
    minStack2.pop()
    print(f"top: {minStack2.top()}")       # 应该返回 0
    print(f"getMin: {minStack2.getMin()}")  # 应该返回 -2
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: 重复元素")
    minStack3 = MinStack()
    minStack3.push(5)
    minStack3.push(5)
    minStack3.push(3)
    minStack3.push(4)
    print(f"getMin: {minStack3.getMin()}")  # 应该返回 3
    minStack3.pop()
    print(f"getMin: {minStack3.getMin()}")  # 应该返回 3
    minStack3.pop()
    print(f"getMin: {minStack3.getMin()}")  # 应该返回 5
