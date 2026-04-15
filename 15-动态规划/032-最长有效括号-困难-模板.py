"""
32. 最长有效括号
https://leetcode.cn/problems/longest-valid-parentheses/description/

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
    """
    请在此处实现你的解法
    """
    
    def longestValidParentheses(self, s: str) -> int:
        """
        找出最长有效括号子串的长度
        
        参数:
            s: 只包含括号的字符串
            
        返回:
            最长有效括号子串的长度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = '(()'")
    s1 = "(()"
    result1 = solution.longestValidParentheses(s1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = ')()())'")
    s2 = ")()())"
    result2 = solution.longestValidParentheses(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = ''")
    s3 = ""
    result3 = solution.longestValidParentheses(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
