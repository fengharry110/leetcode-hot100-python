"""
78. 子集
https://leetcode.cn/problems/subsets/description/

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        返回数组所有可能的子集
        
        参数:
            nums: 互不相同的整数数组
            
        返回:
            所有可能的子集
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,2,3]")
    nums1 = [1, 2, 3]
    result1 = solution.subsets(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [0]")
    nums2 = [0]
    result2 = solution.subsets(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [[],[0]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,2]")
    nums3 = [1, 2]
    result3 = solution.subsets(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[],[1],[2],[1,2]]")
