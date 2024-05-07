package com.friska.manifold;

import com.friska.manifold.discord.HandleCommand;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.requests.GatewayIntent;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        JDABuilder builder = JDABuilder.createDefault(fetchProperty("token"));
        builder.enableIntents(GatewayIntent.MESSAGE_CONTENT);
        builder.addEventListeners(
              new HandleCommand()
        );
        builder.build();
    }

    public static String fetchProperty(String key){
        try {
            Properties prop = new Properties();
            prop.load(new FileInputStream("config.properties"));
            return prop.getProperty(key);
        }catch (IOException ignored){
            throw new RuntimeException("Cannot fetch property.");
        }
    }
}