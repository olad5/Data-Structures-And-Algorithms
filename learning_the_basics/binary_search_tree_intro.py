class Node:
    def __init__(self, value):
        self.value  = value
        self.right  = None
        self.left  = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_authors_solution(self, value):
        new_node  = Node(value)
        if self.root  is None:
            self.root  = new_node
            return True
        temp  = self.root

        while(True):
            if new_node.value  == temp.value:
                return False
            if new_node.value  < temp.value:
                if temp.left is None:
                    temp.left  = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right  = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while True:
            if value == temp.value:
                return True
            if value > temp.value:
                if temp.right is None:
                    return False
                temp  = temp.right 
            else:
                if temp.left is None:
                    return False
                temp  = temp.left

    def contains_authors_solution(self, value):
        # so short, it's amazing
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp  = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert_authors_solution(2)
    bst.insert_authors_solution(1)
    bst.insert_authors_solution(3)
    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)
    print( bst.contains(10) )
    bst.insert_authors_solution(47)
    bst.insert_authors_solution(21)
    bst.insert_authors_solution(76)
    bst.insert_authors_solution(18)
    bst.insert_authors_solution(27)
    bst.insert_authors_solution(52)
    bst.insert_authors_solution(82)
    print( bst.contains_authors_solution(7) )

