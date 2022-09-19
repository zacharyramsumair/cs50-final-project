from serpapi import GoogleSearch
import os
import csv

SERPAPI_KEY = os.environ["SERPAPI_KEY"]

header = ["name", "images"]


with open("projectTest.csv", "r") as csvFile:
    csv_reader = csv.reader(csvFile)

    with open("images.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        next(csv_reader)
        for line in csv_reader:
            params = {
                "q": line[0],
                "tbm": "isch",
                "ijn": "0",
                "api_key": SERPAPI_KEY,
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            images_results = results["images_results"]

            # write the data
            data = [line[0], images_results[:5]]
            writer.writerow(data)


# query = "New York"

# params = {
#     "q": query,
#     "tbm": "isch",
#     "ijn": "0",
#     "api_key": SERPAPI_KEY,
# }

# search = GoogleSearch(params)
# results = search.get_dict()
# images_results = results["images_results"]
# print(images_results)
# print("======================")
# print(images_results[5])


# header = ["name", "map", "local_map", "sights", "images"]


# with open("projectTest.csv", "r") as csvFile:
#     csv_reader = csv.reader(csvFile)

#     with open("projectTest2.csv", "w", encoding="UTF8") as f:
#         writer = csv.writer(f)

#         # write the header
#         writer.writerow(header)

#         next(csv_reader)
#         for line in csv_reader:
#             # write the data
#             data = [line[0], line[0] + " map", 0, 0, 0]
#             writer.writerow(data)
