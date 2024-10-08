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

        dict_copy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            dict_copy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            node = dict_copy[curr]
            node.next = dict_copy[curr.next]
            node.random = dict_copy[curr.random]
            curr = curr.next
        
        return dict_copy[head]