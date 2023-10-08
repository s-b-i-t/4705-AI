class Node:
    def __init__(self, value):
        self.value = value
        self.adj_nodes = {} # key = adjacent node object : value = distance
        self.prev = None

class Graph:
    def __init__(self):
        self.nodes = []
        self.cities = {} # key = city name : value = node object

    def add_node(self, value):
        if isinstance(value, Node):
            self.nodes.append(value)
            return value
        
        new_node = Node(value)
        self.nodes.append(new_node)
        return new_node

    def add_edge(self, node1, node2, distance=None):
        node1.adj_nodes[node2] = distance
        node2.adj_nodes[node1] = distance


    def add_cities(self, locations): #add locations from a dictionary to graph
        for city in locations:
            if city not in self.cities:
                Source_Node = self.add_node(city)
                self.cities[city] = Source_Node
            else:
                Source_Node = self.cities[city]
            
            for neighbor in locations[city]:
                if neighbor not in self.cities:
                    Destination_Node = self.add_node(neighbor)
                    self.cities[neighbor] = Destination_Node
                else:
                    Destination_Node = self.cities[neighbor]
                
                self.add_edge(Source_Node, Destination_Node, locations[city][neighbor])

        
    
    #Reset Node pointers to run next algo
    def reset_prev_pointers(self):
        for node in self.nodes:
            node.prev = None


    # traverse previous nodes, format, then return path as string
    def sol_found(self, start_node, node):
        goal_node = node
        path = []
        distance = 0
        path_str = ""
    
        while (node.prev != None):
            cur_node = node
            path.append((cur_node, cur_node.adj_nodes[node.prev]))
    
            distance += cur_node.adj_nodes[node.prev]
    
            node = node.prev
    
        path.append((start_node, 0))
    
        for node, dist in path[::-1]:
            path_str += str(node.value)
            if node != goal_node:
                path_str += f" [cost = {dist}] -> "
            else:
                path_str += f" [cost = {dist}]"
    
        path_str += f"\ntotal distance= {distance}"
        return path_str
    
