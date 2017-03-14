import operator;

# We have to sort so we need lists
most_popular = []

with open("yob.txt") as f:
    name_collection = f.readlines()
    for entry in name_collection:
        entry.rstrip()
        fields = entry.split(",")
        name = fields[0]
        amount = int(fields[2])
        if(fields[1] == "F"):
            most_popular.insert(0,fields)
            most_popular[0][2] = int(fields[2])
    most_popular.sort(key=operator.itemgetter(2), reverse=True)
            
print most_popular[1][0], "is the most popular with", most_popular[1][2] 
