import json
import re


def start():
    sort()
    reformat()
    hyperlink_requisites()
    wrangle_programs()
    sanitize()


# Bubble sort algorithm to sort the courses json, and disgard unnecessary nesting of objects. Input false into this
# method if the courses.json does not have courses nested in Items.
def sort():
    print('Sorting courses and course requisites')
    f = open('courses.json')
    courses = json.load(f)
    f_req = open('requisites.json')
    reqs = json.load(f_req)
    if "Items" in courses:
        courses = courses["Items"]

    if len(courses) != len(reqs):
        print(
            f"Serious issue! There are {len(courses)} courses, but there are {len(reqs)} requisites, which is a mismatch. Consider re-running the scraper.")

    for i in range(1, len(courses)):
        for j in range(len(courses) - i):

            if courses[j]["CourseCode"] > courses[j + 1]["CourseCode"]:
                temp = courses[j + 1]
                courses[j + 1] = courses[j]
                courses[j] = temp

            if reqs[j]["courseCode"] > reqs[j + 1]["courseCode"]:
                temp = reqs[j + 1]
                reqs[j + 1] = reqs[j]
                reqs[j] = temp
    print('Writing to file')
    f = open('courses.json', 'w')
    f_req = open('requisites.json', 'w')
    f_req.write(json.dumps(reqs, indent=4))
    f.write(json.dumps(courses, indent=4))
    print('Sorting courses and course requisites.')
    print('Sort finished')


# Things like remove unnecessary line breaks, removing awkward spaces before periods etc.
def reformat():
    print('Removing unnecessary linebreaks')
    reqs = json.load(open('requisites.json'))
    courses = json.load(open('courses.json'))
    for i in range(len(reqs)):
        reqs[i]["req"] = reformat_reqs(reqs[i]["req"])
    print('Writing to file')
    f = open('requisites.json', 'w')
    f.write(json.dumps(reqs, indent=4))
    print('Linebreaks removed')


def reformat_reqs(requisite):
    words = re.split(r'\n', requisite)
    for i in range(len(words)):
        if is_course_code(words[i]):
            requisite = requisite.replace(f"\n{words[i]}\n", f" {words[i]} ")
    requisite = requisite.replace(" .", ".")
    requisite = requisite.replace(" ,", ",")
    requisite = requisite.replace(" ;", ";")
    return requisite


# Scans through entire requisites json and replace any words that are an ANU course with a hyperlinked version.
def hyperlink_requisites():
    print('Hyperlinking course codes in requisites')
    f = open('requisites.json')
    reqs = json.load(f)
    courses = json.load(open('courses.json'))
    for i in range(len(reqs)):
        reqs[i]["req"] = hyperlink_requisite(reqs[i]["req"], courses)
    print('Writing to file')
    f = open('requisites.json', 'w')
    f.write(json.dumps(reqs, indent=4))
    print('Hyperlinking process complete')


# Hyperlinks one requisite string
def hyperlink_requisite(requisite, courses):
    words = re.split(r'[\s.,;:]+', requisite)
    linked_words = []
    for i in range(len(words)):
        if has_course(words[i], courses) and words[i] not in linked_words:
            requisite = requisite.replace(words[i], get_hyperlinked_course(words[i]))
            linked_words.append(words[i])
    return requisite


# Performs a binary search on courses and returns if word is in courses.
def has_course(word, courses):
    if len(word) > 12:
        return False
    l = 0
    r = len(courses) - 1
    m = r // 2
    while l < r:
        mc = courses[m]['CourseCode']
        if word == mc:
            return True
        elif word < mc:
            r = m - 1
        elif word > mc:
            l = m + 1
        m = (l + r) // 2
    if courses[m]['CourseCode'] == word:
        return True
    else:
        return False


def get_hyperlinked_course(courseCode):
    return f"[{courseCode}](https://programsandcourses.anu.edu.au/2024/course/{courseCode})"


# Returns true if the input parameter has the structure to a course code. Returns false if otherwise. Note that this
# function does not necessarily gurantee that a course exists. For example, LMAO1234 will return true, but ANU does
# not offer a course with code LMAO1234.
def is_course_code(s):
    if len(s) > 9:
        return False
    if len(s) < 8:
        return False
    if not all(char.isupper() for char in s[0:4]):
        return False
    if not all(char.isdigit() for char in s[4:8]):
        return False
    return True


def wrangle_programs():
    programs = json.load(open("programs.json"))
    if "Items" in programs:
        programs = programs["Items"]
    for i in range(len(programs)):
        programs[i] = {
            "program_code": programs[i]["AcademicPlanCode"],
            "name": programs[i]["ProgramName"],
            "atar": programs[i]["Atar"],
            "career": programs[i]["AcademicCareer"],
            "duration": programs[i]["Duration"],
            "mod": programs[i]["ModeOfDelivery"]
        }
    f = open("programs.json", "w")
    f.write(json.dumps(programs, indent=4).replace("<p>", "").replace("</p>", ""))


# Unwrangles courses and requisites by copying from the backup.
def unwrangle():
    f = open('courses.json', 'w')
    f.write(json.dumps(json.load(open('backup/courses.json')), indent=4))
    f = open('requisites.json', 'w')
    f.write(json.dumps(json.load(open('backup/requisites.json')), indent=4))
    f = open('programs.json', 'w')
    f.write(json.dumps(json.load(open('backup/programs.json')), indent=4))


def sanitize():
    print("Sanitizing courses")
    sanitize_file("courses.json", 'Name')
    print("Sanitizing requisites")
    sanitize_file("requisites.json", 'req')
    print("Sanitizing programs")
    sanitize_file("programs.json", 'name')


def sanitize_file(file, attribute):
    data = json.load(open(file))
    for i in range(len(data)):
        data[i][attribute] = sanitize_quotations(data[i][attribute])
    open(file, 'w').write(json.dumps(data, indent=4))


def sanitize_quotations(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == "'" and (i == 0 or input_string[i - 1] != "'"):
            output_string += "'"
        output_string += input_string[i]
    return output_string


unwrangle()
start()
