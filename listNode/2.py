"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = faker = ListNode(0)
        num = 0
        while l1 and l2:
            res = l1.val + l2.val + num
            remainder = res % 10
            cur.next = ListNode(remainder)
            num = res // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        last = l1 if l1 else l2
        while last:
            res = last.val + num
            remainder = res % 10
            cur.next = ListNode(remainder)
            num = res // 10
            cur = cur.next
            last = last.next
        if num > 0:
            cur.next = ListNode(num)

        return faker.next

