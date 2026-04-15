"""
5. 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/description/

给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""


class Solution:
    """
    请在此处实现你的解法
    """
    
    def longestPalindrome(self, s: str) -> str:
        """
        找出最长回文子串
        
        参数:
            s: 输入字符串
            
        返回:
            最长回文子串
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = 'babad'")
    s1 = "babad"
    result1 = solution.longestPalindrome(s1)
    print(f"结果: {result1}")
    print(f"期望结果: 'bab' 或 'aba'")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = 'cbbd'")
    s2 = "cbbd"
    result2 = solution.longestPalindrome(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 'bb'")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = 'a'")
    s3 = "a"
    result3 = solution.longestPalindrome(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 'a'")
