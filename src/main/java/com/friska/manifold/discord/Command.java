package com.friska.manifold.discord;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.util.Arrays;

import static com.friska.manifold.Vars.*;

public class Command{

    private final String head;
    private final String[] args;
    /**
     * A command is a data structure with a command head and a list of arguments.
     * */
    public Command(@NotNull String head, @Nullable String[] args){
        this.head = head;
        this.args = args;
    }

    @NotNull
    public String getHead(){
        return head;
    }

    @Nullable
    public String getArg(int i){
        if(i > args.length - 1) return null;
        return args[i];
    }

    /**
     * Takes a string input and parses it into a command. Returns null if string is invalid command.
     * */
    @Nullable
    public static Command parse(String parse){
        if(!parse.startsWith(String.valueOf(PREFIX))) return null;
        String[] terms = parse.split(" ");
        if(terms.length == 0) return null;
        String head = terms[0].substring(1);
        String[] args = terms.length > 1 ? Arrays.copyOfRange(terms, 1, terms.length) : null;
        return new Command(head, args);
    }

}
