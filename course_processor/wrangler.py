import json


# Bubble sort algorithm to sort the courses json, and disgard unnecessary nesting of objects.
def wrangle_courses(unnest):
    f = open('courses.json')
    courses = json.load(f)

    f_req = open('requisites.json')
    reqs = json.load(f_req)
    if unnest:
        courses = courses["Items"]
    for i in range(1, len(courses)):
        for j in range(len(courses) - i):

            if courses[j]["CourseCode"] > courses[j + 1]["CourseCode"]:
                temp = courses[j + 1]["CourseCode"]
                courses[j + 1]["CourseCode"] = courses[j]["CourseCode"]
                courses[j]["CourseCode"] = temp

            if reqs[j]["courseCode"] > reqs[j + 1]["courseCode"]:
                temp = reqs[j + 1]["courseCode"]
                reqs[j + 1]["courseCode"] = reqs[j]["courseCode"]
                reqs[j]["courseCode"] = temp

    f = open('courses.json', 'w')
    f_req = open('requisites.json', 'w')
    f_req.write(json.dumps(reqs, indent=4))
    f.write(json.dumps(courses, indent=4))


wrangle_courses(False)
