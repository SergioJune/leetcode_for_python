"""
实现一个动态数组类
1. 支持默认数组长度，也可初始化长度
2. 往数组末尾或者头部插入元素
3. 查询任一元素
4. 修改任一元素
5. 删除数组末尾或者头部元素
6. 当数组长度不够的时候，可以扩容数组长度至1.5倍或者2倍
7. 当数组删除元素至少于一半的时候缩小数组长度
"""


class DynamicArray(object):
    def __init__(self, length=10):
        self.__length = length
        self.__next_ele = 0
        self.__arr = [None] * self.__length

    def length(self):  # 数组长度
        return self.__length

    def add(self, val):  # 往数组添加元素, 默认添加到尾部
        self.add_index(self.__next_ele, val)

    def add_index(self, index, val):  # 往数组任意位置添加元素
        if self.__next_ele == self.__length:
            # 扩容
            self.__length *= 2
            new_arr = [None]*self.__length
            for i in range(self.__next_ele):
                new_arr[i] = self.__arr[i]
            self.__arr = new_arr

        for i in range(self.__next_ele, index, -1):
            self.__arr[i] = self.__arr[i-1]
        self.__arr[index] = val
        self.__next_ele += 1

    def add_head(self, val):  # 往数组头部添加元素
        self.add_index(0, val)

    def index(self, i):
        return self.__arr[i]

    def update(self, index, val):
        self.__arr[index] = val

    def remove(self, index=None):  # 删除元素, 默认删除尾部元素
        if self.__next_ele <= self.__length // 2:
            self.__length = self.__length // 2
            new_arr = [None]*self.__length
            for i in range(self.__next_ele):
                new_arr[i] = self.__arr[i]
            self.__arr = new_arr

        if index is None:
            index = self.__next_ele-1
        print(index)
        remove_val = self.__arr[index]
        self.__next_ele -= 1
        for i in range(index, self.__next_ele):
            self.__arr[i] = self.__arr[i + 1]
        return remove_val

    def remove_head(self):  # 删除头部元素
        return self.remove(0)

    def __str__(self):
        res = ["[", ]
        for i in range(self.__next_ele):
            res.append(str(self.__arr[i]))
            res.append(", ")
        res.pop()
        res.append("]")
        return "".join(res)


if __name__ == "__main__":
    dy = DynamicArray()
    for i in range(10):
        dy.add(i)
    print(dy)
    print(dy.length())
    dy.add_index(3, 100)
    print(dy)
    print(dy.length())
    dy.remove()
    dy.remove()
    dy.remove()
    dy.remove()
    dy.remove()
    dy.remove()
    print(dy.length())
    print(dy)
