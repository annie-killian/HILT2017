import csv
with open('csvs/basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]

new_row = [2,'graham','wayne','meh']
names.append(new_row)

another_new_row = [3, 'Killian', 'Annie', 'super cool']
names.append(another_new_row)


len(names)

# find the length of each first name
for row in names:
    print(len(row[2]))

# find the longest first name
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row[2]
print(longest)

# construct a new list consisting of only the last names we have here.
last_names = [row[1] for row in names]
last_names.reverse()
print(last_names)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i + 30])


print(data)

# with open('csvs/practice.csv', 'r') as fin:
#     our_reader = csv.reader(fin)
#     data = [row for row in our_reader]
# print(data)
