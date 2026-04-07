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
"""

from typing import Optional


class Solution:
    """
    滑动窗口 + 哈希表解法类
    
    解题思路：
        使用滑动窗口（双指针）和哈希表来记录字符的位置
        当遇到重复字符时，移动左指针到重复字符的下一个位置
        
    算法步骤：
        1. 初始化左指针left=0，最大长度max_length=0
        2. 遍历字符串，右指针right从0开始：
           - 如果当前字符在哈希表中且位置>=left，更新left到哈希表中的位置+1
           - 更新哈希表中当前字符的位置为right
           - 更新max_length为max(max_length, right - left + 1)
        3. 返回max_length
        
    时间复杂度：O(n)
    空间复杂度：O(k)，k为字符集大小
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        找出无重复字符的最长子串的长度
        
        参数:
            s: 输入字符串
            
        返回:
            最长子串的长度
        """
        # 哈希表存储字符的最新位置
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 如果字符重复且在当前窗口内
            if s[right] in char_index and char_index[s[right]] >= left:
                # 移动左指针到重复字符的下一个位置
                left = char_index[s[right]] + 1
            
            # 更新字符的位置
            char_index[s[right]] = right
            
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length


class SolutionSet:
    """
    滑动窗口 + 集合解法类
    
    解题思路：
        使用滑动窗口和集合来检测重复字符
        当遇到重复字符时，移动左指针直到没有重复
        
    算法步骤：
        1. 初始化左指针left=0，最大长度max_length=0，集合char_set
        2. 遍历字符串，右指针right从0开始：
           - 当当前字符在集合中，移除左指针字符并移动左指针
           - 将当前字符加入集合
           - 更新max_length为max(max_length, right - left + 1)
        3. 返回max_length
        
    时间复杂度：O(n)
    空间复杂度：O(k)
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        使用集合来检测重复字符
        
        参数:
            s: 输入字符串
            
        返回:
            最长子串的长度
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # 当字符重复时，移动左指针
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # 添加当前字符到集合
            char_set.add(s[right])
            
            # 更新最大长度
            max_length = max(max_length, right - left + 1)
        
        return max_length


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
    solution2 = SolutionSet()
    result2 = solution2.lengthOfLongestSubstring(s2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: \"pwwkew\"")
    s3 = "pwwkew"
    solution3 = Solution()
    result3 = solution3.lengthOfLongestSubstring(s3)
    print(f"结果: {result3}")
    print(f"期望结果: 3")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: \"\"")
    s4 = ""
    solution4 = Solution()
    result4 = solution4.lengthOfLongestSubstring(s4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: \"abcdefg\"")
    s5 = "abcdefg"
    solution5 = SolutionSet()
    result5 = solution5.lengthOfLongestSubstring(s5)
    print(f"结果: {result5}")
    print(f"期望结果: 7")
