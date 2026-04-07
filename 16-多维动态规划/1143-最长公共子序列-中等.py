"""
1143. 最长公共子序列
https://leetcode.cn/problems/longest-common-subsequence/description/

给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
"""

from typing import Optional


class Solution:
    """
    动态规划解法类
    
    解题思路：
        使用二维动态规划，dp[i][j]表示text1的前i个字符和text2的前j个字符的最长公共子序列长度
        
    算法步骤：
        1. 初始化dp数组，大小为(m+1)×(n+1)
        2. 遍历两个字符串：
           - 如果当前字符相等，dp[i][j] = dp[i-1][j-1] + 1
           - 否则，dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        3. 返回dp[m][n]
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        计算两个字符串的最长公共子序列长度
        
        参数:
            text1: 第一个字符串
            text2: 第二个字符串
            
        返回:
            最长公共子序列的长度
        """
        m, n = len(text1), len(text2)
        
        # 初始化dp数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # 当前字符相等，长度加1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 当前字符不相等，取最大值
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]


class SolutionSpaceOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用一维数组代替二维数组，优化空间复杂度
        
    算法步骤：
        1. 初始化一维dp数组，长度为n+1
        2. 遍历text1的每个字符：
           - 保存左上角的值
           - 遍历text2的每个字符：
              * 如果当前字符相等，dp[j] = 左上角值 + 1
              * 否则，dp[j] = max(dp[j], dp[j-1])
        3. 返回dp[n]
        
    时间复杂度：O(mn)
    空间复杂度：O(n)
    """
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        空间优化版本计算最长公共子序列
        
        参数:
            text1: 第一个字符串
            text2: 第二个字符串
            
        返回:
            最长公共子序列的长度
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        m, n = len(text1), len(text2)
        # 初始化一维dp数组
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            # 保存左上角的值
            prev = 0
            for j in range(1, n + 1):
                # 当前左上角的值
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        
        return dp[n]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: text1 = \"abcde\", text2 = \"ace\"")
    text1_1 = "abcde"
    text2_1 = "ace"
    solution = Solution()
    result1 = solution.longestCommonSubsequence(text1_1, text2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: text1 = \"abc\", text2 = \"abc\"")
    text1_2 = "abc"
    text2_2 = "abc"
    solution2 = SolutionSpaceOptimized()
    result2 = solution2.longestCommonSubsequence(text1_2, text2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: text1 = \"abc\", text2 = \"def\"")
    text1_3 = "abc"
    text2_3 = "def"
    solution3 = Solution()
    result3 = solution3.longestCommonSubsequence(text1_3, text2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: text1 = \"bl\", text2 = \"lyby\"")
    text1_4 = "bl"
    text2_4 = "lyby"
    solution4 = SolutionSpaceOptimized()
    result4 = solution4.longestCommonSubsequence(text1_4, text2_4)
    print(f"结果: {result4}")
