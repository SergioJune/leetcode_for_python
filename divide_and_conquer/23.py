"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: list) -> ListNode:

        def merge(headA, headB):

            faker = ListNode(None, headA)
            cur = faker
            while cur.next and headB:
                if headB.val < cur.next.val:
                    next_node = headB.next
                    headB.next = cur.next
                    cur.next = headB
                    headB = next_node

                cur = cur.next
            if cur.next is None:  # 这个容易出错，需要cur.next 为空才插入，不然会漏这个元素
                cur.next = headB

            return faker.next

        def inner_sort(lists):
            length = len(lists)
            while True:
                cur, left, right = 0, 0, 1
                while right < length:
                    lists[cur] = merge(lists[left], lists[right])
                    left = right + 1
                    right = left + 1
                    cur += 1
                if left < length:
                    lists[cur] = lists[left]
                    cur += 1  # 这个长度也需要注意
                length = cur
                if length == 1:
                    break
            return lists[0]

        if len(lists) == 0:
            return None
        return inner_sort(lists)
