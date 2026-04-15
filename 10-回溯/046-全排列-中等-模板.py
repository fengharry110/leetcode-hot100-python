"""
46. 全排列
https://leetcode.cn/problems/permutations/description/

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        返回数组的所有全排列
        
        参数:
            nums: 不含重复数字的数组
            
        返回:
            所有可能的全排列
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [1,2,3]")
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [0,1]")
    nums2 = [0, 1]
    result2 = solution.permute(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [[0,1],[1,0]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1]")
    nums3 = [1]
    result3 = solution.permute(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1]]")
