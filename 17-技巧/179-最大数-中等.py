"""
179. 最大数
https://leetcode.cn/problems/largest-number/description/

给定一组非负整数 nums，重新排列它们的顺序使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [0,0]
输出："0"
"""

from typing import List


class Solution:
    """
    最大数解法类
    
    解题思路：
        自定义排序规则，比较两个数的不同排列方式
        
    算法步骤：
        1. 将所有数字转换为字符串
        2. 自定义排序规则，比较a+b和b+a的大小
        3. 排序后拼接所有字符串
        4. 处理前导零的情况
        
    时间复杂度：O(nlogn)
    空间复杂度：O(n)
    """
    
    def largestNumber(self, nums: List[int]) -> str:
        """
        生成最大数
        
        参数:
            nums: 非负整数数组
            
        返回:
            最大数的字符串形式
        """
        # 将数字转换为字符串
        str_nums = list(map(str, nums))
        
        # 自定义排序规则
        def compare(a, b):
            return int(b + a) - int(a + b)
        
        # 排序
        str_nums.sort(key=lambda x: x, cmp=compare)
        
        # 处理前导零
        if str_nums[0] == '0':
            return '0'
        
        # 拼接结果
        return ''.join(str_nums)


# 兼容Python3的cmp_to_key
from functools import cmp_to_key

class SolutionPython3:
    """
    Python3兼容解法类
    """
    
    def largestNumber(self, nums: List[int]) -> str:
        """
        生成最大数（Python3兼容版本）
        
        参数:
            nums: 非负整数数组
            
        返回:
            最大数的字符串形式
        """
        # 将数字转换为字符串
        str_nums = list(map(str, nums))
        
        # 自定义排序规则
        def compare(a, b):
            return int(b + a) - int(a + b)
        
        # 排序
        str_nums.sort(key=cmp_to_key(compare))
        
        # 处理前导零
        if str_nums[0] == '0':
            return '0'
        
        # 拼接结果
        return ''.join(str_nums)


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [10,2]")
    nums1 = [10,2]
    solution = SolutionPython3()
    result1 = solution.largestNumber(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: \"210\"")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [3,30,34,5,9]")
    nums2 = [3,30,34,5,9]
    solution2 = SolutionPython3()
    result2 = solution2.largestNumber(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: \"9534330\"")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [0,0]")
    nums3 = [0,0]
    solution3 = SolutionPython3()
    result3 = solution3.largestNumber(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: \"0\"")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1]")
    nums4 = [1]
    solution4 = SolutionPython3()
    result4 = solution4.largestNumber(nums4)
    print(f"结果: {result4}")
    print(f"期望结果: \"1\"")
