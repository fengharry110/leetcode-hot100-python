"""
295. 数据流的中位数
https://leetcode.cn/problems/find-median-from-data-stream/description/

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

- MedianFinder() 初始化 MedianFinder 对象。
- void addNum(int num) 从数据流中添加一个整数到数据结构中。
- double findMedian() 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出：
[null, null, null, 1.5, null, 2.0]
解释：
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

提示:
-10^5 <= num <= 10^5
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 10^4 次调用 addNum 和 findMedian
"""


class MedianFinder:
    """
    请在此处实现你的解法
    """
    
    def __init__(self):
        # TODO: 在此实现初始化
        pass

    def addNum(self, num: int) -> None:
        # TODO: 在此实现你的解法
        pass

    def findMedian(self) -> float:
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: 基本操作")
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(f"findMedian(): {medianFinder.findMedian()}, 期望: 1.5")
    medianFinder.addNum(3)
    print(f"findMedian(): {medianFinder.findMedian()}, 期望: 2.0")
