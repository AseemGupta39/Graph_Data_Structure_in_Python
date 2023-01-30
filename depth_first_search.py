def dfs(graph,node,visited = set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)


ipt = [[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]

graph = {}

n = 6

for i in range(1,n+1):
    graph[i] = []

for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)


for key,value in graph.items():
    print(f"{key} : {value}")

dfs(graph=graph,node=1)
