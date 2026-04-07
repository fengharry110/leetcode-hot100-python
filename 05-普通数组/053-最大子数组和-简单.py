"""
53. 最大子数组和
https://leetcode.cn/problems/maximum-subarray/description/

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
"""

from typing import List


class Solution:
    """
    动态规划解法类
    
    解题思路：
        定义dp[i]为以nums[i]结尾的最大子数组和
        状态转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i])
        
    算法步骤：
        1. 初始化dp数组和max_sum
        2. 遍历数组：
           - 计算dp[i]
           - 更新max_sum
        3. 返回max_sum
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        计算最大子数组和
        
        参数:
            nums: 整数数组
            
        返回:
            最大子数组和
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # 初始化dp数组
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        
        for i in range(1, n):
            # 选择当前元素或者当前元素加上前面的和
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            # 更新最大和
            max_sum = max(max_sum, dp[i])
        
        return max_sum


class SolutionSpaceOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用一个变量代替数组，优化空间复杂度
        
    算法步骤：
        1. 初始化current_sum和max_sum
        2. 遍历数组：
           - 更新current_sum
           - 更新max_sum
        3. 返回max_sum
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        空间优化版本计算最大子数组和
        
        参数:
            nums: 整数数组
            
        返回:
            最大子数组和
        """
        if not nums:
            return 0
        
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            # 选择当前元素或者当前元素加上前面的和
            current_sum = max(nums[i], current_sum + nums[i])
            # 更新最大和
            max_sum = max(max_sum, current_sum)
        
        return max_sum


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [-2,1,-3,4,-1,2,1,-5,4]")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result1 = solution.maxSubArray(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 6")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1]")
    nums2 = [1]
    solution2 = SolutionSpaceOptimized()
    result2 = solution2.maxSubArray(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [5,4,-1,7,8]")
    nums3 = [5, 4, -1, 7, 8]
    solution3 = Solution()
    result3 = solution3.maxSubArray(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 23")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [-1,-2,-3,-4]")
    nums4 = [-1, -2, -3, -4]
    solution4 = SolutionSpaceOptimized()
    result4 = solution4.maxSubArray(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: -1")
