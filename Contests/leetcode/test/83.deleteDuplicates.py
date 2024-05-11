class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    cur = head
    while cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
