# Rewrite `mark_component` to not use recursion 
# and instead use the `open_list` data structure 
# discussed in lecture
#

def mark_component_recursive(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        print "Node: ", node, " neighbor ", neighbor
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked
    
def mark_component(G, node, marked):
    #1.) Add neighbors to ol
    #2.) Pop last of ol
        #Mark
    #Repeat until ol
    open_list = []
    total_marked = 0
    open_list.append(node)
    while open_list:
        node = open_list[-1]
        marked[node] = True
        total_marked += 1
        for neighbor in G[node]:
            if neighbor not in open_list and not marked.has_key(neighbor):
                print "Adding ", neighbor
                open_list.append(neighbor)
            #open_list.extend(G[neighbor])
        print "Removing ", node
        open_list.remove(node)
        if total_marked > 10:
            break
    return total_marked

#########
# Code for testing
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    #test_edges = [(1, 2), (2, 3), (1, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    #mark_component_recursive(G,1,marked)
    assert mark_component(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked
test()

