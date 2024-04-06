--THIS SCRIPT RE-INITIALIZES DATABASE FOR CHALKY, AND ALL EXISTING DATABASES WITH OVERLAPPING TABLE NAMES
--WILL BE DROPPED. RUN THIS SCRIPT ONLY WITH CAUTION.

DROP TABLE Plans CASCADE;
DROP TABLE ANU_Courses CASCADE;
DROP TABLE Entries CASCADE;

--Degree is nullable, and title will be defaulted to as "untitled" if left as null.
CREATE TABLE Plans (
    pid INT PRIMARY KEY,
    uid BIGINT NOT NULL,
    plan_num SMALLINT NOT NULL,
    degree VARCHAR(100),
    title VARCHAR(100)
);

--The courses table stores course code and its title, which if exceeds 100 characters, should have the remaining few characters replaced by
--periods. The semester is stored as a small int, in the form of number code: 1 for first semester, 2 for second semester, 3 for both, and NULL for neither.
--Courses exclusive only to autumn/summer etc semester will just be NULL.
CREATE TABLE ANU_Courses (
    course_code CHAR(8) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    semester SMALLINT
)

CREATE TABLE Entries (
    pid INT,
    year SMALLINT,
    semester SMALLINT,
    course_code CHAR(8),
    slot SMALLINT,
    FOREIGN KEY(pid) REFERENCES Plans(pid),
    FOREIGN KEY(course_code) REFERENCES ANU_Courses(course_code)
)