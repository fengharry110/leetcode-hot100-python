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
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

提示：
1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        计算两个字符串的最长公共子序列长度
        
        参数:
            text1: 第一个字符串
            text2: 第二个字符串
            
        返回:
            最长公共子序列长度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: text1 = 'abcde', text2 = 'ace'")
    text1_1 = "abcde"
    text2_1 = "ace"
    result1 = solution.longestCommonSubsequence(text1_1, text2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: text1 = 'abc', text2 = 'abc'")
    text1_2 = "abc"
    text2_2 = "abc"
    result2 = solution.longestCommonSubsequence(text1_2, text2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: text1 = 'abc', text2 = 'def'")
    text1_3 = "abc"
    text2_3 = "def"
    result3 = solution.longestCommonSubsequence(text1_3, text2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
