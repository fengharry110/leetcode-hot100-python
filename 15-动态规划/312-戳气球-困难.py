"""
312. 戳气球
困难
有 n 个气球，编号为 0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10

提示：
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # 添加首尾的虚拟气球
        balloons = [1] + nums + [1]
        
        # dp[i][j] 表示戳破区间 (i, j) 内所有气球能获得的最大硬币数
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # 区间长度从1到n
        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                j = i + length + 1
                # 枚举最后戳破的气球k
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], 
                                   dp[i][k] + dp[k][j] + balloons[i] * balloons[k] * balloons[j])
        
        return dp[0][n + 1]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [3, 1, 5, 8]
    print(f"输入: nums = {nums1}")
    print(f"输出: {solution.maxCoins(nums1)}")
    
    # 测试用例2
    nums2 = [1, 5]
    print(f"\n输入: nums = {nums2}")
    print(f"输出: {solution.maxCoins(nums2)}")
