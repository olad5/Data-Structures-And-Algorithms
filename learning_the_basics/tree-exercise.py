# Exercise Link:  https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md

# Question 1
class TreeNodeOne:
    def __init__(self, data):
        self.children = []
        self.parent = None
        self.data = data

    def add_child(self, child):
        child.parent  = self
        self.children.append(child)

    def get_level(self):
            level = 0
            p = self.parent
            while p:
                level += 1
                p = p.parent

            return level

    def print_tree(self, value= 'name'):
        data =  self.data[0]
        if value == "name":
            data  = self.data[0]
        elif value == "designation":
            data  = self.data[1]
        else:
            # data  = self.data[0] + " " +   str( self.data[1]  )
            data  = self.data[0] + " " +  f"({ self.data[1] })"
                
        spaces  = ' ' * self.get_level() * 3
        prefix  = spaces + "|__" if self.parent else ''
        print(prefix + data)
        if self.children:
            for child in self.children:
                child.print_tree(value)


def build_tree():
        ceo  = TreeNodeOne([ 'Nilpul', 'CEO' ])
        cto  = TreeNodeOne([ 'Chinmay', 'CTO' ])
        infras_head  = TreeNodeOne([ 'Vishwa', 'Infrastructure Head' ])
        hr_head  = TreeNodeOne([ 'Gels', 'HR HEAD' ])

        ceo.add_child(cto)
        ceo.add_child(hr_head)
        cto.add_child(infras_head)
        cto.add_child(TreeNodeOne([ 'Aaamir', 'Application HEAD' ]))
        infras_head.add_child(TreeNodeOne([ 'Dhaval', 'Cloud Manager' ]))
        infras_head.add_child(TreeNodeOne([ 'Abhijit', 'App  Manager' ]))
        hr_head.add_child(TreeNodeOne([ 'Peter', 'Recruitment Manager' ]))
        hr_head.add_child(TreeNodeOne([ 'Waqas', 'Policy Manager' ]))
        ceo.print_tree( 'name')



        
        
# Question 2
class TreeNodeTwo:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree_authors_solution(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix  =  spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree_authors_solution(level)


def build_tree_two():
    root = TreeNodeTwo("Global")

    india = TreeNodeTwo("India")

    gujarat = TreeNodeTwo("Gujarat")
    gujarat.add_child(TreeNodeTwo("Ahmedabad"))
    gujarat.add_child(TreeNodeTwo("Baroda"))

    karnataka = TreeNodeTwo("Karnataka")
    karnataka.add_child(TreeNodeTwo("Bangluru"))
    karnataka.add_child(TreeNodeTwo("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNodeTwo("USA")

    nj = TreeNodeTwo("New Jersey")
    nj.add_child(TreeNodeTwo("Princeton"))
    nj.add_child(TreeNodeTwo("Trenton"))

    california = TreeNodeTwo("California")
    california.add_child(TreeNodeTwo("San Francisco"))
    california.add_child(TreeNodeTwo("Mountain View"))
    california.add_child(TreeNodeTwo("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root 
            

            
            

        

if __name__ == "__main__":
    # build_tree()
    root_node  = build_tree_two()
    root_node.print_tree_authors_solution(1)
