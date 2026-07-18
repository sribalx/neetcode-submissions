# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = head
        k = 0
        while count:
            k += 1
            count = count.next
        
        last_saved_index = k - n
        if last_saved_index == 0:
            return head.next
        ls = head
        while last_saved_index > 1:
            ls = ls.next
            last_saved_index -= 1
        
        ls_link = ls.next.next
        ls.next = ls_link

        return head
        


             
            
        
