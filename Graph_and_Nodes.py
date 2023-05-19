#Fully connected Graph class containing nodes
class Graph:
    def __init__(self):
        self.nodes = []
        
    def add_node(self, node_value):
        new_node = Node(node_value)
        self.nodes.append(new_node)

    def set_connections(self, node_1, node_2, weight):
        if node_1 in self.nodes and node_2 in self.nodes:
            node_1.add_neighbor(node_2, weight)
            node_2.add_neighbor(node_1, weight)
        else:
            print('One of these nodes was not created!')

    def remove_connection(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            node_1.remove_neighbor(node_2)
            node_2.remove_neighbor(node_1)
        else:
            print("These nodes aren't neighbors or these nodes aren't in the graph!")

    def print_nodes(self):
        if len(self.nodes) > 0:
            for node in self.nodes:
                print(node)
        else:
            print('There are no nodes in the graph!')

    #Using dijkstra's algorithm to find the shortest path
    def find_shortest_path(self, start_node):
        if len(self.nodes) > 1 and start_node.get_neighbors() != 'there are no neighbors!':
            infinity = float('inf')

            #Assume start node is the start vertex
            vertices = [node for node in self.nodes]
            
            #Removing the start node so that its easier to put it into the distance_from_start_vertex dictionary
            vertices.remove(start_node)

            #Creating a list of visited and unvisited vertices and initializing the unvisited list to have the start vertex at the start
            visited = [] 
            unvisited = [(vertex.value, vertex) for vertex in vertices]
            unvisited.insert(0, (start_node.value, start_node)) #Inserting start node to first spot in unvisited list
            
            #Setting first value in dictionary to start_node
            distance_from_start_vertex = {}  

            distance_from_start_vertex[start_node.value] = (0, None)
            #Setting first value in dictionary to the start_vertex
            for i in range(1, len(unvisited)):
                distance_from_start_vertex[unvisited[i][0]] = (infinity, None)
                
            #Algorithm start
            #Unvisited values contain (node_value, node)
            while len(unvisited) > 0:
                #Greedy part of algorithm
                curr_vertex = unvisited[0] 
                
                for vertex in unvisited: 
                    if distance_from_start_vertex[vertex[0]][0] < distance_from_start_vertex[curr_vertex[0]][0]:
                        curr_vertex = vertex
                for neighbor in curr_vertex[1].get_neighbors(): #Neighbor values are in tuple (node, weight)
                    if neighbor[0].value in [value[0] for value in unvisited]:
                        calculated_distance = neighbor[1] + distance_from_start_vertex[curr_vertex[0]][0]
                        if calculated_distance < distance_from_start_vertex[neighbor[0].value][0]:
                            distance_from_start_vertex[neighbor[0].value] = (calculated_distance, curr_vertex)
                    else:
                        continue

                visited.append(curr_vertex)
                unvisited.remove(curr_vertex)

            return distance_from_start_vertex
        pass
            
#Node class containing nodes with neighbors
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    
    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value
    
    def add_neighbor(self, new_neighbor, weight):
        if len(self.neighbors) > 0:
            neighbor_to_be_replaced = None
            for neighbor in self.neighbors:
                if neighbor[0] == new_neighbor:
                    neighbor_to_be_replaced = neighbor
                    self.neighbors.remove(neighbor_to_be_replaced)
                    self.neighbors.append([new_neighbor, weight])
                    break
            if neighbor_to_be_replaced == None:
                self.neighbors.append([new_neighbor, weight])
        else:
            self.neighbors.append([new_neighbor, weight])
            

    def get_neighbors(self):
        if len(self.neighbors) > 0:
            for neighbor in self.neighbors:
                #print(neighbor[0].value, neighbor[1])
                pass
            return self.neighbors
        else:
            return 'there are no neighbors!'

    def remove_neighbor(self, node):
        if len(self.neighbors) > 0:
            neighbor_to_be_removed = None
            for neighbor in self.neighbors:
                if neighbor[0] == node:
                    neighbor_to_be_removed = neighbor
                    self.neighbors.remove(neighbor_to_be_removed)
                    break
            print('Node not a neighbor!')

# """Uncomment if you want to use this test code"""
# graph = Graph()
# graph.add_node('san francisco') #a
# graph.add_node('oakland') #b
# graph.add_node('berkeley') #c
# graph.add_node('daly city') #d

# graph.set_connections(graph.nodes[0], graph.nodes[1], 1)
# graph.set_connections(graph.nodes[0], graph.nodes[2], 4)
# graph.set_connections(graph.nodes[1], graph.nodes[3], 6)
# graph.set_connections(graph.nodes[1], graph.nodes[2], 2)
# graph.set_connections(graph.nodes[2], graph.nodes[3], 1)

# print(graph.find_shortest_path(graph.nodes[1]))




