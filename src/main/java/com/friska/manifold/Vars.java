package com.friska.manifold;
/**
 * This class contains many useful constants and variables in this project.
 * Any sophisticated classes or event handlers should statically import this class
 * in order to use much of the data.
 * */
public class Vars {

    /**
    * The prefix is the first character of any Discord command, used to signify that a command is being queried.
    * The prefix is fetched from config.properties, as the first character of the "prefix" property,
    * */
    public static final char PREFIX;

    static{
        PREFIX = Main.fetchProperty("prefix").charAt(0);
    }

}
