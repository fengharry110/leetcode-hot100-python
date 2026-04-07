"""
152. 乘积最大子数组
https://leetcode.cn/problems/maximum-product-subarray/description/

给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

示例 3:
输入: nums = [-2,3,-4]
输出: 24
解释: 子数组 [-2,3,-4] 有最大乘积 24。
"""

from typing import List


class Solution:
    """
    乘积最大子数组解法类
    
    解题思路：
        使用动态规划，同时记录最大值和最小值
        
    算法步骤：
        1. 初始化当前最大值和最小值为数组第一个元素
        2. 遍历数组，对于每个元素：
           - 如果元素为负数，交换最大值和最小值
           - 更新当前最大值为max(当前元素, 当前最大值 * 当前元素)
           - 更新当前最小值为min(当前元素, 当前最小值 * 当前元素)
           - 更新全局最大值
        3. 返回全局最大值
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def maxProduct(self, nums: List[int]) -> int:
        """
        计算乘积最大的子数组
        
        参数:
            nums: 整数数组
            
        返回:
            最大乘积
        """
        if not nums:
            return 0
        
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            # 如果当前元素为负数，交换最大值和最小值
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            
            # 更新当前最大值和最小值
            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])
            
            # 更新全局最大值
            max_product = max(max_product, current_max)
        
        return max_product


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [2,3,-2,4]")
    nums1 = [2,3,-2,4]
    solution = Solution()
    result1 = solution.maxProduct(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 6")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [-2,0,-1]")
    nums2 = [-2,0,-1]
    solution2 = Solution()
    result2 = solution2.maxProduct(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [-2,3,-4]")
    nums3 = [-2,3,-4]
    solution3 = Solution()
    result3 = solution3.maxProduct(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 24")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [0,2]")
    nums4 = [0,2]
    solution4 = Solution()
    result4 = solution4.maxProduct(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
