"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = dict()
        faker = ListNode(None, head)
        cur = faker
        while cur.next:
            res = d.get(cur.next.val, None)
            if res is None:
                d[cur.next.val] = cur
                cur = cur.next
            else:
                val = cur.next.val
                cur.next = cur.next.next
                if res !=1:
                    res.next = res.next.next
                    d[val] = 1
                    cur = res
        return faker.next