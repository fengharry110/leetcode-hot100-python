"""
118. 杨辉三角
https://leetcode.cn/problems/pascals-triangle/description/

给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

示例 2:
输入: numRows = 1
输出: [[1]]
"""

from typing import List


class Solution:
    """
    杨辉三角解法类
    
    解题思路：
        动态规划，每一行的元素由上一行的元素推导而来
        
    算法步骤：
        1. 初始化结果列表
        2. 遍历每一行：
           - 初始化当前行为1
           - 对于中间元素，等于上一行对应位置和前一个位置的和
           - 添加1到行尾
           - 将当前行添加到结果列表
        3. 返回结果列表
        
    时间复杂度：O(n²)
    空间复杂度：O(n²)
    """
    
    def generate(self, numRows: int) -> List[List[int]]:
        """
        生成杨辉三角
        
        参数:
            numRows: 行数
            
        返回:
            杨辉三角的前numRows行
        """
        if numRows == 0:
            return []
        
        result = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            # 计算中间元素
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            # 添加行尾的1
            row.append(1)
            result.append(row)
        
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: numRows = 5")
    numRows1 = 5
    solution = Solution()
    result1 = solution.generate(numRows1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: numRows = 1")
    numRows2 = 1
    solution2 = Solution()
    result2 = solution2.generate(numRows2)
    print(f"结果: {result2}")
    print(f"期望结果: [[1]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: numRows = 3")
    numRows3 = 3
    solution3 = Solution()
    result3 = solution3.generate(numRows3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1],[1,1],[1,2,1]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: numRows = 0")
    numRows4 = 0
    solution4 = Solution()
    result4 = solution4.generate(numRows4)
    print(f"结果: {result4}")
    print(f"期望结果: []")
