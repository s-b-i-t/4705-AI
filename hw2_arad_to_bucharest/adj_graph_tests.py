from adj_graph import Graph, Node

 
graph = Graph()


# node1 = graph.add_node(1)
# node2 = graph.add_node(2)
# node3 = graph.add_node(3)
# node4 = graph.add_node(4)
# node5 = graph.add_node(5)

# graph.add_edge(node1, node2,1)
# graph.add_edge(node2, node3,2)
# graph.add_edge(node3, node4,3)
# graph.add_edge(node4, node5,4)


 # for node in graph.nodes:
#     for adjnode in node.adj_nodes:
#         print(f"node: {node.value}     adj node: {adjnode.value}    distance:  {node.adj_nodes[adjnode]}")

 # print(graph.dfs(node1,node5))


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





graph.add_cities(locations)

# for city in graph.cities:
#     print(city)
    
print(graph.dfs("Oradea","Bucharest"))

print(graph.ucs("Arad","Bucharest"))

# print(graph.gbfs("Arad","Bucharest"))

# print(graph.Astar("Arad","Bucharest"))


