import csv
with open('csvs/ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]
# print(names[2)

# all_texts = [row[4] for row in names]
# all_texts.reverse()
# print(all_texts)

all_dates = [row[3] for row in names]
# all_dates.reverse()
# print(all_dates)

# min(all_dates)
# print(min(all_dates))
# print(max(all_dates))

column_headings = {'0': 'id of text', '1': 'full filename from within the index folder', '2':'journal title', '3': 'publication date', '4': 'text of article'}
names.append(column_headings)
# print(names)

# with open('csvs/ripper.csv', 'w') as fout:
#     csvwriter = csv.writer(fout)
#     for row in column_headings:
#         csvwriter.writerow(row)
#         print(column_headings)


with open('csvs/ripper.csv', 'w') as fout:
    column_names = ['id of text', 'full filename from within the index folder', 'journal title', 'publication date', 'text of article']
    dictwriter = csv.DictWriter(fout, fieldnames=column_names)
    dictwriter.writeheader()
    for row in names:
        dictwriter.writerow(row)
