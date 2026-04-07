"""
704. 二分查找
https://leetcode.cn/problems/binary-search/description/

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
"""

from typing import List


class Solution:
    """
    二分查找解法类
    
    解题思路：
        标准二分查找算法
        
    算法步骤：
        1. 初始化左右指针
        2. 当左指针小于等于右指针时：
           - 计算中间位置
           - 如果中间元素等于目标值，返回下标
           - 如果中间元素小于目标值，左指针右移
           - 否则，右指针左移
        3. 返回-1
        
    时间复杂度：O(logn)
    空间复杂度：O(1)
    """
    
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找
        
        参数:
            nums: 有序数组
            target: 目标值
            
        返回:
            目标值的下标，或-1
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [-1,0,3,5,9,12], target = 9")
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    solution = Solution()
    result1 = solution.search(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [-1,0,3,5,9,12], target = 2")
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    solution2 = Solution()
    result2 = solution2.search(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [5], target = 5")
    nums3 = [5]
    target3 = 5
    solution3 = Solution()
    result3 = solution3.search(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [5], target = 6")
    nums4 = [5]
    target4 = 6
    solution4 = Solution()
    result4 = solution4.search(nums4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: -1")
