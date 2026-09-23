# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        if not head:
            return False
        while (head.next is not None):
            if(head.val not in s):
                s.add(head.val)
            else:
                return True
            head=head.next
        return False