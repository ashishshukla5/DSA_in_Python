def deleteDuplicates(head):
        if head is None:
            return head
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:    
                curr = curr.next
        return head