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

    def dfs_pre_order(self):
        results  = []
        def traverse(current_node) :
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert_authors_solution(47)
    bst.insert_authors_solution(21)
    bst.insert_authors_solution(76)
    bst.insert_authors_solution(18)
    bst.insert_authors_solution(27)
    bst.insert_authors_solution(52)
    bst.insert_authors_solution(82)
    print(bst.dfs_pre_order())

