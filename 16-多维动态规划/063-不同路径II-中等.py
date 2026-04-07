"""
63. 不同路径 II
https://leetcode.cn/problems/unique-paths-ii/description/

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
"""

from typing import List


class Solution:
    """
    不同路径II解法类
    
    解题思路：
        动态规划，dp[i][j]表示到达(i,j)的路径数
        
    算法步骤：
        1. 初始化dp数组
        2. 处理边界条件
        3. 对于每个位置(i,j)，如果有障碍物，dp[i][j] = 0
        4. 否则，dp[i][j] = dp[i-1][j] + dp[i][j-1]
        5. 返回dp[m-1][n-1]
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        计算不同路径数（含障碍物）
        
        参数:
            obstacleGrid: 网格，0表示空格，1表示障碍物
            
        返回:
            不同路径数
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 初始化dp数组
        dp = [[0] * n for _ in range(m)]
        
        # 处理起点
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0
        
        # 处理第一行
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # 处理第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # 计算dp数组
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


class SolutionOptimized:
    """
    空间优化解法类
    """
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        计算不同路径数（含障碍物，空间优化版本）
        
        参数:
            obstacleGrid: 网格，0表示空格，1表示障碍物
            
        返回:
            不同路径数
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 初始化dp数组
        dp = [0] * n
        
        # 处理起点
        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        else:
            return 0
        
        # 处理第一行
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[j] = dp[j-1]
        
        # 计算dp数组
        for i in range(1, m):
            # 处理第一列
            if obstacleGrid[i][0] == 0:
                dp[0] = dp[0]
            else:
                dp[0] = 0
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
        
        return dp[n-1]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]")
    obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()
    result1 = solution.uniquePathsWithObstacles(obstacleGrid1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: obstacleGrid = [[0,1],[0,0]]")
    obstacleGrid2 = [[0,1],[0,0]]
    solution2 = SolutionOptimized()
    result2 = solution2.uniquePathsWithObstacles(obstacleGrid2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: obstacleGrid = [[1]]")
    obstacleGrid3 = [[1]]
    solution3 = Solution()
    result3 = solution3.uniquePathsWithObstacles(obstacleGrid3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: obstacleGrid = [[0]]")
    obstacleGrid4 = [[0]]
    solution4 = SolutionOptimized()
    result4 = solution4.uniquePathsWithObstacles(obstacleGrid4)
    print(f"结果: {result4}")
    print(f"期望结果: 1")
