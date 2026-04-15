"""
31. 下一个排列
https://leetcode.cn/problems/next-permutation/description/

整数数组的一个 排列  就是其所有整数按某种顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
arr = [3,2,1] 的下一个排列是 [1,2,3] 。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        将nums修改为下一个排列，原地修改
        
        参数:
            nums: 整数数组
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,2,3]")
    nums1 = [1, 2, 3]
    solution.nextPermutation(nums1)
    print(f"结果: {nums1}")
    print(f"期望结果: [1, 3, 2]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [3,2,1]")
    nums2 = [3, 2, 1]
    solution.nextPermutation(nums2)
    print(f"结果: {nums2}")
    print(f"期望结果: [1, 2, 3]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,1,5]")
    nums3 = [1, 1, 5]
    solution.nextPermutation(nums3)
    print(f"结果: {nums3}")
    print(f"期望结果: [1, 5, 1]")
