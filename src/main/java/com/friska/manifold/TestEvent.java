package com.friska.manifold;


import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class TestEvent extends ListenerAdapter {

    private static String testString = "[MATH4204](https://programsandcourses.anu.edu.au/2024/course/MATH4204) Algebraic Topology Honours\n" +
            "[MATH4204](https://programsandcourses.anu.edu.au/2024/course/MATH4204) Algebraic Topology Honours\n" +
            "[MATH4204](https://programsandcourses.anu.edu.au/2024/course/MATH4204) Algebraic Topology Honours\n" +
            "[MATH4204](https://programsandcourses.anu.edu.au/2024/course/MATH4204) Algebraic Topology Honours";

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        if(event.getMessage().getContentRaw().equals("test")){
            EmbedBuilder eb = new EmbedBuilder();
            eb.setTitle("Degree Plan");
            eb.addField("Semester 1", testString, true);
            eb.addField("Semester 2", testString, true);
            event.getChannel().sendMessageEmbeds(eb.build()).queue();
        }
    }
}
