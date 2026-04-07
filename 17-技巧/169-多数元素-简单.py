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
"""

from typing import List


class Solution:
    """
    多数元素解法类
    
    解题思路：
        使用哈希表统计元素出现的次数
        
    算法步骤：
        1. 遍历数组，统计每个元素出现的次数
        2. 遍历哈希表，返回出现次数大于n/2的元素
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def majorityElement(self, nums: List[int]) -> int:
        """
        找出多数元素
        
        参数:
            nums: 整数数组
            
        返回:
            多数元素
        """
        count = {}
        n = len(nums)
        
        # 统计元素出现的次数
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            # 提前返回
            if count[num] > n // 2:
                return num
        
        # 遍历哈希表
        for num, cnt in count.items():
            if cnt > n // 2:
                return num
        
        return -1


class SolutionMooreVoting:
    """
    摩尔投票法解法类
    
    解题思路：
        使用摩尔投票算法，抵消不同元素
        
    算法步骤：
        1. 初始化候选元素和计数
        2. 遍历数组：
           - 如果计数为0，更新候选元素
           - 如果当前元素等于候选元素，计数+1
           - 否则，计数-1
        3. 返回候选元素
        
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    
    def majorityElement(self, nums: List[int]) -> int:
        """
        找出多数元素（摩尔投票法）
        
        参数:
            nums: 整数数组
            
        返回:
            多数元素
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [3,2,3]")
    nums1 = [3,2,3]
    solution = Solution()
    result1 = solution.majorityElement(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [2,2,1,1,1,2,2]")
    nums2 = [2,2,1,1,1,2,2]
    solution2 = SolutionMooreVoting()
    result2 = solution2.majorityElement(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1]")
    nums3 = [1]
    solution3 = Solution()
    result3 = solution3.majorityElement(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,1,1,2,2,2,2]")
    nums4 = [1,1,1,2,2,2,2]
    solution4 = SolutionMooreVoting()
    result4 = solution4.majorityElement(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 2")
