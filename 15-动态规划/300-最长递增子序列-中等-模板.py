"""
300. 最长递增子序列
https://leetcode.cn/problems/longest-increasing-subsequence/description/

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        找出最长严格递增子序列的长度
        
        参数:
            nums: 整数数组
            
        返回:
            最长递增子序列长度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [10,9,2,5,3,7,101,18]")
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result1 = solution.lengthOfLIS(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [0,1,0,3,2,3]")
    nums2 = [0, 1, 0, 3, 2, 3]
    result2 = solution.lengthOfLIS(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [7,7,7,7,7,7,7]")
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    result3 = solution.lengthOfLIS(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
