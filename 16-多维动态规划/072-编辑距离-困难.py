"""
72. 编辑距离
https://leetcode.cn/problems/edit-distance/description/

给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

from typing import List


class Solution:
    """
    编辑距离解法类
    
    解题思路：
        动态规划，dp[i][j]表示word1前i个字符转换为word2前j个字符的最少操作数
        
    算法步骤：
        1. 初始化dp数组
        2. 填充第一行和第一列
        3. 遍历两个单词，计算每个位置的最少操作数
        4. 返回dp[-1][-1]
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def minDistance(self, word1: str, word2: str) -> int:
        """
        计算编辑距离
        
        参数:
            word1: 第一个单词
            word2: 第二个单词
            
        返回:
            最少操作数
        """
        m, n = len(word1), len(word2)
        
        # 初始化dp数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 填充第一行和第一列
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # 计算每个位置的最少操作数
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[m][n]


class SolutionOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用一维数组优化空间复杂度
        
    算法步骤：
        1. 初始化prev数组
        2. 遍历两个单词，更新prev数组
        3. 返回prev[-1]
        
    时间复杂度：O(mn)
    空间复杂度：O(n)
    """
    
    def minDistance(self, word1: str, word2: str) -> int:
        """
        计算编辑距离（空间优化版本）
        
        参数:
            word1: 第一个单词
            word2: 第二个单词
            
        返回:
            最少操作数
        """
        m, n = len(word1), len(word2)
        
        # 确保n <= m，以减少空间使用
        if n > m:
            return self.minDistance(word2, word1)
        
        # 初始化prev数组
        prev = list(range(n + 1))
        
        for i in range(1, m + 1):
            curr = [i] * (n + 1)
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
            prev = curr
        
        return prev[n]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: word1 = \"horse\", word2 = \"ros\"")
    word1_1 = "horse"
    word2_1 = "ros"
    solution = Solution()
    result1 = solution.minDistance(word1_1, word2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: word1 = \"intention\", word2 = \"execution\"")
    word1_2 = "intention"
    word2_2 = "execution"
    solution2 = SolutionOptimized()
    result2 = solution2.minDistance(word1_2, word2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 5")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: word1 = \"\", word2 = \"a\"")
    word1_3 = ""
    word2_3 = "a"
    solution3 = Solution()
    result3 = solution3.minDistance(word1_3, word2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: word1 = \"a\", word2 = \"a\"")
    word1_4 = "a"
    word2_4 = "a"
    solution4 = SolutionOptimized()
    result4 = solution4.minDistance(word1_4, word2_4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
