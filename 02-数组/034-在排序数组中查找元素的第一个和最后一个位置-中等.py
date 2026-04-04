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
"""

from typing import List


class Solution:
    """
    二分查找解法类
    
    解题思路：
        使用两次二分查找，分别找到左边界和右边界
        
    算法步骤：
        1. 第一次二分查找，找到左边界：
           - 当nums[mid] >= target时，收缩右边界
        2. 第二次二分查找，找到右边界：
           - 当nums[mid] <= target时，收缩左边界
        3. 验证找到的边界是否有效
        
    时间复杂度：O(log n)
    空间复杂度：O(1)
    """
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        查找目标值的第一个和最后一个位置
        
        参数:
            nums: 非递减排列的整数数组
            target: 目标值
            
        返回:
            目标值的开始位置和结束位置，不存在则返回[-1, -1]
        """
        # 查找左边界
        left = self._findLeft(nums, target)
        # 查找右边界
        right = self._findRight(nums, target)
        
        # 验证边界是否有效
        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]
    
    def _findLeft(self, nums: List[int], target: int) -> int:
        """
        查找左边界
        
        参数:
            nums: 数组
            target: 目标值
            
        返回:
            左边界索引
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def _findRight(self, nums: List[int], target: int) -> int:
        """
        查找右边界
        
        参数:
            nums: 数组
            target: 目标值
            
        返回:
            右边界索引
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [5,7,7,8,8,10], target=8")
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    solution = Solution()
    result1 = solution.searchRange(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: [3,4]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [5,7,7,8,8,10], target=6")
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    solution2 = Solution()
    result2 = solution2.searchRange(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: [-1,-1]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [], target=0")
    nums3 = []
    target3 = 0
    solution3 = Solution()
    result3 = solution3.searchRange(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: [-1,-1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1], target=1")
    nums4 = [1]
    target4 = 1
    solution4 = Solution()
    result4 = solution4.searchRange(nums4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: [0,0]")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: [1,2,3,3,3,3,4,5,9], target=3")
    nums5 = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    target5 = 3
    solution5 = Solution()
    result5 = solution5.searchRange(nums5, target5)
    print(f"结果: {result5}")
    print(f"期望结果: [2,5]")
