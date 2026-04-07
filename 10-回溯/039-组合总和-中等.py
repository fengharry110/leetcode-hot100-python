"""
39. 组合总和
https://leetcode.cn/problems/combination-sum/description/

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []
"""

from typing import List


class Solution:
    """
    组合总和解法类
    
    解题思路：
        使用回溯算法，递归生成所有可能的组合
        
    算法步骤：
        1. 对数组进行排序，方便剪枝
        2. 定义回溯函数，参数为当前路径、当前和、当前索引
        3. 当当前和等于target时，将路径加入结果
        4. 当当前和大于target时，剪枝返回
        5. 遍历数组，从当前索引开始：
           - 选择元素，将其加入路径，更新当前和
           - 递归调用回溯函数
           - 撤销选择，将元素从路径中移除，更新当前和
        
    时间复杂度：O(n^target)
    空间复杂度：O(target)
    """
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        找出所有和为target的组合
        
        参数:
            candidates: 无重复元素的整数数组
            target: 目标整数
            
        返回:
            所有不同的组合
        """
        result = []
        # 排序，方便剪枝
        candidates.sort()
        n = len(candidates)
        
        def backtrack(path, current_sum, start):
            """
            回溯函数
            
            参数:
                path: 当前路径
                current_sum: 当前和
                start: 当前索引
            """
            # 终止条件：和等于target
            if current_sum == target:
                result.append(path[:])
                return
            # 终止条件：和大于target，剪枝
            if current_sum > target:
                return
            
            # 遍历数组
            for i in range(start, n):
                # 选择元素
                path.append(candidates[i])
                current_sum += candidates[i]
                # 递归，注意这里可以重复选择当前元素
                backtrack(path, current_sum, i)
                # 撤销选择
                current_sum -= candidates[i]
                path.pop()
        
        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: candidates = [2,3,6,7], target = 7")
    candidates1 = [2,3,6,7]
    target1 = 7
    solution = Solution()
    result1 = solution.combinationSum(candidates1, target1)
    print(f"结果: {result1}")
    print(f"期望结果: [[2,2,3],[7]]")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: candidates = [2,3,5], target = 8")
    candidates2 = [2,3,5]
    target2 = 8
    solution2 = Solution()
    result2 = solution2.combinationSum(candidates2, target2)
    print(f"结果: {result2}")
    print(f"期望结果: [[2,2,2,2],[2,3,3],[3,5]]")
    
    # 测试用例3
    print("\n" + "=" * 50)
    print("测试用例3: candidates = [2], target = 1")
    candidates3 = [2]
    target3 = 1
    solution3 = Solution()
    result3 = solution3.combinationSum(candidates3, target3)
    print(f"结果: {result3}")
    print(f"期望结果: []")
    
    # 测试用例4
    print("\n" + "=" * 50)
    print("测试用例4: candidates = [1], target = 2")
    candidates4 = [1]
    target4 = 2
    solution4 = Solution()
    result4 = solution4.combinationSum(candidates4, target4)
    print(f"结果: {result4}")
    print(f"期望结果: [[1,1]]")
