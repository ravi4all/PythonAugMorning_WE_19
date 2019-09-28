dataset = {
    "action" : ["thor","hulk","batman","superman","avengers","saaho","kick","ironman","kgf"],
    "comedy" : ["kick","3 idiots","chichore","dhamaal","zero"],
    "biopic" : ["ms dhoni","marykom","sanju"],
    "horror" : ["the nun","the ring","conjuring","anabella"]
}

user = {"thor","hulk","batman","superman","kick","3 idiots","chichore",
        "ms dhoni","marykom","the nun","the ring","conjuring"}

# jaccard distance
# categories = {"action":0.0,"comedy":0.0,"biopic":0.0,"horror":0.0}
categories = {}
for key in dataset:
    categories[key] = 0.0

# print(categories)
for cat in dataset:
    s = len(user.intersection(dataset[cat])) / len(user.union(dataset[cat]))
    categories[cat] = s

print(categories)

cat = list(categories.keys())[list(categories.values()).index(max(list(categories.values())))]


