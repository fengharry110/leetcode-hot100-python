"""
131. 分割回文串
https://leetcode.cn/problems/palindrome-partitioning/description/

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def partition(self, s: str) -> List[List[str]]:
        """
        将字符串分割成回文子串的所有方案
        
        参数:
            s: 输入字符串
            
        返回:
            所有可能的分割方案
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = 'aab'")
    s1 = "aab"
    result1 = solution.partition(s1)
    print(f"结果: {result1}")
    print(f"期望结果: [[\"a\",\"a\",\"b\"],[\"aa\",\"b\"]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = 'a'")
    s2 = "a"
    result2 = solution.partition(s2)
    print(f"结果: {result2}")
    print(f"期望结果: [[\"a\"]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = 'aabb'")
    s3 = "aabb"
    result3 = solution.partition(s3)
    print(f"结果: {result3}")
    print(f"期望结果: [[\"a\",\"a\",\"b\",\"b\"],[\"a\",\"a\",\"bb\"],[\"aa\",\"b\",\"b\"],[\"aa\",\"bb\"]]")
