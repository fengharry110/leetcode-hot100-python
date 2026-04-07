"""
122. 买卖股票的最佳时机II
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。

示例 1：
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
     总利润为 4 + 3 = 7 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     总利润为 4 。

示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。
"""

from typing import List


class Solution:
    """
    买卖股票的最佳时机II解法类
    
    解题思路：
        贪心算法，只要当天价格高于前一天价格，就进行交易
        
    算法步骤：
        1. 初始化总利润为0
        2. 遍历数组，从第二天开始：
           - 如果当天价格高于前一天价格，计算利润并加到总利润中
        3. 返回总利润
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        计算最大利润
        
        参数:
            prices: 股票价格数组
            
        返回:
            最大利润
        """
        if not prices:
            return 0
        
        total_profit = 0
        n = len(prices)
        
        for i in range(1, n):
            # 如果当天价格高于前一天，就进行交易
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        
        return total_profit


class SolutionDynamicProgramming:
    """
    动态规划解法类
    
    解题思路：
        使用动态规划，记录每天持有和不持有的最大利润
        
    算法步骤：
        1. 初始化dp数组，dp[i][0]表示第i天不持有股票的最大利润，dp[i][1]表示持有股票的最大利润
        2. 状态转移方程：
           - dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
           - dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        3. 返回dp[-1][0]
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        计算最大利润（动态规划版本）
        
        参数:
            prices: 股票价格数组
            
        返回:
            最大利润
        """
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0  # 第一天不持有
        dp[0][1] = -prices[0]  # 第一天持有
        
        for i in range(1, n):
            # 不持有：前一天不持有或前一天持有今天卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 持有：前一天持有或前一天不持有今天买入
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[-1][0]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [7,1,5,3,6,4]")
    prices1 = [7,1,5,3,6,4]
    solution = Solution()
    result1 = solution.maxProfit(prices1)
    print(f"结果: {result1}")
    print(f"期望结果: 7")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2,3,4,5]")
    prices2 = [1,2,3,4,5]
    solution2 = SolutionDynamicProgramming()
    result2 = solution2.maxProfit(prices2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [7,6,4,3,1]")
    prices3 = [7,6,4,3,1]
    solution3 = Solution()
    result3 = solution3.maxProfit(prices3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,1,2]")
    prices4 = [1,2,1,2]
    solution4 = SolutionDynamicProgramming()
    result4 = solution4.maxProfit(prices4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
