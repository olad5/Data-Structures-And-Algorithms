class Node:
    def __init__(self, value):
            self.value  = value
            self.next  = None
            self.prev  = None

class DoublyLinkedList:
    def __init__(self):
            self.head  = None
            self.tail  = None
            self.length  = 0

    def print_list_authors_solution(self):
        temp  = self.head
        while temp is not None:
            print("|  " + str( temp.value ) + "  |")
            temp = temp.next
        print('')
        return 


    def append(self, value):
        new_node =  Node(value)
        if self.head is None :
            self.head  = new_node
            self.tail  = new_node
        else:
            self.tail.next =  new_node
            new_node.prev  =  self.tail
            self.tail  = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp  = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            prev = temp.prev
            prev.next  = None
            temp.prev = None
            self.tail  = prev

        self.length -= 1

        return temp

    def prepend(self, value) :
        new_node  = Node(value)
        if self.length == 0:
            self.head  = new_node
            self.tail  = new_node
        else:
            new_node.next  = self.head
            self.head.prev  = new_node
            self.head  = new_node
        self.length  += 1
        return True

    def pop_first(self) :
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else :
            self.head = temp.next
            self.head.prev = None
            temp.next= None
        self.length -= 1
        return  temp

    def get_authors_solution(self, index) :
        # NOTE: the same get method in a singly linked list would work
        # but this version is optimised for a DoublyLinkedList
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length  / 2:
            for _ in range(index):
                temp  =  temp.next

        else:
            temp  =  self.tail
            for _ in range(self.length - 1, index , -1):
                temp  = temp.prev

        return temp


    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if self.length == 1:
            self.head.value  =  value
            return True 
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp =  temp.next
            temp.value  = value
        else:
            temp =  self.tail
            for _ in range(self.length - 1, index, -1 ):
                temp =  temp.next
            temp.value  = value
        return True

    def set_value_authors_solution(self, index, value):
        temp = self.get_authors_solution(index)
        if temp:
            temp.value  =  value
            return True 
        return False

    def insert_authors_solution(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before  = self.get_authors_solution(index - 1)
        after   = before.next

        new_node.prev  = before
        new_node.next  = after
        before.next  = new_node
        after.prev  = new_node

        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            pre = self.get_authors_solution(self.length - 2)
            self.tail =  pre
            self.tail.next  = None
            return True

        temp =  self.get_authors_solution(index)
        before  = temp.prev
        after  = temp.next
        before.next  =  after
        after.prev = before
        self.length -= 1

        return temp

    def remove_authors_solution(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1 :
            return self.pop()

        # NOTE: authors knows this is harder to read, they just wanted to
        # show a new way of doing it
        temp  =  self.get_authors_solution(index)
        temp.next.prev  = temp.prev
        temp.prev.next  = temp.next
        temp.next  = None
        temp.prev  = None

        self.length -= 1 
        return temp




        



            

            






                

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.print_list_authors_solution()
    ll.append(8)
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(1)
    ll.print_list_authors_solution()

    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
    ll.print_list_authors_solution()
    ll.prepend(7)
    ll.prepend(2)
    ll.prepend(9)
    ll.prepend(8)
    ll.print_list_authors_solution()
    ll.pop_first()
    ll.print_list_authors_solution()
    # print( ll.get_authors_solution( 0).value )
    ll.set_value(3, 10 )
    ll.print_list_authors_solution()
    ll.insert_authors_solution(2, 20 )
    ll.print_list_authors_solution()
    print(ll.length)
    ll.remove(1)
    ll.print_list_authors_solution()
