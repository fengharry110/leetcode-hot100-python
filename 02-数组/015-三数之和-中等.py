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
"""

from typing import List


class Solution:
    """
    双指针解法类
    
    解题思路：
        排序后使用双指针，固定一个数，然后在剩余部分找两数之和等于目标值
        
    算法步骤：
        1. 排序数组
        2. 遍历数组，固定当前元素nums[i]：
           - 如果nums[i] > 0，直接返回结果（因为排序后后面的数都大于0，和不可能为0）
           - 跳过重复的nums[i]
           - 初始化左右指针left = i+1, right = n-1
           - 当left < right时：
              * 计算三数之和sum = nums[i] + nums[left] + nums[right]
              * 如果sum == 0，添加到结果，跳过重复的left和right
              * 如果sum < 0，left++
              * 如果sum > 0，right--
        3. 返回结果
        
    时间复杂度：O(n²)
    空间复杂度：O(1) 或 O(n)（取决于排序算法）
    """
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有和为0的三元组
        
        参数:
            nums: 整数数组
            
        返回:
            所有不重复的三元组列表
        """
        n = len(nums)
        if n < 3:
            return []
        
        # 排序数组
        nums.sort()
        result = []
        
        for i in range(n):
            # 第一个数大于0，后面的数都大于0，和不可能为0
            if nums[i] > 0:
                break
            
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 双指针
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # 添加结果
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 跳过重复的right
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


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
    solution2 = Solution()
    result2 = solution2.threeSum(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: []")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0,0,0]")
    nums3 = [0, 0, 0]
    solution3 = Solution()
    result3 = solution3.threeSum(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[0,0,0]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [-2,0,0,2,2]")
    nums4 = [-2, 0, 0, 2, 2]
    solution4 = Solution()
    result4 = solution4.threeSum(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: [[-2,0,2]]")
