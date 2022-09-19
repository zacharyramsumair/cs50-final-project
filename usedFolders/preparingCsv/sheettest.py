import csv

# fieldnames = ["name", "map", "local_map", "sights", "images"]

# with open("projectTest.csv", "r") as csvFile:
#     csv_reader = csv.DictWriter(csvFile, fieldnames=fieldnames)

#     with open("projectTest.csv", "w") as goodFile:
#         fieldnames = ["name", "map", "local_map", "sights", "images"]

#         csv_writer = csv.DictWriter(goodFile, fieldnames=fieldnames)
#         csv_writer.writeheader()
#         for line in csv_reader:


# for line in csv_reader:
#     csv_reader.writerow(line["name"], line["name" + map], 0, 0, 0)


header = ["name", "map", "local_map", "sights", "images"]


with open("projectTest.csv", "r") as csvFile:
    csv_reader = csv.reader(csvFile)

    with open("projectTest2.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        next(csv_reader)
        for line in csv_reader:
            # write the data
            data = [line[0], line[0] + " map", 0, 0, 0]
            writer.writerow(data)
