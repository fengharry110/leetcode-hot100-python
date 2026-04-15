"""
3. 无重复字符的最长子串
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
"""

from typing import Optional


class Solution:
    """
    请在此处实现你的解法
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        找出无重复字符的最长子串的长度
        
        参数:
            s: 输入字符串
            
        返回:
            最长子串的长度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: \"abcabcbb\"")
    s1 = "abcabcbb"
    solution = Solution()
    result1 = solution.lengthOfLongestSubstring(s1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: \"bbbbb\"")
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"pwwkew\"")
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 3")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"\"")
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: \"abcdefg\"")
    s5 = "abcdefg"
    result5 = solution.lengthOfLongestSubstring(s5)
    print(f"结果: {result5}")
    print(f"期望结果: 7")
