"""
169. 多数元素
https://leetcode.cn/problems/majority-element/description/

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def majorityElement(self, nums: List[int]) -> int:
        """
        找出多数元素
        
        参数:
            nums: 整数数组
            
        返回:
            多数元素
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [3,2,3]")
    nums1 = [3, 2, 3]
    result1 = solution.majorityElement(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [2,2,1,1,1,2,2]")
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = solution.majorityElement(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1]")
    nums3 = [1]
    result3 = solution.majorityElement(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
