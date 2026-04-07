"""
733. 图像渲染
https://leetcode.cn/problems/flood-fill/description/

有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的颜色值，然后上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再对这些像素点继续同样的操作，重复这个过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

示例 1:
输入: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析: 
在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。

示例 2:
输入: 
image = [[0,0,0],[0,0,0]]
sr = 0, sc = 0, newColor = 2
输出: [[2,2,2],[2,2,2]]
"""

from typing import List


class Solution:
    """
    图像渲染解法类
    
    解题思路：
        深度优先搜索，从初始位置开始，递归处理四个方向
        
    算法步骤：
        1. 记录初始颜色
        2. 如果初始颜色等于新颜色，直接返回原图
        3. 深度优先搜索，将符合条件的像素点改为新颜色
        4. 返回修改后的图像
        
    时间复杂度：O(mn)
    空间复杂度：O(mn)
    """
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        图像渲染
        
        参数:
            image: 二维图像数组
            sr: 起始行坐标
            sc: 起始列坐标
            newColor: 新颜色
            
        返回:
            渲染后的图像
        """
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        # 如果初始颜色等于新颜色，直接返回
        if oldColor == newColor:
            return image
        
        def dfs(i, j):
            """
            深度优先搜索
            
            参数:
                i, j: 当前位置
            """
            if 0 <= i < m and 0 <= j < n and image[i][j] == oldColor:
                image[i][j] = newColor
                # 四个方向
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        dfs(sr, sc)
        return image


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2")
    image1 = [[1,1,1],[1,1,0],[1,0,1]]
    sr1 = 1
    sc1 = 1
    newColor1 = 2
    solution = Solution()
    result1 = solution.floodFill(image1, sr1, sc1, newColor1)
    print(f"结果: {result1}")
    print(f"期望结果: [[2,2,2],[2,2,0],[2,0,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2")
    image2 = [[0,0,0],[0,0,0]]
    sr2 = 0
    sc2 = 0
    newColor2 = 2
    solution2 = Solution()
    result2 = solution2.floodFill(image2, sr2, sc2, newColor2)
    print(f"结果: {result2}")
    print(f"期望结果: [[2,2,2],[2,2,2]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: image = [[0,0,0],[0,1,0]], sr = 1, sc = 1, newColor = 2")
    image3 = [[0,0,0],[0,1,0]]
    sr3 = 1
    sc3 = 1
    newColor3 = 2
    solution3 = Solution()
    result3 = solution3.floodFill(image3, sr3, sc3, newColor3)
    print(f"结果: {result3}")
    print(f"期望结果: [[0,0,0],[0,2,0]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: image = [[1,1,1],[1,1,1],[1,1,1]], sr = 1, sc = 1, newColor = 1")
    image4 = [[1,1,1],[1,1,1],[1,1,1]]
    sr4 = 1
    sc4 = 1
    newColor4 = 1
    solution4 = Solution()
    result4 = solution4.floodFill(image4, sr4, sc4, newColor4)
    print(f"结果: {result4}")
    print(f"期望结果: [[1,1,1],[1,1,1],[1,1,1]]")
