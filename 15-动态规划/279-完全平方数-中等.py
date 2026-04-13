"""
279. 完全平方数
中等
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数乘以自身。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 10^4
"""

import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 动态规划
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    n1 = 12
    print(f"输入: n = {n1}")
    print(f"输出: {solution.numSquares(n1)}")
    
    # 测试用例2
    n2 = 13
    print(f"\n输入: n = {n2}")
    print(f"输出: {solution.numSquares(n2)}")
