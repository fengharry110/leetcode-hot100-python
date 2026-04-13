"""
32. 最长有效括号
困难
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0

提示：
0 <= s.length <= 3 * 10^4
s[i] 为 '(' 或 ')'
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # 栈底存-1作为基准
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 更新基准
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    s1 = "(()"
    print(f"输入: s = '{s1}'")
    print(f"输出: {solution.longestValidParentheses(s1)}")
    
    # 测试用例2
    s2 = ")()())"
    print(f"\n输入: s = '{s2}'")
    print(f"输出: {solution.longestValidParentheses(s2)}")
    
    # 测试用例3
    s3 = ""
    print(f"\n输入: s = '{s3}'")
    print(f"输出: {solution.longestValidParentheses(s3)}")
