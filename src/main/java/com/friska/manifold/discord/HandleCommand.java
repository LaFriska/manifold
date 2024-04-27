package com.friska.manifold.discord;

import com.friska.manifold.Props;
import com.friska.manifold.data.Course;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

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

    private static void handleCourseSearch(MessageReceivedEvent e, Command cmd){
        String code = cmd.getArg(0);
        Course course = Course.retrieve(code);
        if(course == null) {
            e.getChannel().sendMessage("Course \"" + code + "\" not found!").queue();
            return;
        }
        EmbedBuilder eb = Props.getEmbedTemplate(); //TODO check for nulls
        eb.setTitle(course.name);
        eb.setDescription(Course.formatURL(course.course_code));
        eb.addField("Session", course.session.val, true);
        eb.addField("Units", String.valueOf(course.units), true);
        eb.addField("Career", String.valueOf(course.career), true);
        eb.addField("Requisites", course.requisites, false);
        e.getChannel().sendMessageEmbeds(eb.build()).queue();

    }
}
