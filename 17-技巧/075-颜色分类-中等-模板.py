"""
75. 颜色分类
https://leetcode.cn/problems/sort-colors/description/

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

提示：
n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

进阶：你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def sortColors(self, nums: List[int]) -> None:
        """
        原地排序颜色数组
        
        参数:
            nums: 颜色数组
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: nums = [2,0,2,1,1,0]")
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(f"结果: {nums1}")
    print(f"期望结果: [0, 0, 1, 1, 2, 2]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: nums = [2,0,1]")
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    print(f"结果: {nums2}")
    print(f"期望结果: [0, 1, 2]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: nums = [0]")
    nums3 = [0]
    solution.sortColors(nums3)
    print(f"结果: {nums3}")
    print(f"期望结果: [0]")
