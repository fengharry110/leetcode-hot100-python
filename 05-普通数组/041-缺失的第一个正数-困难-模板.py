"""
41. 缺失的第一个正数
https://leetcode.cn/problems/first-missing-positive/description/

给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1

提示：
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

进阶：你能实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        找出数组中没有出现的最小正整数
        
        参数:
            nums: 未排序的整数数组
            
        返回:
            没有出现的最小正整数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,0]")
    nums1 = [1, 2, 0]
    solution = Solution()
    result1 = solution.firstMissingPositive(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,4,-1,1]")
    nums2 = [3, 4, -1, 1]
    result2 = solution.firstMissingPositive(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [7,8,9,11,12]")
    nums3 = [7, 8, 9, 11, 12]
    result3 = solution.firstMissingPositive(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,3]")
    nums4 = [1, 2, 3]
    result4 = solution.firstMissingPositive(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 4")
