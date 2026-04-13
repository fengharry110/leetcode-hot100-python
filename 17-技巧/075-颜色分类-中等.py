"""
75. 颜色分类
中等
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

提示：
n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

进阶：你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 荷兰国旗问题：三指针
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [2, 0, 2, 1, 1, 0]
    print(f"输入: nums = {nums1}")
    solution.sortColors(nums1)
    print(f"输出: {nums1}")
    
    # 测试用例2
    nums2 = [2, 0, 1]
    print(f"\n输入: nums = {nums2}")
    solution.sortColors(nums2)
    print(f"输出: {nums2}")
