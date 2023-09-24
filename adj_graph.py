class PriorityQueue:
    def __init__(self):
        self.queue = [] # priority  , value
    
    def sort_queue(self):
        self.queue = sorted(self.queue, key=lambda x: x[0])

    def put(self, node):
        self.queue.append(node)
        self.sort_queue()
    
    def get(self):
        return self.queue.pop(0)
    
    def empty(self):
        return len(self.queue) == 0
    
    def get_queue(self):
        return self.queue
    
    def count(self, node):
        return self.queue.count(node)
    
    def remove_occurrences_except_min(self, node_value):
        occurrences = [n for n in self.queue if n[1].value == node_value]
        if occurrences:
            min_occurrence = min(occurrences, key=lambda x: x[0])
            self.queue = [n for n in self.queue if n[1].value != node_value or n == min_occurrence]


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
            Source_Node = self.add_node(city)
            self.cities[city] = Source_Node
            for neighbor in locations[city]:
                if neighbor not in self.cities:
                    Destination_Node = self.add_node(neighbor)
                    self.add_edge(Source_Node,Destination_Node,locations[city][neighbor])
                else:
                    Destination_Node = self.cities[neighbor]
                    self.add_edge(Source_Node,Destination_Node,locations[city][neighbor])
        

    
    # traverse previous nodes, format, then return path as string
    def sol_found(self,start_node, node):
        goal_node = node
        path = []
        distance = 0
        path_str = ""

        while (node.prev != None):
            cur_node = node
            path.append(cur_node)

            distance += cur_node.adj_nodes[node.prev]

            node = node.prev
                    
        path.append(start_node)

        for node in path[::-1]:
            path_str += str(node.value)
            if node != goal_node:
                path_str += " -> "

                    
        path_str += f"  total distance= {distance}"
        return  path_str

    # *************************************
    # BFS CODE
    # *************************************
    def bfs(self, start_node, end_node):
        if (not isinstance(start_node, Node)):
            start_node = self.cities[start_node]

        if (not isinstance(end_node, Node)):
            end_node = self.cities[end_node]
        visited_nodes = set()
        frontier = []
        visited_nodes.add(start_node)
        frontier.append(start_node)
        while (frontier): # while frontier is not empty
            current_node = frontier.pop(0) #current_node = frontier.get() get first city in frontier

            for adj_node in current_node.adj_nodes: 
                if adj_node not in visited_nodes:
                    adj_node.prev = current_node
                if adj_node == end_node: #if neighbor_node is goal state
                    return self.sol_found(start_node,adj_node)
                #visited_nodes.add(neighbor_node)
                visited_nodes.add(adj_node)
                #frontier.put(neighbor_node)
                frontier.append(adj_node)
        return "no path"

    # *************************************
    # DFS CODE
    # *************************************
    def dfs(self, start_node, end_node):
        if (not isinstance(start_node, Node)):
            start_node = self.cities[start_node]
        
        if (not isinstance(end_node, Node)):
            end_node = self.cities[end_node]
        visited_nodes = set()
        frontier = []
        visited_nodes.add(start_node)
        frontier.append(start_node)
        while (frontier): # while frontier is not empty
            current_node = frontier.pop() #current_node = frontier.get() get last city in frontier (only difference between bfs & dfs)
    
            for adj_node in current_node.adj_nodes: 
                if adj_node not in visited_nodes:
                    adj_node.prev = current_node
                if adj_node == end_node: #if neighbor_node is goal state
                    return self.sol_found(start_node,adj_node)
                #visited_nodes.add(neighbor_node)
                visited_nodes.add(adj_node)
                #frontier.put(neighbor_node)
                frontier.append(adj_node)
        return "no path"
    
    # *************************************
    # UCS CODE
    # *************************************
    def compute_cost(self, cur_node):
        cost = 0
        while cur_node.prev is not None:
            cost += cur_node.adj_nodes[cur_node.prev]
            cur_node = cur_node.prev
            return cost

    def ucs(self, start_node, end_node):
        if (not isinstance(start_node, Node)):
            start_node = self.cities[start_node]

        if (not isinstance(end_node, Node)):
            end_node = self.cities[end_node]
        visited_nodes = set()
        frontier = PriorityQueue()  # (priority, node)

        frontier.put((0, start_node))
        while (frontier):  # while frontier is not empty
            current_cost, current_node = frontier.get()
            visited_nodes.add(current_node)

            if current_node == end_node:
                return self.sol_found(start_node, current_node)

            for adj_node in current_node.adj_nodes:
                if adj_node not in visited_nodes:
                    adj_node.prev = current_node
                    # compute cost and put it in frontier (priority queue)
                    current_cost = self.compute_cost(adj_node)
                    # print(adj_node.value)
                    frontier.put((current_cost, adj_node))

                if frontier.count(adj_node) > 1:
                    frontier.remove_occurrences_except_min(adj_node.value)
        return "no path"














