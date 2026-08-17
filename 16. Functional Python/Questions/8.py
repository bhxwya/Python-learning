names = ["Ansh", "Rahul", "Aman", "Keshav", "Riya", "Arjun"]

new_individuals = list(filter(lambda x : len(x)>4, names))
print(new_individuals)