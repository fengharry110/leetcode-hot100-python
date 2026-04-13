"""
146. LRU 缓存
中等
请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 10^5
最多调用 2 * 10^5 次 get 和 put
"""


class DLinkedNode:
    """双向链表节点"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表：key -> 节点
        
        # 虚拟头尾节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def _add_to_head(self, node: DLinkedNode):
        """将节点添加到头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: DLinkedNode):
        """移除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node: DLinkedNode):
        """将节点移动到头部"""
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self) -> DLinkedNode:
        """移除尾节点"""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._remove_tail()
                del self.cache[tail.key]
                self.size -= 1


if __name__ == "__main__":
    # 测试用例
    lru = LRUCache(2)
    print("LRUCache(2)")
    
    lru.put(1, 1)
    print("put(1, 1)")
    
    lru.put(2, 2)
    print("put(2, 2)")
    
    print(f"get(1) = {lru.get(1)}")  # 返回 1
    
    lru.put(3, 3)
    print("put(3, 3)")  # 淘汰 key 2
    
    print(f"get(2) = {lru.get(2)}")  # 返回 -1
    
    lru.put(4, 4)
    print("put(4, 4)")  # 淘汰 key 1
    
    print(f"get(1) = {lru.get(1)}")  # 返回 -1
    print(f"get(3) = {lru.get(3)}")  # 返回 3
    print(f"get(4) = {lru.get(4)}")  # 返回 4
