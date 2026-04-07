"""
238. 除自身以外数组的乘积
https://leetcode.cn/problems/product-of-array-except-self/description/

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""

from typing import List


class Solution:
    """
    除自身以外数组的乘积解法类
    
    解题思路：
        使用左右乘积数组，分别计算左边和右边的乘积
        
    算法步骤：
        1. 初始化左乘积数组left，left[0] = 1
        2. 计算left数组，left[i] = left[i-1] * nums[i-1]
        3. 初始化右乘积数组right，right[-1] = 1
        4. 计算right数组，right[i] = right[i+1] * nums[i+1]
        5. 计算结果数组，answer[i] = left[i] * right[i]
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        计算除自身以外数组的乘积
        
        参数:
            nums: 整数数组
            
        返回:
            结果数组
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n
        
        # 计算左乘积
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # 计算右乘积
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # 计算结果
        for i in range(n):
            answer[i] = left[i] * right[i]
        
        return answer


class SolutionOptimized:
    """
    空间优化解法类
    
    解题思路：
        使用结果数组来存储左乘积，然后计算右乘积并更新结果
        
    算法步骤：
        1. 初始化结果数组answer，answer[0] = 1
        2. 计算左乘积，存储在answer中
        3. 初始化右乘积变量为1
        4. 从右往左遍历，计算右乘积并更新结果
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        计算除自身以外数组的乘积（空间优化版本）
        
        参数:
            nums: 整数数组
            
        返回:
            结果数组
        """
        n = len(nums)
        answer = [1] * n
        
        # 计算左乘积
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # 计算右乘积并更新结果
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3,4]")
    nums1 = [1,2,3,4]
    solution = Solution()
    result1 = solution.productExceptSelf(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [24,12,8,6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [-1,1,0,-3,3]")
    nums2 = [-1,1,0,-3,3]
    solution2 = SolutionOptimized()
    result2 = solution2.productExceptSelf(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [0,0,9,0,0]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [2,3,4,5]")
    nums3 = [2,3,4,5]
    solution3 = Solution()
    result3 = solution3.productExceptSelf(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [60,40,30,24]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2]")
    nums4 = [1,2]
    solution4 = SolutionOptimized()
    result4 = solution4.productExceptSelf(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: [2,1]")
