"""
1. 两数之和
https://leetcode.cn/problems/two-sum/description/

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        找到数组中和为目标值的两个元素的索引
        
        参数:
            nums: 整数数组
            target: 目标值
            
        返回:
            两个元素的索引列表
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [2,7,11,15], target=9")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    solution = Solution()
    result1 = solution.twoSum(nums1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: [0, 1]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,2,4], target=6")
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: [1, 2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [3,3], target=6")
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: [0, 1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [0,4,3,0], target=0")
    nums4 = [0, 4, 3, 0]
    target4 = 0
    result4 = solution.twoSum(nums4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: [0, 3]")
