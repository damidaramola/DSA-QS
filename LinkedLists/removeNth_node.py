class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we want two pointers, left hits num to delete, right moves n times
        # distance between left and right should be n
        # use dummy node to hit node just before target node
        # delete by skipping node in front of left
        # when right goes out of bounds(left is before target), return the mdofied list after deleting

        
        dummy = ListNode(0,head) 
        left = dummy
        right = head

        # move the right pointer n times ahead of left so when right is our of bounds we can remove 
        while n > 0 and right:
            right = right.next
            n -=1

        while right:
            left = left.next
            right = right.next
        #delete nth node
        left.next = left.next.next
        return dummy.next

# Time complexity O(1)
# space complexity O(n)