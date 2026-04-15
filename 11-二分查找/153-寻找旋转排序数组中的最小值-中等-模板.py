"""
153. 寻找旋转排序数组中的最小值
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/

已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

示例 2：
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,3,4,5,6,7] ，旋转 4 次得到输入数组。

示例 3：
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。

提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def findMin(self, nums: List[int]) -> int:
        """
        找出旋转排序数组中的最小值
        
        参数:
            nums: 旋转后的排序数组
            
        返回:
            数组中的最小值
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [3,4,5,1,2]")
    nums1 = [3, 4, 5, 1, 2]
    result1 = solution.findMin(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 1")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [4,5,6,7,0,1,2]")
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    result2 = solution.findMin(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 0")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [11,13,15,17]")
    nums3 = [11, 13, 15, 17]
    result3 = solution.findMin(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 11")
