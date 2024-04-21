# Web scraper for ANU courses

import requests
import json
from bs4 import BeautifulSoup


def start():
    course_data = fetch_all_courses()
    fetch_all_programs()
    fetch_all_requisites(course_data['Items'])


def fetch_all_programs():
    url = "https://programsandcourses.anu.edu.au/data/ProgramSearch/GetPrograms?ShowAll=true"
    print("Fetching data from " + url)
    program_data = json.loads(requests.get(url).text)
    print("Writing to file")
    f = open("backup/programs.json", "w")
    f.write(json.dumps(program_data, indent=4))
    print("Program data updated")


def fetch_all_courses():
    url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true"
    print("Fetching data from " + url)
    course_data = json.loads(requests.get(url).text)
    print("Writing to file")
    f = open("courses.json", "w")
    f.write(json.dumps(course_data, indent=4))
    print("Course data updated")
    return course_data


def fetch_all_requisites(data):
    print("Fetching course requisites.json, this may take 1 - 2 hours.")
    requisites = []
    searchSpace = len(data)
    for i in range(searchSpace):
        courseCode = data[i]["CourseCode"]
        log_req_progress(i, searchSpace)
        requisites.append({"courseCode": courseCode, "req": fetch_requisite(courseCode)})
    print('All requisites.json fetched')
    print('Writing to file')
    f = open("requisites.json", "w")
    f.write(json.dumps(requisites, indent=4))


def log_req_progress(i, searchSpace):
    print(str(round((i/searchSpace)*100, 2)) + "% fetched")


def getURL(courseCode):
    return f"https://programsandcourses.anu.edu.au/2024/course/{courseCode}"


def fetch_requisite(courseCode):
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


start()