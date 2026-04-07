"""
448. 找到所有数组中消失的数字
https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/description/

给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]
"""

from typing import List


class Solution:
    """
    找到所有数组中消失的数字解法类
    
    解题思路：
        原地标记，将出现的数字对应位置标记为负数
        
    算法步骤：
        1. 遍历数组，将每个数字对应位置标记为负数
        2. 再次遍历数组，收集所有正数的位置+1
        3. 返回结果
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        找到所有消失的数字
        
        参数:
            nums: 整数数组
            
        返回:
            消失的数字列表
        """
        n = len(nums)
        
        # 标记出现的数字
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # 收集消失的数字
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [4,3,2,7,8,2,3,1]")
    nums1 = [4,3,2,7,8,2,3,1]
    solution = Solution()
    result1 = solution.findDisappearedNumbers(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [5,6]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1,1]")
    nums2 = [1,1]
    solution2 = Solution()
    result2 = solution2.findDisappearedNumbers(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [2,2,3,3]")
    nums3 = [2,2,3,3]
    solution3 = Solution()
    result3 = solution3.findDisappearedNumbers(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [1,4]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [1,2,3,4,5]")
    nums4 = [1,2,3,4,5]
    solution4 = Solution()
    result4 = solution4.findDisappearedNumbers(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: []")
