import json

f = open('requisites.json', 'r')
data = json.load(f)

longest = ''
longestLength = 0

for req in data:
    if len(req["req"]) > longestLength:
        longestLength = len(req["req"])
        longest = req
print(longest["req"])
print(longestLength)