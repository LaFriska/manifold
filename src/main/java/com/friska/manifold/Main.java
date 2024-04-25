package com.friska.manifold;

import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.requests.GatewayIntent;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        JDABuilder builder = JDABuilder.createDefault(fetchToken());
        builder.enableIntents(GatewayIntent.MESSAGE_CONTENT);
        builder.addEventListeners(

        );
        builder.build();
    }

    private static String fetchToken(){
        try {
            Properties prop = new Properties();
            prop.load(new FileInputStream("config.properties"));
            return prop.getProperty("token");
        }catch (IOException ignored){
            throw new RuntimeException("CANNOT ACCESS TOKEN");
        }
    }
}