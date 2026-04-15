"""
287. 寻找重复数
https://leetcode.cn/problems/find-the-duplicate-number/description/

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3 :
输入：nums = [3,3,3,3,3]
输出：3

提示：
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次

进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度、空间复杂度仅为常数级的解决方案吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def findDuplicate(self, nums: List[int]) -> int:
        """
        找出重复的数
        
        参数:
            nums: 整数数组
            
        返回:
            重复的数
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,3,4,2,2]")
    nums1 = [1, 3, 4, 2, 2]
    result1 = solution.findDuplicate(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 2")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [3,1,3,4,2]")
    nums2 = [3, 1, 3, 4, 2]
    result2 = solution.findDuplicate(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 3")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,1]")
    nums3 = [1, 1]
    result3 = solution.findDuplicate(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
