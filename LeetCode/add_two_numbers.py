from algorithm.pattern_exercises_probable import ListNode

list1 = [2,4,3]
list2 = [5,6,4]
list3 = [0]
list4 = [0]
list5 = [9,9,9,9,9,9,9]
list6 = [9,9,9,9]

def add_two_numbers_for_list(l1: list, l2: list) -> list:
    new_list = []
    remaining = 0
    result = 0

    if len(l1) > len(l2):
        max_iter = len(l1)
        iter_diff = len(l1) - len(l2)
        for i in range(iter_diff):
            l2.append(0)
    else:
        max_iter = len(l2)
        iter_diff = len(l2) - len(l1)
        for i in range(iter_diff):
            l1.append(0)

    for i in range(max_iter):
        if not l1[i]:
            l1.append(0)
        if not l2[i]:
            l2.append(0)

        if remaining != 0:
            l1[i] += remaining
            remaining = 0
        if l1[i] + l2[i] > 9:
            result += ((l1[i] + l2[i]) -10)
            remaining += 1
        else:
            result += (l1[i] + l2[i])
        new_list.append(result)
        result = 0
    if remaining != 0:
        new_list.append(remaining)
    return new_list

print(add_two_numbers_for_list(list1, list2))
print(add_two_numbers_for_list(list3, list4))
print(add_two_numbers_for_list(list5, list6))

ln1, ln1.next, ln1.next.next = ListNode(2), ListNode(4), ListNode(3)
ln2, ln2.next, ln2.next.next = ListNode(5), ListNode(6), ListNode(4)
ln3 = ListNode(0)
ln4 = ListNode(0)
ln5 = ListNode(9, ListNode(9, ListNode(9)))
ln6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))

def add_two_numbers_for_list_node(ln1: ListNode, ln2: ListNode) -> ListNode:
    dummy = ListNode()
    res = dummy

    total = carry = 0

    while ln1 or ln2 or carry:
        total = carry

        if ln1:
            total += ln1.val
            ln1 = ln1.next
        if ln2:
            total += ln2.val
            ln2 = ln2.next

        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next

    return res.next
print("==ListNode==")

print(add_two_numbers_for_list_node(ln1, ln2))