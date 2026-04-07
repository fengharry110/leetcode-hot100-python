"""
33. 搜索旋转排序数组
https://leetcode.cn/problems/search-in-rotated-sorted-array/description/

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1
"""

from typing import List


class Solution:
    """
    搜索旋转排序数组解法类
    
    解题思路：
        使用二分查找，根据中间元素与左右边界的关系判断哪一部分是有序的
        
    算法步骤：
        1. 初始化左指针为0，右指针为数组长度-1
        2. 当左<=右时：
           - 计算中间位置mid
           - 如果nums[mid] == target，返回mid
           - 如果nums[left] <= nums[mid]，说明左半部分有序：
               - 如果target在左半部分，更新右指针
               - 否则，更新左指针
           - 否则，说明右半部分有序：
               - 如果target在右半部分，更新左指针
               - 否则，更新右指针
        3. 返回-1
        
    时间复杂度：O(log n)
    空间复杂度：O(1)
    """
    
    def search(self, nums: List[int], target: int) -> int:
        """
        搜索旋转排序数组
        
        参数:
            nums: 旋转排序数组
            target: 目标值
            
        返回:
            目标值的下标，不存在返回-1
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 判断哪一部分是有序的
            if nums[left] <= nums[mid]:
                # 左半部分有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [4,5,6,7,0,1,2], target = 0")
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    solution = Solution()
    result1 = solution.search(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [4,5,6,7,0,1,2], target = 3")
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    solution2 = Solution()
    result2 = solution2.search(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1], target = 0")
    nums3 = [1]
    target3 = 0
    solution3 = Solution()
    result3 = solution3.search(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: -1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [5,1,3], target = 5")
    nums4 = [5,1,3]
    target4 = 5
    solution4 = Solution()
    result4 = solution4.search(nums4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: 0")
