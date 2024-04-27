package com.friska.manifold;
/**
 * This class contains many useful constants and variables in this project.
 * Any sophisticated classes or event handlers should statically import this class
 * in order to use much of the data.
 * */
public class Props {

    /**
    * The prefix is the first character of any Discord command, used to signify that a command is being queried.
    * The prefix is fetched from config.properties, as the first character of the "prefix" property,
    * */
    public static final char PREFIX = Main.fetchProperty("prefix").charAt(0);

    /**
     * The DB subclass contains every information retrieved from config.properties related to db.
     * */
    public static class Db{
        public static final String SERVER = Main.fetchProperty("db_server");
        public static final String DATABASE = Main.fetchProperty("db_database");
        public static final String PORT = Main.fetchProperty("db_port");
        public static final String USERNAME = Main.fetchProperty("db_username");
        public static final String PASSWORD = Main.fetchProperty("db_password");
    }

}
