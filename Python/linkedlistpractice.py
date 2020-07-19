class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# class LinkedList:
#     def __init__(self):
#         self.head = None

def insertNodeAtPosition(head, data, position):
    n = head
    counter = 1

    if position == 0:
        temp = n
        n = n.next
        return head

    while n.next != None:
        if position == counter:
            temp_temp = n.next
            n.next = n.next.data
            n.next.next = temp_temp
            return head
        else:
            n = n.next
            counter += 1
    return head


print(insertNodeAtPosition((16, 13, 7), 1, 2))

# if __name__ == '__main__':
