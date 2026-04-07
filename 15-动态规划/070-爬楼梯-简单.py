"""
70. 爬楼梯
https://leetcode.cn/problems/climbing-stairs/description/

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""

from typing import Optional


class Solution:
    """
    动态规划解法类
    
    解题思路：
        第n阶的爬法 = 第n-1阶的爬法 + 第n-2阶的爬法
        类似于斐波那契数列
        
    算法步骤：
        1. 初始化dp数组，dp[0]=1, dp[1]=1
        2. 从2到n遍历：
           - dp[i] = dp[i-1] + dp[i-2]
        3. 返回dp[n]
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def climbStairs(self, n: int) -> int:
        """
        计算爬楼梯的方法数
        
        参数:
            n: 台阶数
            
        返回:
            不同的爬法数
        """
        if n <= 1:
            return 1
        
        # 初始化dp数组
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


class SolutionSpaceOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用三个变量代替数组，优化空间复杂度
        
    算法步骤：
        1. 初始化prev1=1, prev2=1, current=1
        2. 从2到n遍历：
           - current = prev1 + prev2
           - prev2 = prev1
           - prev1 = current
        3. 返回current
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def climbStairs(self, n: int) -> int:
        """
        空间优化版本计算爬楼梯的方法数
        
        参数:
            n: 台阶数
            
        返回:
            不同的爬法数
        """
        if n <= 1:
            return 1
        
        prev1, prev2, current = 1, 1, 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return current


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: n = 2")
    n1 = 2
    solution = Solution()
    result1 = solution.climbStairs(n1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: n = 3")
    n2 = 3
    solution2 = SolutionSpaceOptimized()
    result2 = solution2.climbStairs(n2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: n = 4")
    n3 = 4
    solution3 = Solution()
    result3 = solution3.climbStairs(n3)
    print(f"结果: {result3}")
    print(f"期望结果: 5")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: n = 5")
    n4 = 5
    solution4 = SolutionSpaceOptimized()
    result4 = solution4.climbStairs(n4)
    print(f"结果: {result4}")
    print(f"期望结果: 8")
