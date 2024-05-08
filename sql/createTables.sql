--THIS SCRIPT RE-INITIALIZES DATABASE FOR CHALKY, AND ALL EXISTING DATABASES WITH OVERLAPPING TABLE NAMES
--WILL BE DROPPED. RUN THIS SCRIPT ONLY WITH CAUTION.

--Note that if tables plans, courses, entries and programs do not exist, there are 4 expected failed error messages.

DROP TABLE plans CASCADE;
DROP TABLE courses CASCADE;
DROP TABLE entries CASCADE;
DROP TABLE programs CASCADE;

--Degree is nullable, and title will be defaulted to as "untitled" if left as null.
CREATE TABLE plans (
    pid INT PRIMARY KEY,
    uid BIGINT NOT NULL,
    plan_num SMALLINT NOT NULL,
    degree VARCHAR(100),
    title VARCHAR(100),
    years SMALLINT
);

--The courses table stores information about each ANU course. If the name exceeds 100 chars, it should have the remaining few characters cut off.
--The session is stored as a small int, in the form of number code: 1 for first semester, 2 for second semester, 3 for both, and NULL for neither.
--Courses exclusive only to autumn/summer etc semester will just be NULL. Note that mod stands for mode of delivery.
CREATE TABLE courses (
    course_code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    session SMALLINT CHECK(session <= 3),
    career VARCHAR(20),
    units SMALLINT,
    mod VARCHAR(100),
    requisite VARCHAR(2000)
);

CREATE TABLE programs(
    program_code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    atar FLOAT CHECK(atar >= 0 AND atar <= 100),
    career VARCHAR(20),
    duration SMALLINT CHECK(duration > 0 AND duration < 10),
    mod VARCHAR(100)
);

CREATE TABLE entries (
    pid INT,
    year SMALLINT,
    semester SMALLINT,
    course_code CHAR(8),
    slot SMALLINT,
    FOREIGN KEY(pid) REFERENCES plans(pid),
    FOREIGN KEY(course_code) REFERENCES courses(course_code)
);