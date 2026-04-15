"""
35. 搜索插入位置
https://leetcode.cn/problems/search-insert-position/description/

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

提示:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 为 无重复元素 的 升序 排列数组
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        在排序数组中找到目标值的索引或插入位置
        
        参数:
            nums: 排序数组
            target: 目标值
            
        返回:
            目标值的索引或应该插入的位置
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,3,5,6], target = 5")
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = solution.searchInsert(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1,3,5,6], target = 2")
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = solution.searchInsert(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: 1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,3,5,6], target = 7")
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = solution.searchInsert(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: 4")
