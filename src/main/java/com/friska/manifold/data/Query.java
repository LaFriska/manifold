package com.friska.manifold.data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import static com.friska.manifold.Props.Db.*;

public class Query {

    public static final String LINK = "jdbc:postgresql://" + SERVER + ":" + PORT + "/" + DATABASE;

    public static Connection getConnection() throws SQLException {
        Connection conn = DriverManager.getConnection(Query.LINK, USERNAME, PASSWORD);
        conn.setAutoCommit(false);
        return conn;
    }

    public static void handleException(Exception e){
        e.printStackTrace();
        System.err.println(e.getClass().getName()+": "+e.getMessage());
        System.exit(0);
    }
}
