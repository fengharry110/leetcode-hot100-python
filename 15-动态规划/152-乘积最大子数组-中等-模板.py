"""
152. 乘积最大子数组
https://leetcode.cn/problems/maximum-product-subarray/description/

给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

提示:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
nums 的任何前缀或后缀的乘积都 保证 是一个 32-位整数
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def maxProduct(self, nums: List[int]) -> int:
        """
        找出乘积最大的非空连续子数组
        
        参数:
            nums: 整数数组
            
        返回:
            最大乘积
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [2,3,-2,4]")
    nums1 = [2, 3, -2, 4]
    result1 = solution.maxProduct(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 6")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [-2,0,-1]")
    nums2 = [-2, 0, -1]
    result2 = solution.maxProduct(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [-2,3,-4]")
    nums3 = [-2, 3, -4]
    result3 = solution.maxProduct(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 24")
