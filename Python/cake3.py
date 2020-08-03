def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    # Hash table to keep track which values we have visited
    # First node is head node which is our curr node
    # if we have a first node, we add its value to our hash
    # While we have a next on our current node,
    # keep iterating
    # if our curr node's value is in our hash, we break and
    # return false
    # else we keep iterating

    hash_table = {}
    curr_node = first_node

    if curr_node == None:
        return False

    # hash_table[curr_node.value] = curr_node.value

    # print(hash_table)

    # while curr_node.next != None:
    #     if curr_node.value in hash_table:
    #         # print(curr_node.value)
    #         return True
    #     else:
    #         hash_table[curr_node.value] = curr_node.value
    #     curr_node = curr_node.next

    # o(n) time and o(1)
    while curr_node.next != None:
        if curr_node.next.value <= curr_node.value:
            return True
        else:

            curr_node = curr_node.next

    # fast runner and slow runner because the numbers could be
    # totally arbritray and not in order
      # slow_runner = first_node
    # fast_runner = first_node

    # while fast_runner is not None and fast_runner.next is not None:
    #     slow_runner = slow_runner.next
    #     fast_runner = fast_runner.next.next

    #     if fast_runner is slow_runner:
    #         return True

    return False
