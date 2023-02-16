def dfs(graph,node,visited,par):
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            return dfs(graph,child,visited,node)
        else:
            if child != par:
                return True
    return False


ipt=[[1,2],[1,3],[2,3],[2,4],[4,5],[5,1]]
n=5
graph,visited={},{}
for i in range(1, n+1):
    graph[i]=[]
    visited[i]=False

for (u,v) in ipt:
    graph[u].append(v) 
    graph[v].append(u)

temp = dfs(graph,1,visited,-1)
print(temp)       


