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
"""

from typing import List


class Solution:
    """
    零钱兑换解法类
    
    解题思路：
        动态规划，dp[i]表示凑成金额i所需的最少硬币数
        
    算法步骤：
        1. 初始化dp数组，dp[0] = 0，其余为无穷大
        2. 遍历每个金额从1到amount
        3. 对于每个金额，遍历所有硬币：
           - 如果硬币面额小于等于当前金额，更新dp[i] = min(dp[i], dp[i - coin] + 1)
        4. 返回dp[amount]，如果为无穷大则返回-1
        
    时间复杂度：O(amount * n)
    空间复杂度：O(amount)
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        计算凑成总金额所需的最少硬币个数
        
        参数:
            coins: 硬币面额数组
            amount: 总金额
            
        返回:
            最少硬币个数，或-1
        """
        # 初始化dp数组
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # 遍历每个金额
        for i in range(1, amount + 1):
            # 遍历所有硬币
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: coins = [1, 2, 5], amount = 11")
    coins1 = [1, 2, 5]
    amount1 = 11
    solution = Solution()
    result1 = solution.coinChange(coins1, amount1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: coins = [2], amount = 3")
    coins2 = [2]
    amount2 = 3
    solution2 = Solution()
    result2 = solution2.coinChange(coins2, amount2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: coins = [1], amount = 0")
    coins3 = [1]
    amount3 = 0
    solution3 = Solution()
    result3 = solution3.coinChange(coins3, amount3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: coins = [1, 3, 4, 5], amount = 7")
    coins4 = [1, 3, 4, 5]
    amount4 = 7
    solution4 = Solution()
    result4 = solution4.coinChange(coins4, amount4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
