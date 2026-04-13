"""
238. 除自身以外数组的乘积
https://leetcode.cn/problems/product-of-array-except-self/description/

给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
题目数据保证数组 nums 之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]

提示：
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- 保证数组 nums 之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内

进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（输出数组不被视为额外空间）
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        返回除自身以外数组的乘积
        
        参数:
            nums: 整数数组
            
        返回:
            结果数组
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3,4]")
    nums1 = [1, 2, 3, 4]
    solution = Solution()
    result1 = solution.productExceptSelf(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [24,12,8,6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [-1,1,0,-3,3]")
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [0,0,9,0,0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [2,3,4,5]")
    nums3 = [2, 3, 4, 5]
    result3 = solution.productExceptSelf(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [60,40,30,24]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2]")
    nums4 = [1, 2]
    result4 = solution.productExceptSelf(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: [2,1]")
