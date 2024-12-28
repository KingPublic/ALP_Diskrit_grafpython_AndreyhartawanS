import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.show()

    def shortest_path(self, start, end):
        return nx.shortest_path(self.graph, source=start, target=end, weight='weight')

    def visual_shortest_path(self, start, end):
        path = self.shortest_path(start, end)
        edges = list(zip(path, path[1:]))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color='red', width=2)
        plt.show()

    # Metode tambahan
    def is_connected(self):
        return nx.is_connected(self.graph)

    def node_degrees(self):
        return dict(self.graph.degree())

    def connected_components(self):
        return list(nx.connected_components(self.graph))

    def graph_diameter(self):
        if nx.is_connected(self.graph):
            return nx.diameter(self.graph)
        else:
            return "Graph is not connected"

    def has_cycle(self):
        try:
            nx.find_cycle(self.graph)
            return True
        except nx.exception.NetworkXNoCycle:
            return False

# Implementasi
if __name__ == "__main__":
    graph = Graf()

    # Menambah Node
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    # Menambah Edge
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)

    # Visualisasi Graf
    print("Visualisasi Graf:")
    graph.visualize_graph()

    # Jalur Terpendek
    print("Jalur Terpendek dari 1 ke 5:")
    print(graph.shortest_path(1, 5))

    # Visualisasi Jalur Terpendek
    print("Visualisasi Jalur Terpendek:")
    graph.visual_shortest_path(1, 5)

    # Metode tambahan
    print("Apakah graf terhubung?:", graph.is_connected())
    print("Derajat tiap node:", graph.node_degrees())
    print("Komponen terhubung:", graph.connected_components())
    print("Diameter graf:", graph.graph_diameter())
    print("Apakah graf memiliki siklus?:", graph.has_cycle())
