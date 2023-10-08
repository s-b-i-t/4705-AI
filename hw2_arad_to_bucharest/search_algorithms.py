from adj_graph import Graph, Node
city_graph = Graph()


locations = {  'Oradea':{'Zerind':71, 'Sibiu':151},
'Zerind':{'Oradea':71, 'Arad':75},
'Arad':{'Zerind':75, 'Sibiu':140, 'Timisoara':118},
'Timisoara':{'Arad':118, 'Lugoj':111},
'Lugoj':{'Timisoara':111, 'Mehadia':70},
'Mehadia':{'Lugoj':70, 'Dobreta':75},
'Dobreta':{'Mehadia':75, 'Craiova':120},
'Sibiu':{'Oradea':151, 'Fagaras':99, 'Rimnicu Vilcea':80, 'Arad':140},
'Rimnicu Vilcea':{'Sibiu':80, 'Pitesti':97, 'Craiova':146},
'Craiova':{'Rimnicu Vilcea':146, 'Pitesti':138, 'Dobreta':120},
'Fagaras':{'Sibiu':99, 'Bucharest':211},
'Pitesti':{'Rimnicu Vilcea':97, 'Bucharest':101, 'Craiova':138},
'Neamt':{'Iasi':87},
'Giurgiu':{'Bucharest':90},
'Bucharest':{'Pitesti':101, 'Fagaras':211, 'Urziceni':85, 'Giurgiu':90},
'Iasi':{'Neamt':87, 'Vaslui':92},
'Urziceni':{'Bucharest':85, 'Vaslui':142, 'Hirsova':98},
'Vaslui':{'Iasi':92, 'Urziceni':142},
'Hirsova':{'Urziceni':98, 'Eforie':86},
'Eforie':{'Hirsova':86} }

city_graph.add_cities(locations)

sld_to_Bucharest = {'Arad':366,
                    'Bucharest':0,
                    'Craiova':160,
                    'Dobreta':242,
                    'Eforie':161,
                    'Fagaras':176,
                    'Giurgiu':77,
                    'Hirsova':151,
                    'Iasi':226,
                    'Lugoj':244,
                    'Mehadia':241,
                    'Neamt':234,
                    'Oradea':380,
                    'Pitesti':100,
                    'Rimnicu Vilcea':193,
                    'Sibiu':253,
                    'Timisoara':329,
                    'Urziceni':80,
                    'Vaslui':199,
                    'Zerind':374
                   }


class PriorityQueue:
    def __init__(self):
        self.queue = [] # key = priority  , value = node object
    
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

#picks node and explores as deep as possible until goal node is found

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
def compute_cost(cur_node):
    cost = 0
    tmp = cur_node
    while tmp.prev is not None:
        cost += tmp.adj_nodes[tmp.prev]
        tmp = tmp.prev
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
                current_cost = compute_cost(adj_node)
                # print(adj_node.value)
                #if these same node.value is in the frontier with a lower cost then update the current cost to that cost
                frontier.put((current_cost, adj_node))
            if frontier.count(adj_node) > 1:
                print(frontier.count(adj_node))
                frontier.remove_occurrences_except_min(adj_node.value)
    return "no path"


# *************************************
# gbfs CODE
# *************************************
def gbfs(self, start_node , end_node):
    if (not isinstance(start_node, Node)):
        start_node = self.cities[start_node]
    if (not isinstance(end_node, Node)):
        end_node = self.cities[end_node]
        
    visited_nodes = set()
    frontier = PriorityQueue()  # (priority, node)
    
    frontier.put((0, start_node))
    while (frontier):
        current_cost, current_node = frontier.get()
        visited_nodes.add(current_node)
        if current_node == end_node:
            return self.sol_found(start_node, current_node)
        for adj_node in current_node.adj_nodes:
            if adj_node not in visited_nodes:
                adj_node.prev = current_node
                # compute cost and put it in frontier (priority queue)
                current_cost = sld_to_Bucharest[adj_node.value] #shortest long distance to Bucharest
                frontier.put((current_cost, adj_node))
            if frontier.count(adj_node) > 1:
                frontier.remove_occurrences_except_min(adj_node.value)


def Astar(self, start_node , end_node):
    if (not isinstance(start_node, Node)):
        start_node = self.cities[start_node]
    if (not isinstance(end_node, Node)):
        end_node = self.cities[end_node]
        
    visited_nodes = set()
    frontier = PriorityQueue()  # (priority, node)
    
    frontier.put((0, start_node))
    
    while (frontier):
        current_cost, current_node = frontier.get()
        visited_nodes.add(current_node)
        if current_node == end_node:
            return self.sol_found(start_node, current_node)
        for adj_node in current_node.adj_nodes:
            if adj_node not in visited_nodes:
                adj_node.prev = current_node
                # compute cost and put it in frontier (priority queue)
                current_cost = sld_to_Bucharest[adj_node.value]
                current_cost += compute_cost(adj_node) #shortest long distance to bucharest + cost to get to current node
                # print(adj_node.value)
                frontier.put((current_cost, adj_node))
            if frontier.count(adj_node) > 1:
                print(frontier.count(adj_node))
                frontier.remove_occurrences_except_min(adj_node.value)



print(f"BFS path: {bfs(city_graph,'Arad', 'Bucharest')}")
city_graph.reset_prev_pointers()

print(f"DFS path: {dfs(city_graph,'Arad', 'Bucharest')}")
city_graph.reset_prev_pointers()

print(f"UCS path: {ucs(city_graph,'Arad', 'Bucharest')}")
city_graph.reset_prev_pointers()

print(f"GBFS path: {gbfs(city_graph,'Arad', 'Bucharest')}")
city_graph.reset_prev_pointers()

print(f"A* path: {Astar(city_graph,'Arad', 'Bucharest')}")
city_graph.reset_prev_pointers()
