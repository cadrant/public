import operator
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
	#print distance_from_start
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
    # Open IMDB File and parse into a dictionray which would be a bipartite graph
    with open("imdb-1.tsv") as f:
        name_collection = f.readlines()
        for entry in name_collection:
            entry.rstrip()
            fields = entry.split("\t");
            name = fields[0]
            if not actors.has_key(name):
                movies = []
                movies.insert(0,fields[1] + " " + fields[2])
                actors[name] = movies 
            else:
                actors[name].insert(0,fields[1]+fields[2])

    #Create clique style graph based on bipartite
    G = {} #our clique
    for actor in actors:
        for other_actor in actors:
            if actor != other_actor:
                shared_movies = set(actors[actor]) & set(actors[other_actor])
                if len(shared_movies) != 0:
                    #print actor, "and", other_actor, "were in", shared_movies
                    make_link(G,actor,other_actor)

    #Create a double list associating centrality and actor
    C = []
    for actor in actors:
        t = [actor, 0]
        C.insert(0,t)
        C[0][1] = centrality(G,actor)

    C.sort(key=operator.itemgetter(1), reverse=False)
    print C[20]
test()

