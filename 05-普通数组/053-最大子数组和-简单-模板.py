"""
53. 最大子数组和
https://leetcode.cn/problems/maximum-subarray/description/

给你一个整数数组 nums，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23

提示：
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用分治法求解。
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        找出具有最大和的连续子数组
        
        参数:
            nums: 整数数组
            
        返回:
            最大子数组和
        """
        # TODO: 在此实现你的解法
        pass


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
    result2 = solution.maxSubArray(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [5,4,-1,7,8]")
    nums3 = [5, 4, -1, 7, 8]
    result3 = solution.maxSubArray(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 23")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [-1,-2,-3,-4]")
    nums4 = [-1, -2, -3, -4]
    result4 = solution.maxSubArray(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: -1")
