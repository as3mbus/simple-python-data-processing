import csv;

with open('output.csv', 'w', newline='') as finalFile:
    writer = csv.writer(finalFile)
    writer.writerow("Stuff")