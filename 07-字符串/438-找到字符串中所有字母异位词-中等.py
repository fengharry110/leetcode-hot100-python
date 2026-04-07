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
起始索引等于 1 的子串是 "ba", 它不是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""

from typing import List


class Solution:
    """
    找到字符串中所有字母异位词解法类
    
    解题思路：
        使用滑动窗口和字符计数
        
    算法步骤：
        1. 计算p的字符计数
        2. 初始化滑动窗口的左右指针
        3. 遍历s，维护窗口内的字符计数
        4. 当窗口大小等于p的长度时，比较字符计数
        5. 如果计数相同，记录起始索引
        6. 移动左指针，更新计数
        
    时间复杂度：O(n)
    空间复杂度：O(1)
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
        n, m = len(s), len(p)
        if n < m:
            return []
        
        # 初始化计数数组
        p_count = [0] * 26
        s_count = [0] * 26
        
        # 计算p的字符计数
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        # 初始化滑动窗口
        result = []
        left = 0
        
        for right in range(n):
            # 更新右指针的计数
            s_count[ord(s[right]) - ord('a')] += 1
            
            # 当窗口大小等于p的长度时
            if right - left + 1 == m:
                # 比较计数
                if s_count == p_count:
                    result.append(left)
                # 移动左指针，更新计数
                s_count[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return result


class SolutionOptimized:
    """
    优化解法类
    
    解题思路：
        使用滑动窗口和差异计数
        
    算法步骤：
        1. 计算p的字符计数
        2. 初始化滑动窗口的左右指针和差异计数
        3. 遍历s，维护窗口内的字符计数和差异计数
        4. 当窗口大小等于p的长度时，检查差异计数
        5. 如果差异为0，记录起始索引
        6. 移动左指针，更新计数和差异
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        找到字符串中所有字母异位词（优化版本）
        
        参数:
            s: 字符串
            p: 目标字符串
            
        返回:
            起始索引列表
        """
        n, m = len(s), len(p)
        if n < m:
            return []
        
        # 初始化计数数组
        count = [0] * 26
        
        # 计算p的字符计数和初始窗口的差异
        for i in range(m):
            count[ord(p[i]) - ord('a')] -= 1
            count[ord(s[i]) - ord('a')] += 1
        
        # 计算初始差异
        diff = 0
        for c in count:
            if c != 0:
                diff += 1
        
        result = []
        if diff == 0:
            result.append(0)
        
        # 滑动窗口
        for i in range(m, n):
            # 加入右字符
            right_char = s[i]
            right_idx = ord(right_char) - ord('a')
            if count[right_idx] == 0:
                diff += 1
            count[right_idx] += 1
            if count[right_idx] == 0:
                diff -= 1
            
            # 移除左字符
            left_char = s[i - m]
            left_idx = ord(left_char) - ord('a')
            if count[left_idx] == 0:
                diff += 1
            count[left_idx] -= 1
            if count[left_idx] == 0:
                diff -= 1
            
            # 检查差异
            if diff == 0:
                result.append(i - m + 1)
        
        return result


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
    solution2 = SolutionOptimized()
    result2 = solution2.findAnagrams(s2, p2)
    print(f"结果: {result2}")
    print(f"期望结果: [0, 1, 2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = \"a\", p = \"a\"")
    s3 = "a"
    p3 = "a"
    solution3 = Solution()
    result3 = solution3.findAnagrams(s3, p3)
    print(f"结果: {result3}")
    print(f"期望结果: [0]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: s = \"baa\", p = \"aa\"")
    s4 = "baa"
    p4 = "aa"
    solution4 = SolutionOptimized()
    result4 = solution4.findAnagrams(s4, p4)
    print(f"结果: {result4}")
    print(f"期望结果: [1]")
