"""
494. 目标和
中等
给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 动态规划：转化为子集和问题
        # 设正数和为P，负数和为N
        # P - N = target, P + N = sum
        # => P = (target + sum) / 2
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        
        pos_sum = (total + target) // 2
        
        # dp[i] 表示和为i的方法数
        dp = [0] * (pos_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(pos_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[pos_sum]


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {solution.findTargetSumWays(nums1, target1)}")
    
    # 测试用例2
    nums2 = [1]
    target2 = 1
    print(f"\n输入: nums = {nums2}, target = {target2}")
    print(f"输出: {solution.findTargetSumWays(nums2, target2)}")
