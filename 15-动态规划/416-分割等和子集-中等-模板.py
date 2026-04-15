"""
416. 分割等和子集
https://leetcode.cn/problems/partition-equal-subset-sum/description/

给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def canPartition(self, nums: List[int]) -> bool:
        """
        判断是否可以将数组分割成两个和相等的子集
        
        参数:
            nums: 正整数数组
            
        返回:
            是否可以分割
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,5,11,5]")
    nums1 = [1, 5, 11, 5]
    result1 = solution.canPartition(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1,2,3,5]")
    nums2 = [1, 2, 3, 5]
    result2 = solution.canPartition(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,1]")
    nums3 = [1, 1]
    result3 = solution.canPartition(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: True")
