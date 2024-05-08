package com.friska.manifold.discord;

import com.friska.manifold.Props;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import static com.friska.manifold.data.Course.handleCourseSearch;

public class HandleCommand extends ListenerAdapter {

    @Override
    public void onMessageReceived(@NotNull MessageReceivedEvent e) {
        if(e.getAuthor().isBot()) return;
        if(!e.getMessage().getContentRaw().startsWith(String.valueOf(Props.PREFIX))) return;
        Command cmd = Command.parse(e.getMessage().getContentRaw());
        if(cmd == null) return;
        if(cmd.getHead().equalsIgnoreCase("course") && cmd.getArg(0) != null){
            handleCourseSearch(e, cmd);
        }
    }
}
