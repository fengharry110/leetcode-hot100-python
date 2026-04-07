"""
62. 不同路径
https://leetcode.cn/problems/unique-paths/description/

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
"""

class Solution:
    """
    不同路径解法类
    
    解题思路：
        动态规划，dp[i][j]表示到达(i,j)的路径数
        
    算法步骤：
        1. 初始化dp数组，第一行和第一列都为1
        2. 对于每个位置(i,j)，dp[i][j] = dp[i-1][j] + dp[i][j-1]
        3. 返回dp[m-1][n-1]
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def uniquePaths(self, m: int, n: int) -> int:
        """
        计算不同路径数
        
        参数:
            m: 网格行数
            n: 网格列数
            
        返回:
            不同路径数
        """
        # 初始化dp数组
        dp = [[1] * n for _ in range(m)]
        
        # 计算dp数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


class SolutionOptimized:
    """
    空间优化解法类
    """
    
    def uniquePaths(self, m: int, n: int) -> int:
        """
        计算不同路径数（空间优化版本）
        
        参数:
            m: 网格行数
            n: 网格列数
            
        返回:
            不同路径数
        """
        # 确保n <= m，减少空间使用
        if n > m:
            return self.uniquePaths(n, m)
        
        # 初始化dp数组
        dp = [1] * n
        
        # 计算dp数组
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[n-1]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: m = 3, n = 7")
    m1 = 3
    n1 = 7
    solution = Solution()
    result1 = solution.uniquePaths(m1, n1)
    print(f"结果: {result1}")
    print(f"期望结果: 28")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: m = 3, n = 2")
    m2 = 3
    n2 = 2
    solution2 = SolutionOptimized()
    result2 = solution2.uniquePaths(m2, n2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: m = 1, n = 1")
    m3 = 1
    n3 = 1
    solution3 = Solution()
    result3 = solution3.uniquePaths(m3, n3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: m = 4, n = 4")
    m4 = 4
    n4 = 4
    solution4 = SolutionOptimized()
    result4 = solution4.uniquePaths(m4, n4)
    print(f"结果: {result4}")
    print(f"期望结果: 20")
