# 136. 只出现一次的数字
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。


class Solution:
    def singleNumber(self, nums):
        """
        找出只出现一次的数字
        方法1：异或操作
        时间复杂度：O(n)，其中n是数组的长度
        空间复杂度：O(1)，只使用常数级额外空间
        思路：利用异或的性质：a ^ a = 0，a ^ 0 = a，异或操作满足交换律和结合律
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    
    def singleNumberHash(self, nums):
        """
        找出只出现一次的数字
        方法2：哈希表
        时间复杂度：O(n)，其中n是数组的长度
        空间复杂度：O(n)，哈希表的空间
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num, freq in count.items():
            if freq == 1:
                return num
        return -1


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [2, 2, 1]
    print("测试用例1:")
    print("输入:", nums1)
    print("异或方法:", solution.singleNumber(nums1))
    print("哈希表方法:", solution.singleNumberHash(nums1))
    print()
    
    # 测试用例2
    nums2 = [4, 1, 2, 1, 2]
    print("测试用例2:")
    print("输入:", nums2)
    print("异或方法:", solution.singleNumber(nums2))
    print("哈希表方法:", solution.singleNumberHash(nums2))
    print()
    
    # 测试用例3
    nums3 = [1]
    print("测试用例3:")
    print("输入:", nums3)
    print("异或方法:", solution.singleNumber(nums3))
    print("哈希表方法:", solution.singleNumberHash(nums3))
    print()
    
    # 测试用例4
    nums4 = [10, 20, 30, 20, 10]
    print("测试用例4:")
    print("输入:", nums4)
    print("异或方法:", solution.singleNumber(nums4))
    print("哈希表方法:", solution.singleNumberHash(nums4))