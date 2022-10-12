
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # create node and push to front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_nth_from_last(self,n):
        # traverse list to find length
        scan = self.head
        length = 0
        while scan is not None:
            length += 1
            scan = scan.next

        # handle error condition if n > length
        if n > length:
            print('n cannot be greater than length of list.')
            return None

        # iterate to nth node at length - n + 1(next)
        scan = self.head
        # print(length, n)
        for i in range(0, length - n):
            # print(i)
            scan = scan.next
        print(scan.data)

#Driver Code

#TEST1:  return 2
llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print('TEST#1:  Third from last node is:  ')
llist.print_nth_from_last(3)

#TEST2:  return none
llist = LinkedList()
llist.push(2)                           
llist.push(1)

print('TEST#2:  Fourth from last node is:  ')
llist.print_nth_from_last(4)
