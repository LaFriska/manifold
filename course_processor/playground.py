import json

f = open('courses.json')
courses = json.load(f)

shortest = 20
curr = "aaaaaaaaaaaaaaaaaaaaaa"
for i in range(len(courses)):
    if len(courses[i]['CourseCode']) < shortest:
        shortest = len(courses[i]['CourseCode'])
        curr = courses[i]['CourseCode']
print(curr)