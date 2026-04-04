"""
4. 寻找两个正序数组的中位数
https://leetcode.cn/problems/median-of-two-sorted-arrays/description/

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数是 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数是 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
"""

from typing import List


class Solution:
    """
    二分查找解法类
    
    解题思路：
        利用二分查找找到两个数组的分割点，使得左半部分的元素个数等于右半部分
        确保左边的所有元素都小于等于右边的所有元素
        
    算法步骤：
        1. 确保nums1是较短的数组，以减少搜索空间
        2. 初始化二分查找的左右边界
        3. 循环直到找到正确的分割点：
           - 计算nums1的分割点i和nums2的分割点j
           - 计算左边的最大值和右边的最小值
           - 根据比较结果调整分割点
        4. 根据总元素个数的奇偶性计算中位数
        
    时间复杂度：O(log(min(m, n)))
    空间复杂度：O(1)
    """
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        寻找两个正序数组的中位数
        
        参数:
            nums1: 第一个正序数组
            nums2: 第二个正序数组
            
        返回:
            中位数
        """
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left < right:
            i = (left + right) // 2
            j = half_len - i
            
            # 如果nums1的分割点右边的元素小于nums2的分割点左边的元素，需要右移分割点
            if nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i
        
        i, j = left, half_len - left
        
        # 计算左边的最大值
        if i == 0:
            max_left = nums2[j-1]
        elif j == 0:
            max_left = nums1[i-1]
        else:
            max_left = max(nums1[i-1], nums2[j-1])
        
        # 如果总长度是奇数，直接返回左边的最大值
        if (m + n) % 2 == 1:
            return max_left
        
        # 计算右边的最小值
        if i == m:
            min_right = nums2[j]
        elif j == n:
            min_right = nums1[i]
        else:
            min_right = min(nums1[i], nums2[j])
        
        # 总长度是偶数，返回平均值
        return (max_left + min_right) / 2


class SolutionMerge:
    """
    合并解法类
    
    解题思路：
        合并两个数组，然后找到中位数
        
    算法步骤：
        1. 合并两个有序数组
        2. 计算中位数的位置
        3. 根据总长度的奇偶性返回中位数
        
    时间复杂度：O(m + n)
    空间复杂度：O(m + n)
    """
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        通过合并数组找到中位数
        
        参数:
            nums1: 第一个正序数组
            nums2: 第二个正序数组
            
        返回:
            中位数
        """
        merged = []
        i = j = 0
        m, n = len(nums1), len(nums2)
        
        # 合并两个有序数组
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # 处理剩余元素
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        total_len = m + n
        if total_len % 2 == 1:
            return merged[total_len // 2]
        else:
            mid = total_len // 2
            return (merged[mid - 1] + merged[mid]) / 2


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,3] + [2]")
    nums1_1 = [1, 3]
    nums2_1 = [2]
    solution = Solution()
    result1 = solution.findMedianSortedArrays(nums1_1, nums2_1)
    print(f"结果: {result1}")
    print(f"期望结果: 2.0")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [1,2] + [3,4]")
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    solution2 = SolutionMerge()
    result2 = solution2.findMedianSortedArrays(nums1_2, nums2_2)
    print(f"结果: {result2}")
    print(f"期望结果: 2.5")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0,0] + [0,0]")
    nums1_3 = [0, 0]
    nums2_3 = [0, 0]
    solution3 = Solution()
    result3 = solution3.findMedianSortedArrays(nums1_3, nums2_3)
    print(f"结果: {result3}")
    print(f"期望结果: 0.0")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [] + [1]")
    nums1_4 = []
    nums2_4 = [1]
    solution4 = Solution()
    result4 = solution4.findMedianSortedArrays(nums1_4, nums2_4)
    print(f"结果: {result4}")
    print(f"期望结果: 1.0")
    
    # 测试用例5
    print("\n" + "=" * 50)
    print("测试用例5: [2] + []")
    nums1_5 = [2]
    nums2_5 = []
    solution5 = SolutionMerge()
    result5 = solution5.findMedianSortedArrays(nums1_5, nums2_5)
    print(f"结果: {result5}")
    print(f"期望结果: 2.0")
