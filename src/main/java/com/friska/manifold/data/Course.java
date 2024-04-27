package com.friska.manifold.data;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import static com.friska.manifold.Props.Db.*;
import static com.friska.manifold.data.Query.*;

/**
 * Encapsulates all relevant data into a single object.
 */
public class Course {

    public final String course_code;
    public final String name;
    public final Session session;
    public final String career;
    public final Integer units;
    public final String requisites;

    public Course(@NotNull String course_code, @NotNull String name, @Nullable Session session, String career, Integer units, String requisites) {
        this.course_code = course_code;
        this.name = name;
        this.session = session;
        this.career = career;
        this.units = units;
        this.requisites = requisites;
    }


    public static enum Session {
        FIRST_SEMESTER("First Semester"),
        SECOND_SEMESTER("Second Semester"), //TODO fix enum strings
        OTHER("Other Semesters");

        public String val;

        Session(String val){
            this.val = val;
        }
    }

    public static Course retrieve(String course_code) {
        course_code = course_code.toUpperCase();
        Connection c;
        Statement s;
        try {
            Class.forName("org.postgresql.Driver");
            c = Query.getConnection();
            s = c.createStatement();

            ResultSet r = s.executeQuery(getQuery(course_code)); //TODO potential SQL injection vulnerability
            Course course;
            if (!r.next()) course = null;
            else course = new Course(
                    course_code,
                    r.getString("name"),
                    convertToSession(r.getInt("session")),
                    r.getString("career"),
                    r.getInt("units"),
                    r.getString("requisite"));
            r.close();
            s.close();
            c.close();
            return course;
        }catch (Exception e) {
            handleException(e);
            return null;
        }
    }

    private static String getQuery(String course_code) {
        return "SELECT * FROM courses WHERE course_code = \'" + course_code + "\';";
    }

    private static Session convertToSession(Integer session_number) {
        if (session_number == null) return null;
        switch (session_number) {
            case 1 -> {
                return Session.FIRST_SEMESTER;
            }
            case 2 -> {
                return Session.SECOND_SEMESTER;
            }
            default -> {
                return Session.OTHER;
            }
        }
    }

    public static String formatURL(String course_code){
        return "[" + course_code + "](https://programsandcourses.anu.edu.au/2024/course/" + course_code + ")";
    }

}
