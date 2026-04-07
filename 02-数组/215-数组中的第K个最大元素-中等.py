"""
215. 数组中的第K个最大元素
https://leetcode.cn/problems/kth-largest-element-in-an-array/description/

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""

from typing import List
import heapq


class Solution:
    """
    数组中的第K个最大元素解法类
    
    解题思路：
        使用最小堆，维护一个大小为k的最小堆
        
    算法步骤：
        1. 初始化一个最小堆
        2. 遍历数组，将元素加入堆中
        3. 当堆的大小超过k时，弹出堆顶元素
        4. 遍历结束后，堆顶元素即为第k个最大元素
        
    时间复杂度：O(n log k)
    空间复杂度：O(k)
    """
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        寻找数组中的第K个最大元素
        
        参数:
            nums: 整数数组
            k: 第k个最大元素
            
        返回:
            第k个最大元素
        """
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            # 保持堆的大小为k
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]


class SolutionQuickSelect:
    """
    快速选择解法类
    
    解题思路：
        使用快速选择算法，基于快速排序的思想
        
    算法步骤：
        1. 选择一个 pivot
        2. 将数组分为两部分，左边大于pivot，右边小于pivot
        3. 根据pivot的位置与k的关系，决定在左半部分还是右半部分继续查找
        4. 重复直到找到第k个最大元素
        
    时间复杂度：O(n) 平均情况，O(n²) 最坏情况
    空间复杂度：O(log n)
    """
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        寻找数组中的第K个最大元素（快速选择版本）
        
        参数:
            nums: 整数数组
            k: 第k个最大元素
            
        返回:
            第k个最大元素
        """
        def quick_select(left, right):
            """
            快速选择函数
            """
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            
            if i == k - 1:
                return nums[i]
            elif i < k - 1:
                return quick_select(i + 1, right)
            else:
                return quick_select(left, i - 1)
        
        return quick_select(0, len(nums) - 1)


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [3,2,1,5,6,4], k = 2")
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    solution = Solution()
    result1 = solution.findKthLargest(nums1, k1)
    print(f"结果: {result1}")
    print(f"期望结果: 5")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,2,3,1,2,4,5,5,6], k = 4")
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    solution2 = SolutionQuickSelect()
    result2 = solution2.findKthLargest(nums2, k2)
    print(f"结果: {result2}")
    print(f"期望结果: 4")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1], k = 1")
    nums3 = [1]
    k3 = 1
    solution3 = Solution()
    result3 = solution3.findKthLargest(nums3, k3)
    print(f"结果: {result3}")
    print(f"期望结果: 1")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [7,6,5,4,3,2,1], k = 3")
    nums4 = [7,6,5,4,3,2,1]
    k4 = 3
    solution4 = SolutionQuickSelect()
    result4 = solution4.findKthLargest(nums4, k4)
    print(f"结果: {result4}")
    print(f"期望结果: 5")
