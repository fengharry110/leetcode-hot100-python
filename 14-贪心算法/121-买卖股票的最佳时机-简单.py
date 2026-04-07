"""
121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List


class Solution:
    """
    买卖股票的最佳时机解法类
    
    解题思路：
        使用动态规划，记录历史最低点，计算每天的最大利润
        
    算法步骤：
        1. 初始化历史最低点为第一个元素
        2. 初始化最大利润为0
        3. 遍历数组：
           - 更新历史最低点
           - 计算当前利润
           - 更新最大利润
        4. 返回最大利润
        
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
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # 更新历史最低点
            if price < min_price:
                min_price = price
            # 计算当前利润
            current_profit = price - min_price
            # 更新最大利润
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [7,1,5,3,6,4]")
    prices1 = [7,1,5,3,6,4]
    solution = Solution()
    result1 = solution.maxProfit(prices1)
    print(f"结果: {result1}")
    print(f"期望结果: 5")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [7,6,4,3,1]")
    prices2 = [7,6,4,3,1]
    solution2 = Solution()
    result2 = solution2.maxProfit(prices2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,2,3,4,5]")
    prices3 = [1,2,3,4,5]
    solution3 = Solution()
    result3 = solution3.maxProfit(prices3)
    print(f"结果: {result3}")
    print(f"期望结果: 4")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [2,4,1]")
    prices4 = [2,4,1]
    solution4 = Solution()
    result4 = solution4.maxProfit(prices4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
