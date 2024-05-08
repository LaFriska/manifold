package com.friska.manifold.discord;

import com.friska.manifold.Props;
import com.friska.manifold.data.Plan;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import static com.friska.manifold.data.Course.parseCommand;
import static com.friska.manifold.Util.isMatch;

public class HandleCommand extends ListenerAdapter {

    @Override
    public void onMessageReceived(@NotNull MessageReceivedEvent e) {
        if(e.getAuthor().isBot()) return;
        if(!e.getMessage().getContentRaw().startsWith(String.valueOf(Props.PREFIX))) return;
        Command cmd = Command.parse(e.getMessage().getContentRaw());
        if(cmd == null) return;
        String head = cmd.getHead();
        if(head.equalsIgnoreCase("course") && cmd.getArg(0) != null) parseCommand(e, cmd);
        if(head.equalsIgnoreCase("plan")){
            Plan.parseCommand(e, cmd);
        }
    }
}
