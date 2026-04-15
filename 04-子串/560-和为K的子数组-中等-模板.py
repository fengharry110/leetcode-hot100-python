"""
560. 和为 K 的子数组
中等
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2

提示：
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    请在此处实现你的解法
    """
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        统计数组中和为 k 的子数组的个数
        
        参数:
            nums: 整数数组
            k: 目标和
            
        返回:
            和为 k 的子数组的个数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1, 1, 1]
    k1 = 2
    print("=" * 50)
    print(f"输入: nums = {nums1}, k = {k1}")
    print(f"输出: {solution.subarraySum(nums1, k1)}")
    print(f"期望输出: 2")
    
    # 测试用例2
    nums2 = [1, 2, 3]
    k2 = 3
    print("\n" + "=" * 50)
    print(f"输入: nums = {nums2}, k = {k2}")
    print(f"输出: {solution.subarraySum(nums2, k2)}")
    print(f"期望输出: 2")
