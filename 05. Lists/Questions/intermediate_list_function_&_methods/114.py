my_list = [50, 50, 50, "Ansh", "Ansh", 20, 20, 20, "Ansh", "Ansh"]
result = []

for i in range(0, len(my_list)):
    if my_list[i] not in result:
        result.append(my_list[i])

highest_occurence_element = 0
highest_occurence = 0

for i in range(0, len(result)):
    count = my_list.count(result[i])

    if count > highest_occurence:
        highest_occurence = count
        highest_occurence_element = result[i]

print(f"{highest_occurence_element} occurs {highest_occurence} times")
