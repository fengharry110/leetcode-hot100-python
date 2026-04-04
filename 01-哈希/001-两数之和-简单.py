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
"""

from typing import List


class Solution:
    """
    哈希表解法类
    
    解题思路：
        使用哈希表存储已经遍历过的元素及其索引，对于当前元素，检查target - current是否在哈希表中
        
    算法步骤：
        1. 初始化一个哈希表
        2. 遍历数组：
           - 计算 complement = target - nums[i]
           - 如果 complement 在哈希表中，返回 [哈希表[complement], i]
           - 否则，将当前元素及其索引存入哈希表
        3. 若没有找到，返回空列表（题目保证有解）
        
    时间复杂度：O(n)
    空间复杂度：O(n)
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
        # 创建哈希表，键为元素值，值为索引
        num_map = {}
        
        for i, num in enumerate(nums):
            # 计算需要的补数
            complement = target - num
            
            # 如果补数在哈希表中，返回结果
            if complement in num_map:
                return [num_map[complement], i]
            
            # 将当前元素加入哈希表
            num_map[num] = i
        
        # 题目保证有解，所以不会执行到这里
        return []


class SolutionBruteForce:
    """
    暴力解法类
    
    解题思路：
        双重循环遍历所有可能的元素对，检查和是否为目标值
        
    算法步骤：
        1. 外层循环遍历每个元素
        2. 内层循环遍历当前元素之后的元素
        3. 检查两个元素的和是否为target
        4. 如果找到，返回索引
        
    时间复杂度：O(n²)
    空间复杂度：O(1)
    """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力解法找到两数之和
        
        参数:
            nums: 整数数组
            target: 目标值
            
        返回:
            两个元素的索引列表
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


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
    solution2 = SolutionBruteForce()
    result2 = solution2.twoSum(nums2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: [1, 2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [3,3], target=6")
    nums3 = [3, 3]
    target3 = 6
    solution3 = Solution()
    result3 = solution3.twoSum(nums3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: [0, 1]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [0,4,3,0], target=0")
    nums4 = [0, 4, 3, 0]
    target4 = 0
    solution4 = Solution()
    result4 = solution4.twoSum(nums4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: [0, 3]")
