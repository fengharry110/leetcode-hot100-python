# 295. 数据流的中位数
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，
# 中位数是两个中间值的平均值。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。

import heapq

class MedianFinder:
    def __init__(self):
        # 最大堆（存储较小的一半，Python用负数模拟）
        self.max_heap = []
        # 最小堆（存储较大的一半）
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        # 先加入最大堆
        heapq.heappush(self.max_heap, -num)
        
        # 平衡：将最大堆的最大值移到最小堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # 如果最小堆比最大堆多超过1个元素，移回一个
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"中位数: {mf.findMedian()}")  # 期望输出: 1.5
    mf.addNum(3)
    print(f"中位数: {mf.findMedian()}")  # 期望输出: 2.0
