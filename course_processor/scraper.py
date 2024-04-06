# Web scraper for ANU courses

import requests
import json


def updateCourseData():
    url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true"
    print("Fetching data from " + url)
    course_data = json.dumps(json.loads(requests.get(url).text), indent=4)
    print("Writing to file")
    f = open("courses.json", "w")
    f.write(course_data)
    print("Complete")


updateCourseData()
