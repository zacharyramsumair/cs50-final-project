postedIDS = "/5/6/2/7/7"
oldIds = "/2/3/4"


newArray = postedIDS.split("/")
oldArray = oldIds.split("/")


newArray = list(dict.fromkeys(newArray))
oldArray = list(dict.fromkeys(oldArray))


newArray.pop(0)
oldArray.pop(0)

for id in range(0,len(newArray)):
    if (newArray[id] not in oldArray):
        oldIds += "/" + newArray[id]
                

print(oldIds)