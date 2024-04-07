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

def getURL(courseCode):
    return f"https://programsandcourses.anu.edu.au/2024/course/{courseCode}"

def fetchRequisite(courseCode):
    print("Fetching requisites: " + courseCode)
    response = requests.get(getURL(courseCode))
    soup = BeautifulSoup(response.text, "html.parser")
    req = soup.find("div", {"class": "requisite"})
    if req is not None:
        return req.get_text(strip=True, separator="\n")

    reqTitle = soup.find("h2", {"id": "inherent-requirements"})
    if reqTitle is not None:
        req = reqTitle.find_next("p")
        if req is not None:
            return req.get_text(strip=True, separator="\n")

    reqTitle = soup.find("h2", {"id": "incompatibility"})
    if reqTitle is not None:
        req = reqTitle.find_next("p")
        if req is not None:
            return req.get_text(strip=True, separator="\n")

    print("ERROR: CANNOT FETCH FOR " + courseCode)
    return "Cannot find requisites. Please visit programs & courses."


