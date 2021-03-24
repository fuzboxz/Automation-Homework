import os
import csv

def createCsv(topcast, path):
    if os.path.exists(path):
        print("Found earlier revision of", path, "on local filesystem, deleting it now")
        os.remove(path)

    with open(file=path, mode="w") as csvfile:
        writer = csv.writer(csvfile)
        for cast in topcast:
            writer.writerow(cast)

def top5(path):
    with open(file=path, mode="r") as f:
        
        top = {}
        
        # Read first line, but discard it right away
        cast = f.readline()

        # Count cast frequency into dictionary and return top 5
        while (True):
            cast = str(f.readline()).strip("\n")
            if cast == "":
                break
            elif cast in top.keys():
                top[cast] = top[cast] + 1
            else:
                top[cast] = 1
        return sorted(top.items(), key=lambda item: item[1], reverse=True)[0:5]
