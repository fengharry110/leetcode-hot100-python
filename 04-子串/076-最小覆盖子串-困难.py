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
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # 统计t中字符出现的次数
        need = Counter(t)
        # 滑动窗口内字符统计
        window = {}
        
        left = 0
        valid = 0  # 窗口中满足need条件的字符个数
        start, length = 0, float('inf')
        
        for right, char in enumerate(s):
            # 扩大窗口
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1
            
            # 判断是否需要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1
                
                # 收缩窗口
                left_char = s[left]
                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
                left += 1
        
        return s[start:start + length] if length != float('inf') else ""


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    s1, t1 = "ADOBECODEBANC", "ABC"
    print(f"输入: s = '{s1}', t = '{t1}'")
    print(f"输出: '{solution.minWindow(s1, t1)}'")
    
    # 测试用例2
    s2, t2 = "a", "a"
    print(f"\n输入: s = '{s2}', t = '{t2}'")
    print(f"输出: '{solution.minWindow(s2, t2)}'")
    
    # 测试用例3
    s3, t3 = "a", "aa"
    print(f"\n输入: s = '{s3}', t = '{t3}'")
    print(f"输出: '{solution.minWindow(s3, t3)}'")
