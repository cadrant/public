#
# centrality 
#

def centrality(G, v):
    # your code here
	distance_from_start = {}
	open_list = [v]
	distance_from_start[v] = 0
	while len(open_list) > 0:
		current = open_list[0]
		del open_list[0]
		for neighbor in G[current].keys():
			if neighbor not in distance_from_start:
				distance_from_start[neighbor] = distance_from_start[current] + 1
				open_list.append(neighbor)
	print distance_from_start
	return max(distance_from_start.values())

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

actors = {}

def test():
    # Open IMDB File and parse into a list
    # What will the list look like?
    current_actor = "Nobody"
    with open("imdb-1.tsv") as f:
        name_collection = f.readlines()
        for entry in name_collection:
            entry.rstrip()
            fields = entry.split("\t");
            name = fields[0]
            if not actors.has_key(name):
                print name
                movie = fields[1]
                date = int(fields[2])
                actors[name] = movie 
    print actors[0]
    print actors[1]

    #chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    #G = {}
    #for n1, n2 in chain:
        #make_link(G, n1, n2)
    #assert centrality_max(G, 1) == 5
    #assert centrality_max(G, 3) == 3
    #tree = ((1, 2), (1, 3),
            #(2, 4), (2, 5),
            #(3, 6), (3, 7),
            #(4, 8), (4, 9),
            #(6, 10), (6, 11))
    #G = {}
    #for n1, n2 in tree:
        #make_link(G, n1, n2)
    #assert centrality_max(G, 1) == 3
    #assert centrality_max(G, 11) == 6
test()
