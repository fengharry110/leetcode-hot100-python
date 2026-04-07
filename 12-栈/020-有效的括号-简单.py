"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/description/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
"""

from typing import Optional


class Solution:
    """
    栈解法类
    
    解题思路：
        使用栈来匹配括号，遇到左括号入栈，遇到右括号出栈并检查是否匹配
        
    算法步骤：
        1. 初始化栈
        2. 遍历字符串：
           - 如果是左括号，入栈
           - 如果是右括号：
              * 栈为空，返回false
              * 栈顶元素与当前右括号不匹配，返回false
              * 否则，出栈
        3. 遍历结束后，栈为空则返回true，否则返回false
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def isValid(self, s: str) -> bool:
        """
        判断括号是否有效
        
        参数:
            s: 包含括号的字符串
            
        返回:
            是否有效
        """
        # 括号匹配字典
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            # 左括号入栈
            if char in bracket_map.values():
                stack.append(char)
            # 右括号出栈并检查
            elif char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            # 其他字符（如果有的话）
            else:
                return False
        
        # 栈为空则有效
        return len(stack) == 0


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"()\"")
    s1 = "()"
    solution = Solution()
    result1 = solution.isValid(s1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"()[]{}\"")
    s2 = "()[]{}"
    solution2 = Solution()
    result2 = solution2.isValid(s2)
    print(f"结果: {result2}")
    print(f"期望结果: True")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"(]\"")
    s3 = "(]"
    solution3 = Solution()
    result3 = solution3.isValid(s3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"([)]\"")
    s4 = "([)]"
    solution4 = Solution()
    result4 = solution4.isValid(s4)
    print(f"结果: {result4}")
    print(f"期望结果: False")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: \"{[]}\"")
    s5 = "{[]}"
    solution5 = Solution()
    result5 = solution5.isValid(s5)
    print(f"结果: {result5}")
    print(f"期望结果: True")
