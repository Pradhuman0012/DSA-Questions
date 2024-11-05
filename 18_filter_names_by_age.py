peoples = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28},
    {"name": "Ethan", "age": 42}
]

res=[]
for people in peoples:
    if people['age']>30:
        res.append(people['name'])
print(res)


# ---------------------
# output
# ['Charlie', 'Ethan']