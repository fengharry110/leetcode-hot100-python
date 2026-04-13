"""
15. 三数之和
https://leetcode.cn/problems/3sum/description/

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = [0,1,1]
输出：[]

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]

提示：
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有和为0的三元组
        
        参数:
            nums: 整数数组
            
        返回:
            所有不重复的三元组列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [-1,0,1,2,-1,-4]")
    nums1 = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result1 = solution.threeSum(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [[-1,-1,2],[-1,0,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,1,1]")
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0,0,0]")
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[0,0,0]]")
