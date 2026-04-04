"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/description/

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""

from typing import List


class Solution:
    """
    哈希表解法类
    
    解题思路：
        使用哈希表存储所有元素，然后遍历每个元素，当找到序列的起始元素时（即当前元素-1不在哈希表中），开始计算连续序列的长度
        
    算法步骤：
        1. 将所有元素存入哈希表
        2. 遍历哈希表中的每个元素：
           - 如果 current - 1 不在哈希表中，说明这是一个序列的起始元素
           - 从当前元素开始，依次检查 current+1, current+2, ... 是否在哈希表中
           - 计算当前序列的长度，并更新最长长度
        3. 返回最长序列长度
        
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        找出最长连续序列的长度
        
        参数:
            nums: 未排序的整数数组
            
        返回:
            最长连续序列的长度
        """
        if not nums:
            return 0
        
        # 构建哈希表，用于快速查找
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # 只有当num-1不在集合中时，才开始计算连续序列
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # 不断检查current_num + 1是否在集合中
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # 更新最长长度
                max_length = max(max_length, current_length)
        
        return max_length


class SolutionSort:
    """
    排序解法类
    
    解题思路：
        先排序数组，然后遍历数组计算连续序列的长度
        
    算法步骤：
        1. 排序数组
        2. 遍历排序后的数组：
           - 如果当前元素等于前一个元素+1，长度+1
           - 如果当前元素等于前一个元素，跳过
           - 否则，重置长度为1
           - 更新最长长度
        3. 返回最长长度
        
    时间复杂度：O(n log n)
    空间复杂度：O(1) 或 O(n)（取决于排序算法）
    """
    
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        排序解法找出最长连续序列
        
        参数:
            nums: 未排序的整数数组
            
        返回:
            最长连续序列的长度
        """
        if not nums:
            return 0
        
        # 排序数组
        nums.sort()
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # 如果当前元素与前一个元素连续
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            # 如果当前元素与前一个元素相同，跳过
            elif nums[i] != nums[i-1]:
                # 重置长度
                current_length = 1
            
            # 更新最长长度
            max_length = max(max_length, current_length)
        
        return max_length


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [100,4,200,1,3,2]")
    nums1 = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result1 = solution.longestConsecutive(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,3,7,2,5,8,4,6,0,1]")
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    solution2 = SolutionSort()
    result2 = solution2.longestConsecutive(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 9")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: []")
    nums3 = []
    solution3 = Solution()
    result3 = solution3.longestConsecutive(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,0,1]")
    nums4 = [1, 2, 0, 1]
    solution4 = Solution()
    result4 = solution4.longestConsecutive(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 3")
