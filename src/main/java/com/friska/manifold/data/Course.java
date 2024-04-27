package com.friska.manifold.data;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

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

   public static enum Session{
       FIRST_SEMESTER,
       SECOND_SEMESTER,
       OTHER
   }

}
