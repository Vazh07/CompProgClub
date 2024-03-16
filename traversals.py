import queue


def get_adj(graph, vertex):
    vs = []
    for s in graph:
        if s[0] == vertex:
            vs.append(s[1])
    return vs


def order_bfs(graph, start_node):
    order = []
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    while not q.empty():
        v = q.get()
        if v not in visited:
            order.append(v)
            visited.add(v)
            for node in get_adj(graph, v):
                if node not in visited:
                    q.put(node)
    return order


g = [[0,1],[0,2],[0,3],[1,3],[2,3],[3,4]]
ddfs=[]
marked = []
def visit(node):
    ddfs.append(node)
def neighbors(graph,node):
    ns=[]
    for ni in graph:
        if ni[0]==node[1]:
            ns.append(ni)
    return ns
def dfs(graph, node):
    visit(node)
    marked.append(node)
    for w in neighbors(graph,node):
        if w not in marked:
            dfs(graph, node)
def dfs_iter(graph,v):
    stack = [v]
    while len(stack)>0:
        v=stack.pop()
        if v not in marked:
            visit(v)
            marked.append(v)
            for w in neighbors(graph,v):
                if w not in marked:
                    stack.append(w)

dfs_iter(g,[0,1])
print(ddfs)
print(order_bfs([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')],'A'))
