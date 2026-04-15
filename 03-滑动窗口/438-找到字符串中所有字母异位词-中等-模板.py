"""
438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

提示:
1 <= s.length, p.length <= 3 * 10^4
s 和 p 仅包含小写英文字母
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        找到字符串中所有字母异位词
        
        参数:
            s: 字符串
            p: 目标字符串
            
        返回:
            起始索引列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = \"cbaebabacd\", p = \"abc\"")
    s1 = "cbaebabacd"
    p1 = "abc"
    solution = Solution()
    result1 = solution.findAnagrams(s1, p1)
    print(f"结果: {result1}")
    print(f"期望结果: [0, 6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = \"abab\", p = \"ab\"")
    s2 = "abab"
    p2 = "ab"
    result2 = solution.findAnagrams(s2, p2)
    print(f"结果: {result2}")
    print(f"期望结果: [0, 1, 2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = \"a\", p = \"a\"")
    s3 = "a"
    p3 = "a"
    result3 = solution.findAnagrams(s3, p3)
    print(f"结果: {result3}")
    print(f"期望结果: [0]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: s = \"baa\", p = \"aa\"")
    s4 = "baa"
    p4 = "aa"
    result4 = solution.findAnagrams(s4, p4)
    print(f"结果: {result4}")
    print(f"期望结果: [1]")
