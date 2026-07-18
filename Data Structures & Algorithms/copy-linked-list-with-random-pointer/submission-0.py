"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return None
        base_head_1 = head
        node_map = {}

        temp_1 = Node(head.val)
        base_head_2 = temp_1
        node_map[head] = temp_1
        head = head.next
        

        while head:
            temp_2 = Node(head.val)
            node_map[head] = temp_2
            temp_1.next = temp_2
            temp_1 = temp_2
            head = head.next

        random_1 = base_head_1
        random_2 = base_head_2
        while random_1:
            temp_3 = random_1.random
            random_2.random = node_map.get(temp_3, None)
            random_1 = random_1.next
            random_2 = random_2.next

        
        return base_head_2
        

