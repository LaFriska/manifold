package com.friska.manifold.data;

import java.sql.Connection;
import java.sql.DriverManager;

import static com.friska.manifold.Props.Db.*;

public class Query {

    public static void main(String[] args) {
        Connection c = null;
        try {
            Class.forName("org.postgresql.Driver");
            c = DriverManager.getConnection("jdbc:postgresql://" + SERVER + ":" + PORT + "/" + DATABASE, USERNAME, PASSWORD);
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println(e.getClass().getName()+": "+e.getMessage());
            System.exit(0);
        }
        System.out.println("Opened database successfully");
    }

}
