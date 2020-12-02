"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        faker = ListNode(None)
        faker.next = head
        slow = fast = faker
        while fast and fast.next:
            if fast.next.val < x:
                if slow == fast:
                    slow = slow.next
                    fast = fast.next
                    continue
                cur = fast.next
                fast.next = fast.next.next
                # 插入到slow指针的下一个结点
                cur.next = slow.next
                slow.next = cur
                slow = cur
            else:
                fast = fast.next

        return faker.next

