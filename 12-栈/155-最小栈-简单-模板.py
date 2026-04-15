"""
155. 最小栈
https://leetcode.cn/problems/min-stack/description/

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
- MinStack() 初始化堆栈对象。
- void push(int val) 将元素val推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

示例 1：
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

提示：
-2^31 <= val <= 2^31 - 1
pop、top 和 getMin 操作总是在 非空栈 上调用
push, pop, top, and getMin最多被调用 3 * 10^4 次
"""


class MinStack:
    """
    请在此处实现你的解法
    """
    
    def __init__(self):
        # TODO: 在此实现初始化
        pass

    def push(self, val: int) -> None:
        # TODO: 在此实现你的解法
        pass

    def pop(self) -> None:
        # TODO: 在此实现你的解法
        pass

    def top(self) -> int:
        # TODO: 在此实现你的解法
        pass

    def getMin(self) -> int:
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: 基本操作")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"getMin(): {minStack.getMin()}, 期望: -3")
    minStack.pop()
    print(f"top(): {minStack.top()}, 期望: 0")
    print(f"getMin(): {minStack.getMin()}, 期望: -2")
