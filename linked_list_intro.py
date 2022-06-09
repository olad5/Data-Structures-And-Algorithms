class Node:
    def __init__(self, value):
            self.value  = value
            self.next  = None

class LinkedList:
    def __init__(self):
            self.head  = None
            self.tail  = None
            self.length  = 0

    def print_list_authors_solution(self):
        temp  = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print(self):
        # this method is from the codebasics youtube channel
        if self.head is None:
            print('Linked list is empty')
            return
        iterator = self.head # iterator
        llstr  = ''
        while iterator is not None:
            llstr += str(iterator.value) + ' --> '
            iterator = iterator.next
        print(llstr)

    def append(self, value):
        new_node =  Node(value)
        if self.head is None :
            self.head  = new_node
            self.tail  = new_node
            self.length += 1
            return
        else:
            self.tail.next =  new_node
            self.tail  = new_node
        self.length += 1
        return True

    def pop( self):
        if self.head is None:
            raise Exception('Linked list is empty')

        if self.length == 1:
            self.head = None
            self.tail = None
            return

        iterator  = self.head

        while  iterator.next.next is not None:
            iterator  =  iterator.next

        # saving this so we can return it
        temp  = iterator.next.value 

        self.tail  = iterator
        self.tail.next  = None
        self.length -= 1

        return temp

    def pop_author_solution(self):
        if self.length == 0:
            return None
        temp  = self.head
        pre  = self.head
        while (temp.next):
            pre  = temp
            temp  = temp.next

        self.tail  = pre
        self.tail.next  = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


    def prepend(self, value):
        new_node   = Node(value)
        if self.head is None: 
            self.head  = new_node
            self.tail  = new_node
            return
        else:
            new_node.next  = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.head is None:
            return None
        if self.length == 1:
            self.head  = None
            self.tail  = None
            return temp
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        return temp

    def pop_first_author_solution(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head  = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        iterator =  self.head
        count  = 0
        if self.head is None:
            return None
        while iterator is not None:
            if index == count:
                # print(f'value gotten {iterator.value}')
                return iterator
            count += 1
            iterator  = iterator.next
        raise Exception('Index not found')

    def get_author_solution(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print (temp.value)
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        new_node  = Node(value)
        temp  =  self.head
        pre =  self.head
        if index == 0:
            new_node.next = self.head.next
            self.head = new_node
            return True
        for  _ in  range(index):
            pre = temp
            temp  = temp.next
        pre.next = new_node 
        new_node.next  = temp.next
        return True

    def set_value_authors_solution(self, index, value):
        temp = self.get_author_solution(index)
        if temp:
            temp.value  = value
            return True
        return False


    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)

        if index == 0:
             return self.prepend(value)

        if index  == self.length :
            return self.append(value)

        if index  == self.length - 1:
            new_node.next =  self.tail
            self.get_author_solution(index - 1).next  = new_node
            return True

        pre  = self.get_author_solution(index )
        after  = self.get_author_solution(index + 1)
        new_node.next  = after
        pre.next = new_node
        self.length += 1
        return True

    def insert_value_authors_solution(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node   = Node(value)
        temp = self.get(index - 1)
        new_node.next  = temp.next
        temp.next  = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length :
            return None
        if index == 0:
            self.pop_first()
            return True
        if self.length  == 1:
            self.head = None
            self.tail = None
            return True
        if index == self.length - 1:
            temp = self.get(self.length - 2) 
            temp.next = None
            self.tail = temp
            return True

        pre = self.get(index - 1)
        temp = self.get(index)
        pre.next = temp.next
        # forgot to decrement the length
        # self.length -= 1
        return True

    def remove_authors_solution(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index  == self.length - 1:
            return self.pop()

        prev = self.get (index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # NOTE: this method doesn't work
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head
        pre = self.head
        temp = pre.next
        current = temp
        while current is not None:
            # temp  = temp.next
            current  = temp.next
            temp.next  = pre

        self.head, self.tail  =  self.tail, self.head
        return True

    def reverse_authors_solution(self):
        temp  = self.head
        self.head  = self.tail
        self.tail = temp
        after  = temp.next
        before = None
        for _ in range(self.length):
            # NOTE: they must appear exactly in this order
            after  =  temp.next
            temp.next = before
            before = temp
            temp  =  after







                

if __name__ == "__main__":
    ll = LinkedList()
    ll.print()
    ll.append(8)
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.print()
    # print( ll.length)
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()
    print( ll.length)
    ll.pop()
    ll.print()
    ll.prepend( 12)
    ll.print()
    ll.prepend( 13)
    ll.prepend( 18)
    ll.prepend( 1)
    ll.prepend( 10)
    ll.print()
    print( ll.length)

    # ll.pop_first()
    # ll.pop_first()
    # ll.pop_first()
    # ll.pop_first()
    # ll.pop_first()
    ll.print()

    # ll.get(0)
    # ll.get_author_solution(3)
    # ll.set_value_authors_solution(2, 4)
    # ll.set_value(4, 5)
    ll.print()
    # ll.insert_value(0, 19)
    print(ll.length)
    # ll.insert_value(4, 41)
    # ll.insert_value_authors_solution(5, 41)
    ll.remove(5)
    ll.print()
    ll.reverse_authors_solution()
    ll.print()
