"""
78. 子集
https://leetcode.cn/problems/subsets/description/

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]
"""

from typing import List


class Solution:
    """
    子集解法类
    
    解题思路：
        使用回溯算法，递归生成所有子集
        
    算法步骤：
        1. 定义回溯函数，参数为当前路径和当前索引
        2. 将当前路径加入结果
        3. 从当前索引开始遍历数组：
           - 选择元素，将其加入路径
           - 递归调用回溯函数，索引+1
           - 撤销选择，将元素从路径中移除
        4. 返回结果
        
    时间复杂度：O(2^n)
    空间复杂度：O(n)
    """
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        生成所有子集
        
        参数:
            nums: 整数数组
            
        返回:
            所有可能的子集
        """
        result = []
        n = len(nums)
        
        def backtrack(path, start):
            """
            回溯函数
            
            参数:
                path: 当前路径
                start: 当前索引
            """
            # 将当前路径加入结果
            result.append(path[:])
            
            # 从当前索引开始遍历
            for i in range(start, n):
                # 选择元素
                path.append(nums[i])
                # 递归
                backtrack(path, i + 1)
                # 撤销选择
                path.pop()
        
        backtrack([], 0)
        return result


class SolutionBitmask:
    """
    位掩码解法类
    
    解题思路：
        使用位掩码，每个元素对应一个二进制位
        
    算法步骤：
        1. 计算子集总数：2^n
        2. 遍历每个可能的位掩码
        3. 根据位掩码生成对应的子集
        4. 返回结果
        
    时间复杂度：O(n * 2^n)
    空间复杂度：O(n)
    """
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        生成所有子集（位掩码版本）
        
        参数:
            nums: 整数数组
            
        返回:
            所有可能的子集
        """
        result = []
        n = len(nums)
        total = 1 << n  # 2^n
        
        for mask in range(total):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3]")
    nums1 = [1, 2, 3]
    solution = Solution()
    result1 = solution.subsets(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0]")
    nums2 = [0]
    solution2 = SolutionBitmask()
    result2 = solution2.subsets(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [[],[0]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1,2]")
    nums3 = [1, 2]
    solution3 = Solution()
    result3 = solution3.subsets(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[],[1],[2],[1,2]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [4,5,6]")
    nums4 = [4, 5, 6]
    solution4 = SolutionBitmask()
    result4 = solution4.subsets(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: [[],[4],[5],[4,5],[6],[4,6],[5,6],[4,5,6]]")
