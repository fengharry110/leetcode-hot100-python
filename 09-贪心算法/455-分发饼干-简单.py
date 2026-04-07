"""
455. 分发饼干
https://leetcode.cn/problems/assign-cookies/description/

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例 1:
输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

示例 2:
输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.
"""

from typing import List


class Solution:
    """
    分发饼干解法类
    
    解题思路：
        排序后使用双指针，贪心策略
        
    算法步骤：
        1. 对孩子的胃口和饼干的尺寸进行排序
        2. 初始化两个指针，分别指向孩子和饼干的起始位置
        3. 遍历饼干：
           - 如果当前饼干能满足当前孩子，移动两个指针
           - 否则，移动饼干指针
        4. 返回满足的孩子数量
        
    时间复杂度：O(n log n + m log m)
    空间复杂度：O(1)
    """
    
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        计算最多能满足的孩子数量
        
        参数:
            g: 孩子的胃口数组
            s: 饼干的尺寸数组
            
        返回:
            最多能满足的孩子数量
        """
        # 排序
        g.sort()
        s.sort()
        
        # 初始化指针
        child = 0
        cookie = 0
        n = len(g)
        m = len(s)
        
        # 遍历饼干
        while child < n and cookie < m:
            if s[cookie] >= g[child]:
                # 饼干能满足孩子，移动两个指针
                child += 1
            # 无论是否满足，都移动饼干指针
            cookie += 1
        
        return child


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: g = [1,2,3], s = [1,1]")
    g1 = [1, 2, 3]
    s1 = [1, 1]
    solution = Solution()
    result1 = solution.findContentChildren(g1, s1)
    print(f"结果: {result1}")
    print(f"期望结果: 1")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: g = [1,2], s = [1,2,3]")
    g2 = [1, 2]
    s2 = [1, 2, 3]
    solution2 = Solution()
    result2 = solution2.findContentChildren(g2, s2)
    print(f"结果: {result2}")
    print(f"期望结果: 2")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: g = [10,9,8,7,6], s = [5,6,7,8]")
    g3 = [10, 9, 8, 7, 6]
    s3 = [5, 6, 7, 8]
    solution3 = Solution()
    result3 = solution3.findContentChildren(g3, s3)
    print(f"结果: {result3}")
    print(f"期望结果: 3")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: g = [1,1,1,1], s = [1,1,1,1,1]")
    g4 = [1, 1, 1, 1]
    s4 = [1, 1, 1, 1, 1]
    solution4 = Solution()
    result4 = solution4.findContentChildren(g4, s4)
    print(f"结果: {result4}")
    print(f"期望结果: 4")
