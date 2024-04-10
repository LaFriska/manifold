import json
import scraper

f = open('requisites.json')
data = json.load(f)
for i in range(len(data)):
    cc = data[i]["courseCode"]
    req = data[i]["req"]
    if req == f"ERROR: CANNOT FETCH FOR {cc}":
        print(" Fixing \'" + req + "\'")
        data[i]["req"] = scraper.fetch_requisite(cc)
        print(" Found solution: " + data[i]["req"])
f = open('requisites.json', 'w')
f.write(json.dumps(data))