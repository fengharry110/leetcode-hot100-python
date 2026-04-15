"""
136. 只出现一次的数字
https://leetcode.cn/problems/single-number/description/

给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

示例 1 ：
输入：nums = [2,2,1]
输出：1

示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4

示例 3 ：
输入：nums = [1]
输出：1

提示：
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
除了某个元素只出现一次以外，其余每个元素均出现两次。
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def singleNumber(self, nums: List[int]) -> int:
        """
        找出只出现一次的元素
        
        参数:
            nums: 整数数组
            
        返回:
            只出现一次的元素
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [2,2,1]")
    nums1 = [2, 2, 1]
    result1 = solution.singleNumber(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: 1")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [4,1,2,1,2]")
    nums2 = [4, 1, 2, 1, 2]
    result2 = solution.singleNumber(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [1]")
    nums3 = [1]
    result3 = solution.singleNumber(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
