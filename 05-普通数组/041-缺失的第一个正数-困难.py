"""
41. 缺失的第一个正数
https://leetcode.cn/problems/first-missing-positive/description/

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

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
"""

from typing import List


class Solution:
    """
    缺失的第一个正数解法类
    
    解题思路：
        将数组视为哈希表，将每个正数放到对应的位置
        
    算法步骤：
        1. 遍历数组，将每个正数放到对应的位置（如果在1到n之间）
        2. 再次遍历数组，找到第一个位置上的数不等于索引+1的位置
        3. 返回该位置+1，否则返回n+1
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        寻找缺失的第一个正数
        
        参数:
            nums: 整数数组
            
        返回:
            缺失的第一个正数
        """
        n = len(nums)
        
        # 将每个正数放到对应的位置
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换位置
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # 找到第一个缺失的正数
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 如果所有位置都正确，返回n+1
        return n + 1


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,0]")
    nums1 = [1,2,0]
    solution = Solution()
    result1 = solution.firstMissingPositive(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,4,-1,1]")
    nums2 = [3,4,-1,1]
    solution2 = Solution()
    result2 = solution2.firstMissingPositive(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [7,8,9,11,12]")
    nums3 = [7,8,9,11,12]
    solution3 = Solution()
    result3 = solution3.firstMissingPositive(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,3,4,5]")
    nums4 = [1,2,3,4,5]
    solution4 = Solution()
    result4 = solution4.firstMissingPositive(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 6")
