package com.friska.manifold;

public class Util {

    public static boolean isMatch(String keyword, String[] matchArray){
        if(matchArray == null) return false;
        for (String s : matchArray) if (s.equalsIgnoreCase(keyword)) return true;
        return false;
    }
}
