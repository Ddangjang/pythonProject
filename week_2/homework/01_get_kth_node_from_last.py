def get_kth_node_from_last(self, k):
    slow = self.head
    fast = self.head

    for i in range(k):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow