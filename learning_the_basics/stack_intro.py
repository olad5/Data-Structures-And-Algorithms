
class Node:
    def __init__(self, value):
        self.value  = value
        self.next  = None

class Stack:
    def __init__(self):
        self.top  = None
        self.height  = 0


    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            print("↓")
            temp = temp.next
        if self.top:
            print( 'end of print \n')

    def push(self, value):
        new_node  = Node(value)
        if self.height == 0:
            self.top  = new_node
        else:
            new_node.next  = self.top
            self.top  = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp  = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top  =  temp.next
            temp.next  =  None
        self.height -= 1
        return temp

    def pop_authors_solution(self):
        if self.height == 0:
            return None
        temp  = self.top
        self.top  =  self.top.next
        temp.next  =  None
        self.height -= 1
        return temp



if __name__ == "__main__":
    st = Stack()
    st.print_stack()
    st.push(8)
    st.push(4)
    st.push(5)
    st.print_stack()
    st.pop()
    st.pop_authors_solution()
    st.print_stack()
