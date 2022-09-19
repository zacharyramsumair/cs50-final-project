from unittest import result
from serpapi import GoogleSearch
import os
import csv

SERPAPI_KEY = os.environ["SERPAPI_KEY"]

header = ["name", "map", "sights", "description"]

import json

with open("projectTest.csv", "r") as csvFile:
    csv_reader = csv.reader(csvFile)

    with open("otherInfo.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        next(csv_reader)
        for line in csv_reader:
            params = {
                "q": line[0],
                "hl": "en",
                "gl": "us",
                "google_domain": "google.com",
                "api_key": SERPAPI_KEY,
            }

            search = GoogleSearch(params)
            results = search.get_dict()

            with open("other.txt", "w", encoding="UTF8") as f:
                op = json.dumps(results)

                f.write(op)

            try:
                map = results["knowledge_graph"]["local_map"]["link"]
            except:
                map = ""

            try:
                sights = results["top_sights"]["sights"]
            except:
                sights = ""
            try:
                description = results["knowledge_graph"]["description"]
            except:
                description = ""

            # write the data
            data = [line[0], map, sights, description]
            writer.writerow(data)


# params = {
#     "q": "new York",
#     # "location": "Austin, Texas, United States",
#     "hl": "en",
#     "gl": "us",
#     "google_domain": "google.com",
#     "api_key": "a41712daf04199723535e4d07f2f37d368aeef8ad92fb85ea37685bed12517f3",
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# with open("convert.json", "w") as convert_file:
#     convert_file.write(json.dumps(results))


# results_json = json.dumps(results)


# print(results_json["search_metadata"])
# print("===========================")
# print("map")
# print(results["search_information"]["menu_items"][2])
# print("===========================")

# print("sights")
# print(results["top_sights"]["sights"])
# print("===========================")

# print("local map")
# print(results["knowledge_graph"]["local_map"])
# print("===========================")


# results


# $ python location.py
# https://serpapi.com/search
# ===========================
# map
# {'position': 3, 'title': 'Maps', 'link': 'https://maps.google.com/maps?hl=en&gl=us&q=new+York&um=1&ie=UTF-8&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ_AUoAnoECAIQBA'}
# ===========================
# sights
# [{'title': 'Central Park', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/09c7v&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAB6BAhlECU', 'description': 'Urban oasis with ballfields & a zoo', 'rating': 4.8, 'reviews': 239469, 'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh-5gjeszvn43wAwPpaaLjaI_jfgeKHrwWH3wVvRCRozwNwxsS6SHzviB_YKl5nD_UywaAoAGdKxKowuat4U5wyHD8'}, {'title': 'The Metropolitan Museum of Art', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/09c7b&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAF6BAhlECc', 'description': 'World-class art collection', 'rating': 4.8, 'reviews': 69615, 'thumbnail': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRrhQ3RYJmK5BcO7mtV24A-1i9s1VA9NaY1czMaqSloGQ5GKkiu3Eq6Q5UmBWUuz_FCZOjiTngdzJoxsUmS7y8-au6I'}, {'title': 'The Museum of Modern Art', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/0hhjk&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAJ6BAhlECk', 'description': 'World-class sculpture, art & design', 'rating': 4.6, 'reviews': 39707, 'thumbnail': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTM3S5rW5lUriojtooCQ9zmexJb6EgA_whwR7_p-sv6VWw_Seqq09j2m5DF_wpjxcZ5-y3HY5Yp5-4ncdp9G_6N3ehU'}, {'title': 'Statue of Liberty', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/072p8&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAN6BAhlECs', 'description': 'American icon in New York Harbor', 'rating': 4.7, 'reviews': 84197, 'thumbnail': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT4_pMciJ178al7NGaVDYZhCAcJNCNUBjTyqU66ztXoVWLs2OeEa0HBSiZoQMC7_d4Vsu-80upaUcl21IrI_LFEBbHk'}, {'title': 'Empire State Building', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/02nd_&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAR6BAhlEC0', 'description': '103-story landmark with observatories', 'rating': 4.7, 'reviews': 83747, 'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGwicnqvbdXpD8hHjGGHu5P1ZJjjxRKhS6sLDWMsObtEDa1fc-XvpSK7_qX39WVFIsvMs3LbTuG48h5MTUPrpkJXl1'}, {'title': 'Solomon R. Guggenheim Museum', 'link': 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548,2503771,2503781,4258168,4270442,4284970,4291517,4306835,4308227,4597339,4703207,4718358,4723331,4757164,4786958,4790928,4809518,4814050,4816977,4828448,4829505,4832717,4836614,4838766&hl=en-US&gl=us&ssta=1&dest_mid=/m/02_286&dest_state_type=sattd&dest_src=ts&q=&poi_mid=/m/0q9h2&sa=X&ved=2ahUKEwjX5bHwwvT5AhVUB4gKHcG9BEIQ69EBKAV6BAhlEC8', 'description': 'Modern-art museum with a notable design', 'rating': 4.4, 'reviews': 18251, 'thumbnail': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSo37_ZjfHL1eNqO8JVO2gedrvj0Kh_n9jChiDkUKGQHDirLi7rOrlak2EnqR6U3UhXVn6LvtCYcXpQu3AIoDVy5bky'}]
# ===========================
# local map
# {'image': 'https://www.google.com/maps/vt/data=pKutU30vmWYQC9m8nxguyEuKlJU9Sg8tSfkuyu8VuGwk40zCl2ahZRWln-lPowX58hHGxQNyt5xu0JhbMnOhkYUN97PYPelaK1z3joVgEykZQeyEJVlOKyVRdrASg9Ov7s5Csee-9MVhHneMVYkzaQ6MqlAz-x5V_LKnETXEvreFDSY5K1f2e6nGI9OaYXa2E3tSOgAqCLTrO2kj1uGR-F9KE51A5fwsgnEHaY-sqB_sdNUO8SrSFUSK', 'link': 'https://www.google.com/maps/place/New+York,+NY/data=!4m2!3m1!1s0x89c24fa5d33f083b:0xc80b8f06e177fe62?sa=X&hl=en&gl=us'}
# ===========================
