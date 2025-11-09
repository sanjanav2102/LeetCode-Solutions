# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        '''l = []
        current = head
        while current and current.next:
            if current in l:
                return True   
            else:
                l.append(current)
                current = current.next
               
        return False'''
        slow =head
        fast = head
        while (fast!= None and fast.next!= None):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                return True
        return False
        
