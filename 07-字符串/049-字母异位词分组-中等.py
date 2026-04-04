"""
49. 字母异位词分组
https://leetcode.cn/problems/group-anagrams/description/

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    哈希表解法类
    
    解题思路：
        使用哈希表，将每个字符串的字符排序后作为键，原字符串作为值
        这样字母异位词会有相同的排序键
        
    算法步骤：
        1. 初始化一个哈希表
        2. 遍历每个字符串：
           - 将字符串转换为字符列表并排序
           - 将排序后的字符列表转换为元组作为键
           - 将原字符串添加到对应键的列表中
        3. 将哈希表的值转换为列表并返回
        
    时间复杂度：O(n * k log k)，其中n是字符串数量，k是字符串长度
    空间复杂度：O(n * k)
    """
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        将字母异位词分组
        
        参数:
            strs: 字符串数组
            
        返回:
            分组后的列表
        """
        # 使用defaultdict来存储分组
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 将字符串排序作为键
            sorted_key = tuple(sorted(s))
            anagram_map[sorted_key].append(s)
        
        # 将值转换为列表返回
        return list(anagram_map.values())


class SolutionCount:
    """
    计数解法类
    
    解题思路：
        使用字符计数作为键，避免排序操作
        对于每个字符串，统计每个字符出现的次数，用这个计数数组作为键
        
    算法步骤：
        1. 初始化一个哈希表
        2. 遍历每个字符串：
           - 初始化一个长度为26的计数数组
           - 统计每个字符的出现次数
           - 将计数数组转换为元组作为键
           - 将原字符串添加到对应键的列表中
        3. 将哈希表的值转换为列表并返回
        
    时间复杂度：O(n * k)
    空间复杂度：O(n * k)
    """
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        使用字符计数分组字母异位词
        
        参数:
            strs: 字符串数组
            
        返回:
            分组后的列表
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 初始化字符计数数组
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # 将计数数组转换为元组作为键
            anagram_map[tuple(count)].append(s)
        
        return list(anagram_map.values())


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"]")
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result1 = solution.groupAnagrams(strs1)
    print(f"结果: {result1}")
    print(f"期望结果: [[\"bat\"], [\"nat\", \"tan\"], [\"ate\", \"eat\", \"tea\"]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [\"\"]")
    strs2 = [""]
    solution2 = SolutionCount()
    result2 = solution2.groupAnagrams(strs2)
    print(f"结果: {result2}")
    print(f"期望结果: [[\"\"]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [\"a\"]")
    strs3 = ["a"]
    solution3 = Solution()
    result3 = solution3.groupAnagrams(strs3)
    print(f"结果: {result3}")
    print(f"期望结果: [[\"a\"]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [\"ab\", \"ba\", \"abc\", \"cba\", \"bac\"]")
    strs4 = ["ab", "ba", "abc", "cba", "bac"]
    solution4 = SolutionCount()
    result4 = solution4.groupAnagrams(strs4)
    print(f"结果: {result4}")
