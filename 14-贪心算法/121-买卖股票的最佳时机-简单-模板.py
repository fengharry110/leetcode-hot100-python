"""
121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一只股票一次），设计一个算法来计算你所能获取的最大利润。注意：你不能在买入股票前卖出股票。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        计算买卖股票的最大利润
        
        参数:
            prices: 股票价格数组
            
        返回:
            最大利润
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: prices = [7,1,5,3,6,4]")
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    print(f"结果: {result1}")
    print(f"期望结果: 5")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: prices = [7,6,4,3,1]")
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: prices = [1,2]")
    prices3 = [1, 2]
    result3 = solution.maxProfit(prices3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
