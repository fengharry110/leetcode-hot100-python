# 1143. 最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 如果不存在公共子序列，返回 0。
# 一个字符串的子序列是指这样一个新的字符串：
# 它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除）后组成的新字符串。
#
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3
#
# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
#
# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0

from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.longestCommonSubsequence('abcde', 'ace')}")  # 期望输出: 3
    
    # 测试2
    print(f"测试2结果: {solution.longestCommonSubsequence('abc', 'abc')}")  # 期望输出: 3
    
    # 测试3
    print(f"测试3结果: {solution.longestCommonSubsequence('abc', 'def')}")  # 期望输出: 0
