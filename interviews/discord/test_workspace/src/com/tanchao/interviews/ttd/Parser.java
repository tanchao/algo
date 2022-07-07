package com.tanchao.ttd;

import java.util.*;

import org.apache.commons.lang3.ArrayUtils;
import org.apache.commons.lang3.StringUtils;

public class Parser {
    public static final char COMMA = ',';
    public static final char FLAG = '\\'; // assumption

    public static List<String> parse(String line) {
        char[] chars = line.toCharArray();

        List<String> result = new ArrayList<>();
        int start = 0;
        boolean ignoreComma = false;
        for (int i = 0; i < chars.length; i++) {
            if (COMMA == chars[i]) {
                if (ignoreComma) {
                    ignoreComma = false;
                    continue;
                }
                // append
                result.add(extractWord(chars, start, i - 1)); // index before comma 
                start = i + 1; // index after comma
            }
            if (FLAG == chars[i]) {
                ignoreComma = true;
            }
            if (i == chars.length - 1) { // final result
                result.add(extractWord(chars, start, i));
            }
        }

        return result;
    }




    private static String extractWord(char[] chars, int start, int end) {
        String word = String.valueOf(chars, start, end - start + 1);
        // trim the flags if any
        if (word.indexOf(FLAG) > 0) { // exists
            word = StringUtils.substring(word, 0, word.indexOf(FLAG))
                    + StringUtils.substring(word, word.indexOf(FLAG) + 1, word.length());
        }
        return word;
    }

    public static void main(String[] args) {
        System.out.println("start");

        System.out.println(parse("test,hello,world")); // [test | hello | world]
        System.out.println(parse("test,he\\,llo,world")); // [test | he,llo | world]
        System.out.println(parse("test,he\\\\,llo,world")); // [test | he,llo | world]
        System.out.println(parse("\\test,he\\\\,llo,world")); // [test | he,llo | world]

        // ? 

        System.out.println("\\end,hello\\\\,world");
    }
}



///
int start = 0;
boolean isFlagged = false;
String preFlag;
for (int i = 0; i < chars.length; i++) {
    if (isFlagged) {
        if (COMMA == chars[i]) { // comma in content
            // continue
        } else {
            start = i;
        }

        isFlagged = false;
    } else {
        if (FLAG == chars[i]) {
            isFlagged = true;
            preFalg = extractWord(chars, start, i - 1);
        }
        if (COMMA == chars[i]) {
            if ("".equals(preFlag)) {
                result.add(extractWord(chars, start, i));
            } else {
                result.add(preFlag + extractWord(chars, start, i));
                preFlag = "";
            }
            
        }
    }
}