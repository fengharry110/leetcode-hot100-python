"""
301. 删除无效的括号
困难
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

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
"""

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 计算需要删除的左右括号数量
        left_remove, right_remove = 0, 0
        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        
        result = set()
        
        def dfs(index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add(expr)
                return
            
            char = s[index]
            
            # 删除当前字符
            if char == '(' and left_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem - 1, right_rem, expr)
            elif char == ')' and right_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem, right_rem - 1, expr)
            
            # 保留当前字符
            if char != '(' and char != ')':
                dfs(index + 1, left_count, right_count, left_rem, right_rem, expr + char)
            elif char == '(':
                dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, expr + char)
            elif char == ')' and left_count > right_count:
                dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, expr + char)
        
        dfs(0, 0, 0, left_remove, right_remove, "")
        return list(result)


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    s1 = "()())()"
    print(f"输入: s = '{s1}'")
    print(f"输出: {solution.removeInvalidParentheses(s1)}")
    
    # 测试用例2
    s2 = "(a)())()"
    print(f"\n输入: s = '{s2}'")
    print(f"输出: {solution.removeInvalidParentheses(s2)}")
    
    # 测试用例3
    s3 = ")("
    print(f"\n输入: s = '{s3}'")
    print(f"输出: {solution.removeInvalidParentheses(s3)}")
