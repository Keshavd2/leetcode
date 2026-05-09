class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    fast_pointer = slow_pointer = head
    while (fast_pointer != None and fast_pointer.next != None):
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if fast_pointer == slow_pointer:
            return True
    
    return False

# Build test case: 1 → 2 → 3 → 4 → back to node at index 1
n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
print(has_cycle(n1))   # Expected: True

# No cycle: 1 → 2 → 3
a, b, c = ListNode(1), ListNode(2), ListNode(3)
a.next, b.next = b, c
print(has_cycle(a))    # Expected: False