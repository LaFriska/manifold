package com.friska.manifold.data;

import com.friska.manifold.Props;
import com.friska.manifold.discord.Command;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

import static com.friska.manifold.data.Query.*;

/**
 * Encapsulates all relevant data into a single object.
 */
public record Course(String course_code,
                     String name,
                     Session session,
                     String career,
                     Integer units,
                     String requisites) {

//    public Course(@NotNull String course_code, @NotNull String name, @Nullable Session session, String career, Integer units, String requisites) {
//        this.course_code = course_code;
//        this.name = name;
//        this.session = session;
//        this.career = career;
//        this.units = units;
//        this.requisites = requisites;
//    }


    public static enum Session {
        OTHER("Other Semesters"),
        FIRST_SEMESTER("First Semester"),
        SECOND_SEMESTER("Second Semester"),
        BOTH("Both Semesters");

        public final String val;

        Session(String val) {
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
        } catch (Exception e) {
            handleException(e);
            return null;
        }
    }

    private static String getQuery(String course_code) {
        return "SELECT * FROM courses WHERE course_code = \'" + course_code + "\';";
    }

    @NotNull
    private static Session convertToSession(Integer session_number) {
        if (session_number == null) return Session.OTHER;
        switch (session_number) {
            case 1 -> {
                return Session.FIRST_SEMESTER;
            }
            case 2 -> {
                return Session.SECOND_SEMESTER;
            }
            default -> {
                return Session.BOTH;
            }
        }
    }

    /**
     * Formats a course code so that it is hyperlinked when sent over on Discord.
     */
    public static String formatURL(String course_code) {
        return "[" + course_code + "](https://programsandcourses.anu.edu.au/2024/course/" + course_code + ")";
    }

    public static void handleCourseSearch(MessageReceivedEvent e, Command cmd) {
        String code = cmd.getArg(0);
        Course course = Course.retrieve(code);
        if (course == null) {
            e.getChannel().sendMessage("Course \"" + code + "\" not found!").queue();
            return;
        }
        EmbedBuilder eb = Props.getEmbedTemplate(); //TODO check for nulls
        eb.setTitle(course.name);
        eb.setDescription(Course.formatURL(course.course_code));
        eb.addField("Session", course.session.val, true);
        eb.addField("Units", String.valueOf(course.units), true);
        eb.addField("Career", String.valueOf(course.career), true);
        eb.addField("Requisites", course.requisites, false);
        e.getChannel().sendMessageEmbeds(eb.build()).queue();

    }

}
