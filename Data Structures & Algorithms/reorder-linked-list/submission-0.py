# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# find length of linked list
# reverse second half of the linked list
# redo the process where the next points to alternate ones

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head
        rear = head
        n = 1
        while rear.next:
            n += 1
            rear = rear.next
        
        mid_index = -(-n//2)
        mid = head
        while mid_index != 1:
            mid = mid.next
            mid_index -= 1
        
        temp = mid.next
        mid.next = None
        mid = temp
        # mid onwards, we want to reverse the linked list
        prev = None
        curr = mid

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        # so now i have [0 -> 1 -> 2 -> 3], head is front and 
        # [6 -> 5 -> 4], head is prev
        base = front
        while prev:
            temp = front.next
            front.next = prev
            front = front.next
            prev = temp
        

