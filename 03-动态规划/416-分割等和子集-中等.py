"""
416. 分割等和子集
https://leetcode.cn/problems/partition-equal-subset-sum/description/

给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
"""

from typing import List


class Solution:
    """
    分割等和子集解法类
    
    解题思路：
        动态规划，转化为0-1背包问题
        
    算法步骤：
        1. 计算数组总和，如果总和为奇数，直接返回False
        2. 目标值为总和的一半
        3. 初始化dp数组，dp[i]表示是否可以组成和为i的子集
        4. 遍历数组，更新dp数组
        5. 返回dp[target]
        
    时间复杂度：O(n*target)
    空间复杂度：O(target)
    """
    
    def canPartition(self, nums: List[int]) -> bool:
        """
        判断是否可以分割等和子集
        
        参数:
            nums: 整数数组
            
        返回:
            是否可以分割
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,5,11,5]")
    nums1 = [1,5,11,5]
    solution = Solution()
    result1 = solution.canPartition(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: True")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [1,2,3,5]")
    nums2 = [1,2,3,5]
    solution2 = Solution()
    result2 = solution2.canPartition(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: False")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1,2,5]")
    nums3 = [1,2,5]
    solution3 = Solution()
    result3 = solution3.canPartition(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: False")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: nums = [1,2,3,4,5,6,7]")
    nums4 = [1,2,3,4,5,6,7]
    solution4 = Solution()
    result4 = solution4.canPartition(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: True")
