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

G = {} # our clique
M = {} # Movies
C = [] # Centrality

def test():
    # Open IMDB File and parse into a dictionray which would be a bipartite graph
    with open("imdb-1.tsv") as f:
        movie_collection = f.read().splitlines()
        #for entry in f.readlines():
        for entry in movie_collection:
            entry.rstrip()
            fields = entry.split("\t");
            actor = fields[0]
            movie = fields[1] + " " + fields[2]
            movie.rstrip("\n")
            #print movie
            # Have we seen this movie
            if not M.has_key(movie):
                #No? build a list of actors
                A = []
                A.insert(0,fields[0])
                M[movie] = A
            else:
                #Yes? make a link to all the other actors
                for ca in M[movie]:
                    make_link(G,actor,ca)
                #and add it to the list
                M[movie].insert(0,actor)
    movie = "Elf 2003"
    #print movie, "has", M[movie]
    #print M

    #Create a double list associating centrality and actor
    # TODO: need a list of actors!
    C = []
    for actor in A:
        t = [actor, 0]
        C.insert(0,t)
        C[0][1] = centrality(G,actor)

    C.sort(key=operator.itemgetter(1), reverse=False)
    print C
test()

