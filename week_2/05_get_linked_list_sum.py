def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2


def _get_linked_list_sum(linked_list):
    sum = 0
    head = linked_list.head
    while head is not None:
        sum = sum * 10 + head.data
        head = head.next
    return sum