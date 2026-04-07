"""
392. 判断子序列
https://leetcode.cn/problems/is-subsequence/description/

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true

示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false
"""

class Solution:
    """
    判断子序列解法类
    
    解题思路：
        双指针，遍历t，同时匹配s
        
    算法步骤：
        1. 初始化两个指针i和j，分别指向s和t的开始
        2. 遍历t，当s[i] == t[j]时，i向前移动
        3. 如果i到达s的末尾，返回True
        4. 否则返回False
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        判断s是否为t的子序列
        
        参数:
            s: 子序列字符串
            t: 目标字符串
            
        返回:
            是否是子序列
        """
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class SolutionDP:
    """
    动态规划解法类
    """
    
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        判断s是否为t的子序列（动态规划版本）
        
        参数:
            s: 子序列字符串
            t: 目标字符串
            
        返回:
            是否是子序列
        """
        m, n = len(s), len(t)
        
        # 构建dp数组，dp[i][j]表示s的前i个字符是否是t的前j个字符的子序列
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 空字符串是任何字符串的子序列
        for j in range(n + 1):
            dp[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[m][n]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: s = \"abc\", t = \"ahbgdc\"")
    s1 = "abc"
    t1 = "ahbgdc"
    solution = Solution()
    result1 = solution.isSubsequence(s1, t1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: s = \"axc\", t = \"ahbgdc\"")
    s2 = "axc"
    t2 = "ahbgdc"
    solution2 = SolutionDP()
    result2 = solution2.isSubsequence(s2, t2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: s = \"\", t = \"ahbgdc\"")
    s3 = ""
    t3 = "ahbgdc"
    solution3 = Solution()
    result3 = solution3.isSubsequence(s3, t3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: s = \"abc\", t = \"\"")
    s4 = "abc"
    t4 = ""
    solution4 = SolutionDP()
    result4 = solution4.isSubsequence(s4, t4)
    print(f"结果: {result4}")
    print(f"期望结果: False")
