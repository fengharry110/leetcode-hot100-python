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

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def search(self, nums: List[int], target: int) -> int:
        """
        在旋转排序数组中搜索目标值
        
        参数:
            nums: 旋转后的排序数组
            target: 目标值
            
        返回:
            目标值的下标，不存在则返回-1
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [4,5,6,7,0,1,2], target = 0")
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [4,5,6,7,0,1,2], target = 3")
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: -1")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1], target = 0")
    nums3 = [1]
    target3 = 0
    result3 = solution.search(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: -1")
