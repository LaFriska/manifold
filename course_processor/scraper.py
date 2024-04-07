# Web scraper for ANU courses

import requests
import json
from bs4 import BeautifulSoup


def start():
    url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true"
    print("Fetching data from " + url)
    course_data = json.loads(requests.get(url).text)
    print("Writing to file")
    f = open("courses.json", "w")
    f.write(json.dumps(course_data, indent=4))
    print("Course data updated")
    print("Fetching course requisites.json")
    fetchAllRequisites(course_data['Items'])


def fetchAllRequisites(data):
    requisites = []
    searchSpace = len(data)
    for i in range(searchSpace):
        courseCode = data[i]["CourseCode"]
        log(i, searchSpace)
        requisites.append({"courseCode": courseCode, "req": fetchRequisite(courseCode)})
    print('All requisites.json fetched')
    print('Writing to file')
    f = open("requisites.json", "w")
    f.write(json.dumps(requisites))


def log(i, searchSpace):
    if i == searchSpace // 10:
        print('10% Done')
    if i == searchSpace // (10/2):
        print('20% Done')
    if i == searchSpace // (10/3):
        print('30% Done')
    if i == searchSpace // (10/4):
        print('40% Done')
    if i == searchSpace // (10/5):
        print('50% Done')
    if i == searchSpace // (10/6):
        print('60% Done')
    if i == searchSpace // (10/7):
        print('70% Done')
    if i == searchSpace // (10/8):
        print('80% Done')
    if i == searchSpace // (10/9):
        print('90% Done')


def fetchRequisite(courseCode):
    print("Fetching requisites: " + courseCode)
    response = requests.get(f"https://programsandcourses.anu.edu.au/2024/course/{courseCode}")
    soup = BeautifulSoup(response.text, "html.parser")
    program_requirements = soup.find("div", {"class": "requisite"})
    if program_requirements is None:
        err = "ERROR: CANNOT FETCH FOR " + courseCode
        print(err)
        return err
    return program_requirements.get_text(strip=True, separator="\n")


start()
