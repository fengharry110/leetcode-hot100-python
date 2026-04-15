"""
301. 删除无效的括号
https://leetcode.cn/problems/remove-invalid-parentheses/description/

给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。你可以按 任意顺序 返回答案。

示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]

示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

示例 3：
输入：s = ")("
输出：[""]

提示：
1 <= s.length <= 25
s 由小写英文字母和括号 '(' 或 ')' 组成
s 中至多含 20 个括号
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        删除最小数量的无效括号使字符串有效
        
        参数:
            s: 输入字符串
            
        返回:
            所有可能的有效结果
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = '()())()'")
    s1 = "()())()"
    result1 = solution.removeInvalidParentheses(s1)
    print(f"结果: {result1}")
    print(f"期望结果: ['(())()','()()()']")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = '(a)())()'")
    s2 = "(a)())()"
    result2 = solution.removeInvalidParentheses(s2)
    print(f"结果: {result2}")
    print(f"期望结果: ['(a())()','(a)()()']")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = ')('")
    s3 = ")("
    result3 = solution.removeInvalidParentheses(s3)
    print(f"结果: {result3}")
    print(f"期望结果: ['']")
