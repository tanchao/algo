package com.tanchao.playground;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;

/**
encode 和decodeing
比如  "abc,  aaa, bca, aaa,  abc,  bca, aaa"
encoded as " abc, aaa, bca:0,1,2,1,0,2,1"
**/

public class Playground {
    public static String encode(List<String> words) {
        List<String> dict = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        List<String> codes = new ArrayList<>();
        for (String word : words) {
            if (map.containsKey(word)) { // exists
                codes.add(map.get(word).toString());
            } else {
                dict.add(word);
                map.put(word, dict.size() - 1);
                codes.add(map.get(word).toString());
            }
        }
        String wordsCode = String.join(",", dict);
        String ordersCode = String.join(",", codes);
        return wordsCode + ":" + ordersCode;
    }
    
    public static List<String> decode(String code) {
        // todo: validation
        String wordsCode = code.split(":")[0];
        String ordersCode = code.split(":")[1];
        String[] dict = wordsCode.split(",");
        String[] orders = ordersCode.split(",");
        List<String> output = new ArrayList<>();
        for (String order : orders) {
            output.add(dict[Integer.valueOf(order)]);
        }
        return output;
    }
    
    public static void main(String[] args) {
        System.out.println("Start");
        List<String> input = Arrays.asList("abc", "aaa", "bca", "aaa", "abc", "bca", "aaa");
        String expected = "abc,aaa,bca:0,1,2,1,0,2,1";
        
        
        System.out.println(encode(input));
        System.out.println(expected.equals(encode(input)));
        
        System.out.println(decode(expected));
        System.out.println(input.equals(decode(expected)));
        
        System.out.println("End");
        PriorityQueue q = new PriorityQueue();
    }
}