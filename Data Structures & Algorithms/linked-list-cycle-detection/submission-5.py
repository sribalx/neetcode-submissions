# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can return false if any node.next gives you null
# but how to return true?
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        point_1 = head
        point_2 = head

        while point_2 and point_2.next:
            point_1 = point_1.next
            point_2 = point_2.next.next
            if point_1 == point_2:
                return True
        return False