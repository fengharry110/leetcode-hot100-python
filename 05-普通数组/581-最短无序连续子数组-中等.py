"""
581. 最短无序连续子数组
中等
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0

示例 3：
输入：nums = [1]
输出：0

提示：
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 从左到右找右边界
        max_val = nums[0]
        right = 0
        for i in range(n):
            if nums[i] < max_val:
                right = i
            else:
                max_val = nums[i]
        
        # 从右到左找左边界
        min_val = nums[-1]
        left = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] > min_val:
                left = i
            else:
                min_val = nums[i]
        
        return right - left + 1 if right > left else 0


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [2, 6, 4, 8, 10, 9, 15]
    print(f"输入: nums = {nums1}")
    print(f"输出: {solution.findUnsortedSubarray(nums1)}")
    
    # 测试用例2
    nums2 = [1, 2, 3, 4]
    print(f"\n输入: nums = {nums2}")
    print(f"输出: {solution.findUnsortedSubarray(nums2)}")
    
    # 测试用例3
    nums3 = [1]
    print(f"\n输入: nums = {nums3}")
    print(f"输出: {solution.findUnsortedSubarray(nums3)}")
