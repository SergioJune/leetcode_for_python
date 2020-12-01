"""
设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=None, real=None, next_node=None):
        self.val = val
        self.real = real
        self.next = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.head = ListNode()
        self.d = dict()
        self.last = None

    def get(self, key: int) -> int:
        res = self.d.get(key, -1)
        if res != -1:
            target = res.next  # 这个是目标节点，里面含有返回的值
            if target == self.last and res != self.head:  # 修改尾指针
                self.last = res
            if target.next and target.next.val:  # 修改map中对应的关系，因为我的map是记录key对应的前驱结点
                self.d[target.next.val] = res
            res.next = res.next.next
            if self.head.next:
                self.d[self.head.next.val] = target
            target.next = self.head.next
            self.head.next = target
            self.d[key] = self.head  # 更新map中的关系
            res = target

        return res.real

    def put(self, key: int, value: int) -> None:
        exist_node = self.d.get(key, None)
        if exist_node is not None:  # 直接插入到头节点即可
            if exist_node.next.next:
                self.d[exist_node.next.next.val] = exist_node
            exist_node.next = exist_node.next.next
        else:
            if self.length == self.capacity:  # 说明需要删除为节点
                prev = self.d[self.last.val]
                prev.next = None
                del self.d[self.last.val]  # 记得删除map中的映射
                self.last = prev
            else:
                self.length += 1
        node = ListNode(key, value, self.head.next)  # 每次都生成节点是因为value的值可能不一样

        if self.last is None: # 说明当前节点就是尾结点
            self.last = node
        elif self.last.val == key:
            if exist_node.val is None:  # 当前结点只有一个元素
                self.last = node
            else:
                self.last = exist_node

        if node.next:
            self.d[node.next.val] = node
        self.head.next = node
        self.d[key] = self.head


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(2, 2)
    print(obj.get(2))
    obj.put(1, 1)
    obj.put(4, 1)
    print(obj.get(2))

