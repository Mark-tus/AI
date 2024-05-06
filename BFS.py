#Write a python/prolog program to implement Breadth First Search Traversal.

def BFS(graph, start_node, target_node):
 visited = set()
 queue = []
 queue.append(start_node)
 visited.add(start_node)

 while queue:
  current_node = queue.pop(0)
  print(current_node, end=" ")
  
  if current_node == target_node:
   print(f"\nTarget node {target_node} found!")
   return True
  
  for neighbor in graph[current_node]:
   if neighbor not in visited:
    queue.append(neighbor)
    visited.add(neighbor)
 print(f"\nTarget node {target_node} not found.")

# Graph representation
graph = {
 '0': {'1', '2'},
 '1': {'0', '3', '4'},
 '2': {'0', '6'},
 '3': {'1'},
 '4': {'1', '5'},
 '5': {'4', },
 '6': {'2'}
}

# Starting node and target node
start_node = '0'
target_node = '4'

# BFS traversal
print("BFS")
BFS(graph, start_node, target_node)