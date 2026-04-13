# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
#
# 示例 1:
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
# 示例 2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.searchInsert([1, 3, 5, 6], 5)}")  # 期望输出: 2
    
    # 测试2
    print(f"测试2结果: {solution.searchInsert([1, 3, 5, 6], 2)}")  # 期望输出: 1
    
    # 测试3
    print(f"测试3结果: {solution.searchInsert([1, 3, 5, 6], 7)}")  # 期望输出: 4
