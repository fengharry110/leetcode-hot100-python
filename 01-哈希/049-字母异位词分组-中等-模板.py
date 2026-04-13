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

提示：
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] 仅包含小写字母
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        将字母异位词分组
        
        参数:
            strs: 字符串数组
            
        返回:
            分组后的列表
        """
        # TODO: 在此实现你的解法
        pass


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
    result2 = solution.groupAnagrams(strs2)
    print(f"结果: {result2}")
    print(f"期望结果: [[\"\"]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [\"a\"]")
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    print(f"结果: {result3}")
    print(f"期望结果: [[\"a\"]]")
