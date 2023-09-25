    def ucs(self, start_node, end_node):
        if not isinstance(start_node, Node):
            start_node = self.cities[start_node]
        if not isinstance(end_node, Node):
            end_node = self.cities[end_node]
    
        visited_nodes = set()
        frontier = PriorityQueue()
        frontier.put((0, start_node))
    
        # Dictionary to keep track of costs
        costs = {node: float('inf') for node in self.nodes}
        costs[start_node] = 0
    
        while not frontier.empty():
            current_cost, current_node = frontier.get()
            visited_nodes.add(current_node)
    
            if current_node == end_node:
                return self.sol_found(start_node, current_node)
    
            for adj_node, edge_cost in current_node.adj_nodes.items():
                new_cost = current_cost + edge_cost
                if new_cost < costs[adj_node]:
                    adj_node.prev = current_node
                    costs[adj_node] = new_cost
                    frontier.put((new_cost, adj_node))
    
        return "no path"
