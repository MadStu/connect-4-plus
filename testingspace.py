import csv

# https://www.pythontutorial.net/python-basics/python-write-csv-file/

top_scores = []

with open('scores.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader):
        top_scores.append(line)
        top_scores[line_no][0] = int(top_scores[line_no][0])

#print(top_scores)

with open('scores.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)

    # write csv rows
    writer.writerows(top_scores)

top_scores.sort(reverse = True)

i=0
while i < 10:
    print(top_scores[i])
    i += 1
