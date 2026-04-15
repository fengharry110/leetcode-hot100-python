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

提示:
1 <= numRows <= 30
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def generate(self, numRows: int) -> List[List[int]]:
        """
        生成杨辉三角的前numRows行
        
        参数:
            numRows: 行数
            
        返回:
            杨辉三角
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: numRows = 5")
    numRows1 = 5
    result1 = solution.generate(numRows1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: numRows = 1")
    numRows2 = 1
    result2 = solution.generate(numRows2)
    print(f"结果: {result2}")
    print(f"期望结果: [[1]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: numRows = 2")
    numRows3 = 2
    result3 = solution.generate(numRows3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1],[1,1]]")
