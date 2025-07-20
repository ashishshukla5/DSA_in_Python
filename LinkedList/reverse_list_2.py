class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        left_prev = dummy

        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next
        
        prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left_prev.next.next = curr
        left_prev.next = prev
        
        return dummy.next