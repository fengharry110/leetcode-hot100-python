# 88. 合并两个有序数组
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        合并两个有序数组到nums1中
        方法：双指针从后往前遍历
        时间复杂度：O(m + n)，其中m和n分别是nums1和nums2的长度
        空间复杂度：O(1)，只使用常数级额外空间
        """
        # 初始化三个指针：
        # p1指向nums1的最后一个有效元素
        # p2指向nums2的最后一个元素
        # p指向nums1的最后一个位置
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # 从后往前遍历，将较大的元素放到nums1的末尾
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # 处理nums2中剩余的元素
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        
        # 无需处理nums1中剩余的元素，因为它们已经在正确的位置
        return nums1


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print("测试用例1:")
    print("输入: nums1 =", [1, 2, 3, 0, 0, 0], "m =", m, "nums2 =", [2, 5, 6], "n =", n)
    solution.merge(nums1, m, nums2, n)
    print("输出:", nums1)
    print()
    
    # 测试用例2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print("测试用例2:")
    print("输入: nums1 =", [1], "m =", m, "nums2 =", [], "n =", n)
    solution.merge(nums1, m, nums2, n)
    print("输出:", nums1)
    print()
    
    # 测试用例3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print("测试用例3:")
    print("输入: nums1 =", [0], "m =", m, "nums2 =", [1], "n =", n)
    solution.merge(nums1, m, nums2, n)
    print("输出:", nums1)
    print()
    
    # 测试用例4
    nums1 = [1, 3, 5, 0, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6, 7]
    n = 4
    print("测试用例4:")
    print("输入: nums1 =", [1, 3, 5, 0, 0, 0, 0], "m =", m, "nums2 =", [2, 4, 6, 7], "n =", n)
    solution.merge(nums1, m, nums2, n)
    print("输出:", nums1)