package com.friska.manifold.data;

import com.friska.manifold.discord.Command;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

import static com.friska.manifold.Util.isMatch;

public class Plan {

    public static void parseCommand(MessageReceivedEvent e, Command cmd) {
        if(isMatch(cmd.getArg(0), new String[]{"create", "new", "c"})){
            try {
                int years = cmd.getArg(1) == null ? 3 : Integer.parseInt(cmd.getArg(1));
                String name = cmd.concatenateArgsFrom(2);
                if(name == null) name = "Untitled";
                e.getChannel().sendMessage("Creating new " + years + " year degree plan called " + "\"" + name + "\".").queue();
            }catch(NumberFormatException ignored){
                e.getChannel().sendMessage("**Error**: The `<years>` parameter must be an integer! Example command: `!plan create 3 My Awesome Degree Plan`").queue();
            }
        }
    }

}
