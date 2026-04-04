"""
46. 全排列
https://leetcode.cn/problems/permutations/description/

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]
"""

from typing import List


class Solution:
    """
    回溯解法类
    
    解题思路：
        使用回溯算法，通过选择和撤销选择来生成所有排列
        
    算法步骤：
        1. 定义回溯函数，参数为当前路径和已使用的元素
        2. 当路径长度等于数组长度时，将当前路径加入结果
        3. 遍历数组中的每个元素：
           - 如果元素已被使用，跳过
           - 选择该元素，标记为已使用
           - 递归调用回溯函数
           - 撤销选择，标记为未使用
        4. 返回结果
        
    时间复杂度：O(n * n!)
    空间复杂度：O(n)
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        生成所有全排列
        
        参数:
            nums: 不含重复数字的数组
            
        返回:
            所有可能的全排列
        """
        result = []
        used = [False] * len(nums)
        
        def backtrack(path):
            """
            回溯函数
            
            参数:
                path: 当前路径
            """
            # 终止条件：路径长度等于数组长度
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # 如果元素已被使用，跳过
                if used[i]:
                    continue
                
                # 选择元素
                used[i] = True
                path.append(nums[i])
                
                # 递归
                backtrack(path)
                
                # 撤销选择
                path.pop()
                used[i] = False
        
        backtrack([])
        return result


class SolutionSwap:
    """
    交换解法类
    
    解题思路：
        通过交换元素来生成排列，避免使用额外的标记数组
        
    算法步骤：
        1. 定义回溯函数，参数为当前位置
        2. 当当前位置等于数组长度时，将当前数组加入结果
        3. 从当前位置开始遍历：
           - 交换当前位置与遍历位置的元素
           - 递归调用回溯函数，处理下一个位置
           - 交换回来，恢复原状
        4. 返回结果
        
    时间复杂度：O(n * n!)
    空间复杂度：O(n)
    """
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        通过交换生成全排列
        
        参数:
            nums: 不含重复数字的数组
            
        返回:
            所有可能的全排列
        """
        result = []
        n = len(nums)
        
        def backtrack(start):
            """
            回溯函数
            
            参数:
                start: 当前处理的位置
            """
            # 终止条件：处理到数组末尾
            if start == n:
                result.append(nums[:])
                return
            
            for i in range(start, n):
                # 交换元素
                nums[start], nums[i] = nums[i], nums[start]
                # 递归处理下一个位置
                backtrack(start + 1)
                # 交换回来
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: [1,2,3]")
    nums1 = [1, 2, 3]
    solution = Solution()
    result1 = solution.permute(nums1)
    print(f"结果: {result1}")
    print(f"期望结果: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: [0,1]")
    nums2 = [0, 1]
    solution2 = SolutionSwap()
    result2 = solution2.permute(nums2)
    print(f"结果: {result2}")
    print(f"期望结果: [[0,1],[1,0]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: [1]")
    nums3 = [1]
    solution3 = Solution()
    result3 = solution3.permute(nums3)
    print(f"结果: {result3}")
    print(f"期望结果: [[1]]")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: [1,2,3,4]")
    nums4 = [1, 2, 3, 4]
    solution4 = SolutionSwap()
    result4 = solution4.permute(nums4)
    print(f"结果数量: {len(result4)}")
    print(f"期望结果数量: 24")
