"""
给定一个链表，判断链表中是否有环。
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        low = head
        fast = head.next
        while fast and fast.next:
            if low == fast:
                return True
            low = low.next
            fast = fast.next.next


if __name__ == "__main__":
    # [3,2,0,-4]
    head = ListNode(3)
    head.next = head
    solu = Solution()
    print(solu.hasCycle(head))
