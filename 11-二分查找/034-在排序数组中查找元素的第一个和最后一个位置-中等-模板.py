"""
34. 在排序数组中查找元素的第一个和最后一个位置
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        找出目标值在数组中的开始和结束位置
        
        参数:
            nums: 非递减顺序排列的整数数组
            target: 目标值
            
        返回:
            [开始位置, 结束位置]，不存在则返回 [-1, -1]
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [5,7,7,8,8,10], target = 8")
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: [3, 4]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [5,7,7,8,8,10], target = 6")
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: [-1, -1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [], target = 0")
    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: [-1, -1]")
