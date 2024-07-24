# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # input - list, output - true/false
        # a linkedlist can only go in one direction
        # do i need to reverse it?
        # if the reverse is true then its a palindrome

        # if we reverse and equate it to the head
        # if they are the same then true else false 
        # I dont need to create a new head?
        # look up dummy nodes
        # if dummy.next == head true/false

        #actual pseudocode

        # set fast and slow pointers
        # reverse ll half way
        # check both halves for same values
        # ll true/false


        # set fast and slow pointers
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        # reverse ll half way
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur 
            cur = next 

        left = head 
        right = prev

        # check both halves for same values
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
# Time complexity O(n)
# Space complexity O(1)           