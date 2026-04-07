"""
300. 最长递增子序列
https://leetcode.cn/problems/longest-increasing-subsequence/description/

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
"""

from typing import List


class Solution:
    """
    最长递增子序列解法类
    
    解题思路：
        使用动态规划，dp[i]表示以nums[i]结尾的最长递增子序列长度
        
    算法步骤：
        1. 初始化dp数组，每个元素初始值为1
        2. 遍历数组，对于每个元素i：
           - 遍历之前的所有元素j：
               - 如果nums[i] > nums[j]，更新dp[i] = max(dp[i], dp[j] + 1)
        3. 返回dp数组中的最大值
        
    时间复杂度：O(n²)
    空间复杂度：O(n)
    """
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        计算最长递增子序列的长度
        
        参数:
            nums: 整数数组
            
        返回:
            最长递增子序列的长度
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


class SolutionBinarySearch:
    """
    二分查找优化解法类
    
    解题思路：
        使用贪心算法结合二分查找，维护一个递增序列
        
    算法步骤：
        1. 初始化一个空列表tail
        2. 遍历数组中的每个元素：
           - 如果元素大于tail的最后一个元素，添加到tail
           - 否则，使用二分查找找到第一个大于等于该元素的位置，替换为该元素
        3. 返回tail的长度
        
    时间复杂度：O(n log n)
    空间复杂度：O(n)
    """
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        计算最长递增子序列的长度（二分查找优化版本）
        
        参数:
            nums: 整数数组
            
        返回:
            最长递增子序列的长度
        """
        tail = []
        
        for num in nums:
            # 二分查找
            left, right = 0, len(tail)
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(tail):
                tail.append(num)
            else:
                tail[left] = num
        
        return len(tail)


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [10,9,2,5,3,7,101,18]")
    nums1 = [10,9,2,5,3,7,101,18]
    solution = Solution()
    result1 = solution.lengthOfLIS(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 4")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,1,0,3,2,3]")
    nums2 = [0,1,0,3,2,3]
    solution2 = SolutionBinarySearch()
    result2 = solution2.lengthOfLIS(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [7,7,7,7,7,7,7]")
    nums3 = [7,7,7,7,7,7,7]
    solution3 = Solution()
    result3 = solution3.lengthOfLIS(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [3,6,2,7]")
    nums4 = [3,6,2,7]
    solution4 = SolutionBinarySearch()
    result4 = solution4.lengthOfLIS(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: 3")
