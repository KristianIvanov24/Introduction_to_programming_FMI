results = (("Megan", 22.4, 23, 22.8), ("Alan", 20.9, 20.3, 21), ("Tonny", 21, 21.1, 20.95))

average_results = ()
for person in results:
    sum = 0
    for i in range(1, 4):
        sum += person[i]
    average_results += (person[0], round(sum/3, 2)),

print(average_results)
sorted_results = []

while len(average_results) > 0:
    min_tuple = average_results[0]
    for j in range(1, len(average_results)):
        if average_results[j][1] < min_tuple[1]:
            min_tuple = average_results[j]
    sorted_results.append(min_tuple)
    new_results = ()
    for t in average_results:
        if t != min_tuple:
            new_results += (t,)
    average_results = new_results

sorted_results = tuple(sorted_results)
print(sorted_results)
for name, time in sorted_results:
    print(f"{name}'s average result from the competition is {time} s.")


