# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        i = 1
        while l1:
            num1 += (l1.val * i)
            l1 = l1.next
            i = i * 10
        
        i = 1
        while l2:
            num2 += (l2.val * i)
            l2 = l2.next
            i = i * 10
        
        sum = num1 + num2
        if sum == 0:
            return ListNode()
        curr = ListNode()
        base = curr
        while sum > 0:
            value = sum % 10
            sum = sum // 10
            curr.next = ListNode(value)
            curr = curr.next
        
        return base.next
