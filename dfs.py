#5) Write a Program to Implement Depth First Search
def dfs(graph, start, target, visited=None):
if visited is None:
visited = set()
visited.add(start)
print(start)
if start == target:
return True

for next_node in graph[start]-visited:
if dfs(graph, next_node, target, visited):
return True
return False

graph = {
'0': {'1', '2'},
'1': {'0', '3', '4'},
'2': {'0'},
'3': {'1'},
'4': {'1'},
}

start_node = '0'
target_node = '4'

if dfs(graph, start_node, target_node):
print(f"Node {target_node} found!")
else:
print(f"Node {target_node} not found!")