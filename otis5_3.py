
import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
  G = nx.Graph()
  G.name = input ("Graph name: " )
  while(input("Do you want to add node(y/n)")=='y'):
    node_name = input("Enter node info: ")
    G.add_node(node_name)
  if(G.number_of_nodes()>=2):
    while(input("Do you want to add edge to nodes(y/n)")=='y'):
      source_node = input("Enter the source node: ")
      target_node = input("Enter the target node: ")
      if source_node in G.nodes() and target_node in G.nodes():
        G.add_edge(source_node, target_node)
  return G 

def add_node(graph):
  node_name = input("Enter node info: ")
  graph.add_node(node_name)
def rename_graph():
  G.name = input("New graph name: ")
  return G

def print_graph(graph):
    plt.figure()
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

def create_edge():
  source_node = input("Enter the source node: ")
  target_node = input("Enter the target node: ")
  if source_node in G.nodes() and target_node in G.nodes():
    G.add_edge(source_node, target_node)
  else:
    print(f"Node {source_node} or {target_node} not found in the graph.")
  return G

def remove_edge(source_node, target_node,graph):
  if source_node in G.nodes() and target_node in G.nodes():
    graph.remove_edge(source_node, target_node)
  else:
    print(f"Node {source_node} or {target_node} not found in the graph.")
  

def rename_node(old_node, new_node, graph):
  if old_node in graph.nodes() and new_node not in graph.nodes():
    graph = nx.relabel_nodes(graph, {old_node: new_node})
    print(f"Node {old_node} has been renamed")
  

def remove_node(node,graph):
  if node in graph.nodes():
    graph.remove_node(node)
  else:
    print(f"Node {node} not found in the graph.")
  return graph

def print_info(graph):
  print ("name:", graph.name)
  print ("Is weight?:", nx.is_weighted(graph))
  print ("number of nodes:", graph.number_of_nodes())
  print ("number of edges:", graph.number_of_edges())
  print_graph(graph)
  
  

def move_node( graph):
  node = input("Enter a node that you need to move")
  new_position_x = input("Enten a new coordinate x ")
  new_position_y = input("Enten a new coordinate y ")
  if node in graph.nodes():
        graph.nodes[node]['pos'] = (new_position_x,new_position_y)
  else:
        print(f"Node {node} not found in the graph.")
  print_graph(graph)
  return graph

def is_tree(graph):
  return print(nx.is_tree(graph))

def get_incidence_matrix(graph):
  print( nx.incidence_matrix(graph))


# def make_binary_tree(graph):
#   return binary_tree

def make_tree(graph):
  return nx.junction_tree(graph)

def find_hamilton_cycles(graph):
    cut_vertices = list(nx.articulation_points(graph))
    cut_edges = list(nx.bridges(graph))
    if not cut_edges and not cut_vertices:
        cycles = list(nx.find_cycle(graph))
        if cycles:
            print("Hamiltonian cycles found:")
            for cycle in cycles:
                print(cycle)
        else:
            print("Your graph does not have any Hamiltonian cycles.")
    else:
        print("Your graph contains cut vertices or cut edges, so it does not have any Hamiltonian cycles.")

def find_eulerian_cycles(graph): #this function is search in graphs like G=nx.complete_graph(3)
    eulerian_cycles = list(nx.eulerian_circuit(graph))
    print("Eulerian cycles found:")
    for cycle in eulerian_cycles:
        print(cycle)

def find_all_path_between_two_nodes(graph):
  print_graph(graph)
  source_node = input("Enter the source node: ")
  target_node = input("Enter the target node: ")
  all_paths = list(nx.all_simple_paths(graph, source_node, target_node))
  # Вывод всех найденных путей
  for path in all_paths:
      print(path)
def find_shortest_path_between_two_nodes(graph):
  source_node = input("Enter the source node: ")
  target_node = input("Enter the target node: ")
  all_paths = list(nx.shortest_path(graph, source_node, target_node))
  # Вывод всех найденных путей
  for path in all_paths:
      print(path)


def find_center_graph(graph):
  print("centerOfGraph: ", nx.center(graph))
  plt.figure()
  nx.draw(graph, with_labels=True, font_weight='bold')
  plt.show()



def find_graph_radius(graph): 
  print("radius  of Graph: ", nx.radius(graph))
  print_graph(graph)

def find_graph_diametr(graph):
  print("diametr of Graph: ", nx.diameter(graph))
  print_graph(graph)

def find_cortesian_product(graph1, graph2):
  plt.figure()
  nx.draw(nx.cartesian_product(graph1, graph2), with_labels=True, font_weight='bold')
  plt.show() 

def find_tensor_product(graph1, graph2):
  plt.figure()
  nx.draw(nx.tensor_product(graph1, graph2), with_labels=True, font_weight='bold')
  plt.show() 


G=create_graph()
isCycle=True
while(isCycle):
  choice=int(input("Choose operation:\n1.Add node\n2.Add edge\n3.Remove edge\n4.Rename node\n5.Remove node\n6.Print info\n7.Move node\n8.Is tree\n9.Get incidence matrix\n10.Make tree\n11.Find Hamiltonian cycles\n12.Find Eulerian cycles\n13.Find all paths between two nodes\n14.Find shortest path between two nodes\n15.Find center of graph\n16.Find radius of graph\n17.Find diametr of graph\n18.Find cortesian product\n19.Find tensor product\n"))
  if choice ==0:
    print_graph(G)
    continue
  if choice==1:
    add_node(G)
    continue
  elif choice==2:
    G=create_edge()
    continue
  elif choice==3:
    source_node=input("Enter source node: ")
    target_node=input("Enter target node: ")
    G=remove_edge(source_node, target_node,G)
    continue
  elif choice==4:
    old_node=input("Enter old node name: ")
    new_node=input("Enter new node name: ")
    G=rename_node(old_node, new_node, G)
    continue
  elif choice==5:
    node=input("Enter node: ")
    G=remove_node(node, G)
    continue
  elif choice==6:
    print_info(G)
    continue
  if choice==7:
    node=input("Enter node: ")
    move_node(node, G)
    continue
  elif choice==8:
    is_tree(G)
    continue
  elif choice==9:
    get_incidence_matrix(G)
    continue
  elif choice==10:
    make_tree(G)
    continue
  elif choice==11:
    find_hamilton_cycles(G)
    continue
  elif choice==12:
    find_eulerian_cycles(G)
    continue
  elif choice==13:
    find_all_path_between_two_nodes(G)
    continue
  elif choice==14:
    find_shortest_path_between_two_nodes(G)
    continue
  elif choice==15:
    find_center_graph(G)
    continue
  elif choice==16:
    find_graph_radius(G)
    continue
  elif choice==17:
    find_graph_diametr(G)
    continue
  elif choice==18:
    F=create_graph()
    find_cortesian_product(G, F)
    continue
  elif choice==19:
    F=create_graph()
    find_tensor_product(G, F)
    continue
  else:
    isCycle=False