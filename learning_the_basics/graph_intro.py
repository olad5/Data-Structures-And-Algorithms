class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex_authors_solution(self, vertex):
        if vertex not in self.adj_list.keys() :
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge_authors_solution(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge_authors_solution(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False
        for edge in self.adj_list[vertex]:
            other_vertex  = edge
            self.adj_list[other_vertex].remove(vertex)
        del self.adj_list[vertex]
        return True

    def remove_vertex_authors_solution(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


if __name__ == "__main__":
    gr = Graph()
    gr.add_vertex_authors_solution('A')
    gr.add_vertex_authors_solution('B')
    gr.add_vertex_authors_solution('C')
    gr.add_vertex_authors_solution('D')
    gr.add_edge_authors_solution('A', 'B')
    gr.add_edge_authors_solution('A', 'C')
    gr.add_edge_authors_solution('A', 'D')
    gr.add_edge_authors_solution('B', 'D')
    gr.add_edge_authors_solution('C', 'D')
    gr.print_graph()
    # gr.remove_edge_authors_solution('A', 'B')
    gr.print_graph()
    gr.remove_vertex_authors_solution('D')
    gr.print_graph()
