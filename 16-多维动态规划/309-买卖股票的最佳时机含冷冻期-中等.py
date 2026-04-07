"""
309. 买卖股票的最佳时机含冷冻期
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

给定一个整数数组prices，其中第 prices[i] 表示第 i 天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
输入: prices = [1]
输出: 0
"""

from typing import List


class Solution:
    """
    买卖股票的最佳时机含冷冻期解法类
    
    解题思路：
        使用动态规划，定义三种状态：
        - dp[i][0]: 持有股票的最大利润
        - dp[i][1]: 不持有股票且处于冷冻期的最大利润
        - dp[i][2]: 不持有股票且不处于冷冻期的最大利润
        
    算法步骤：
        1. 初始化dp数组
        2. 状态转移方程：
           - dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
           - dp[i][1] = dp[i-1][0] + prices[i]
           - dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        3. 返回max(dp[-1][1], dp[-1][2])
        
    时间复杂度：O(n)
    空间复杂度：O(n)
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
        
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        # 初始状态
        dp[0][0] = -prices[0]  # 持有股票
        dp[0][1] = 0  # 不持有且冷冻期
        dp[0][2] = 0  # 不持有且非冷冻期
        
        for i in range(1, n):
            # 持有股票：前一天持有或前一天非冷冻期买入
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            # 不持有且冷冻期：前一天卖出
            dp[i][1] = dp[i-1][0] + prices[i]
            # 不持有且非冷冻期：前一天非冷冻期或前一天冷冻期
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1][1], dp[-1][2])


class SolutionOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用变量代替二维数组，优化空间复杂度
        
    算法步骤：
        1. 初始化变量
        2. 遍历数组，更新变量
        3. 返回max(sell, rest)
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        计算最大利润（空间优化版本）
        
        参数:
            prices: 股票价格数组
            
        返回:
            最大利润
        """
        if not prices:
            return 0
        
        n = len(prices)
        # 初始化状态
        hold = -prices[0]  # 持有股票
        sell = 0  # 不持有且冷冻期
        rest = 0  # 不持有且非冷冻期
        
        for i in range(1, n):
            # 保存前一天的状态
            prev_hold = hold
            prev_sell = sell
            prev_rest = rest
            
            # 更新状态
            hold = max(prev_hold, prev_rest - prices[i])
            sell = prev_hold + prices[i]
            rest = max(prev_rest, prev_sell)
        
        return max(sell, rest)


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3,0,2]")
    prices1 = [1,2,3,0,2]
    solution = Solution()
    result1 = solution.maxProfit(prices1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1]")
    prices2 = [1]
    solution2 = SolutionOptimized()
    result2 = solution2.maxProfit(prices2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,2,4,5,7]")
    prices3 = [1,2,4,5,7]
    solution3 = Solution()
    result3 = solution3.maxProfit(prices3)
    print(f"结果: {result3}")
    print(f"期望结果: 6")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [6,1,3,2,4,7]")
    prices4 = [6,1,3,2,4,7]
    solution4 = SolutionOptimized()
    result4 = solution4.maxProfit(prices4)
    print(f"结果: {result4}")
    print(f"期望结果: 6")
