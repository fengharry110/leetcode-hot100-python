"""
322. 零钱兑换
https://leetcode.cn/problems/coin-change/description/

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        计算凑成总金额所需的最少硬币个数
        
        参数:
            coins: 硬币面额数组
            amount: 目标金额
            
        返回:
            最少硬币个数，无法组成则返回-1
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: coins = [1, 2, 5], amount = 11")
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = solution.coinChange(coins1, amount1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: coins = [2], amount = 3")
    coins2 = [2]
    amount2 = 3
    result2 = solution.coinChange(coins2, amount2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: coins = [1], amount = 0")
    coins3 = [1]
    amount3 = 0
    result3 = solution.coinChange(coins3, amount3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
