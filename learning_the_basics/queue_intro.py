class Node:
    def __init__(self, value):
        self.value  = value
        self.next  = None


class Queue: 
    def __init__(self):
        self.first  = None
        self.last  = None
        self.length = 0

    def print_queue(self):
        temp  =  self.first
        while temp:
            print(temp.value)
            temp = temp.next
        if self.first:
            print( 'end of the queue\n')

    def enqueue(self, value):
        new_node  =  Node(value)
        if self.length == 0:
            self.first  =  new_node
            self.last  =  new_node

        else:
            # NOTE: because it's FIFO
            self.last.next  = new_node
            self.last = new_node

        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp  = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
           self.first  = temp.next
           temp.next = None

        self.length -= 1
        return temp


if __name__ == "__main__":
    qu = Queue()
    qu.enqueue(2)
    qu.enqueue(1)
    qu.enqueue(9)
    # print('printing the first element now: ')
    # print( qu.last.value )
    qu.print_queue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.print_queue()
