"""
10. 正则表达式匹配
困难
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。

示例 1：
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个，所以这里 'a' 可以匹配 "aa"。

示例 3：
输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

提示：
1 <= s.length <= 20
1 <= p.length <= 20
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都有效字符。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] 表示 s[:i] 和 p[:j] 是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # 处理 p 以 a* 或 .* 开头的情况
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * 匹配零个前面的字符
                    dp[i][j] = dp[i][j - 2]
                    # * 匹配一个或多个前面的字符
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    s1, p1 = "aa", "a"
    print(f"输入: s = '{s1}', p = '{p1}'")
    print(f"输出: {solution.isMatch(s1, p1)}")
    
    # 测试用例2
    s2, p2 = "aa", "a*"
    print(f"\n输入: s = '{s2}', p = '{p2}'")
    print(f"输出: {solution.isMatch(s2, p2)}")
    
    # 测试用例3
    s3, p3 = "ab", ".*"
    print(f"\n输入: s = '{s3}', p = '{p3}'")
    print(f"输出: {solution.isMatch(s3, p3)}")
