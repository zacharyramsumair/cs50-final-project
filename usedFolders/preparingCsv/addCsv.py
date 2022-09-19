import csv

header = ["name", "map", "sights", "description", "images"]

import csv

with open("otherInfo.csv", "r") as csvinput1:
    with open("images.csv", "r") as csvinput2:
        with open("output.csv", "w") as csvoutput:
            writer = csv.writer(csvoutput)
            writer.writerow(header)
            for row in csv.reader(csvinput1):
                writer.writerow(row + ["images"])
