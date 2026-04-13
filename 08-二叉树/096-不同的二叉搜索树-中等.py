"""
96. 不同的二叉搜索树
中等
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
输入：n = 3
输出：5

示例 2：
输入：n = 1
输出：1

提示：
1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划：卡特兰数
        # G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    n1 = 3
    print(f"输入: n = {n1}")
    print(f"输出: {solution.numTrees(n1)}")
    
    # 测试用例2
    n2 = 1
    print(f"\n输入: n = {n2}")
    print(f"输出: {solution.numTrees(n2)}")
    
    # 测试用例3
    n3 = 4
    print(f"\n输入: n = {n3}")
    print(f"输出: {solution.numTrees(n3)}")
