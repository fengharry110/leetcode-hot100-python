"""
76. 最小覆盖子串
困难
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
对于 t 中重复字符，我们寻找的子字符串内该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

示例 2：
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。

示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

提示：
m == s.length
n == t.length
1 <= m, n <= 10^5
s 和 t 由英文字母组成

进阶：如果你能设计一个在 o(m+n) 时间内解决此问题的算法，请试试看
"""

from collections import Counter


class Solution:
    """
    请在此处实现你的解法
    """
    
    def minWindow(self, s: str, t: str) -> str:
        """
        找到 s 中涵盖 t 所有字符的最小子串
        
        参数:
            s: 源字符串
            t: 目标字符串
            
        返回:
            最小覆盖子串，如果不存在则返回空字符串
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    s1, t1 = "ADOBECODEBANC", "ABC"
    print("=" * 50)
    print(f"输入: s = '{s1}', t = '{t1}'")
    print(f"输出: '{solution.minWindow(s1, t1)}'")
    print(f"期望输出: 'BANC'")
    
    # 测试用例2
    s2, t2 = "a", "a"
    print("\n" + "=" * 50)
    print(f"输入: s = '{s2}', t = '{t2}'")
    print(f"输出: '{solution.minWindow(s2, t2)}'")
    print(f"期望输出: 'a'")
    
    # 测试用例3
    s3, t3 = "a", "aa"
    print("\n" + "=" * 50)
    print(f"输入: s = '{s3}', t = '{t3}'")
    print(f"输出: '{solution.minWindow(s3, t3)}'")
    print(f"期望输出: ''")
