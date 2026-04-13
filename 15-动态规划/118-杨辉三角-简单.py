# 118. 杨辉三角
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
# 示例 1:
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# 示例 2:
# 输入: numRows = 1
# 输出: [[1]]

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(row)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print(f"测试1结果: {solution.generate(5)}")
    
    # 测试2
    print(f"测试2结果: {solution.generate(1)}")
