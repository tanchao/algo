package upstart;

import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class SimplifyPath {
    public static String simplifyPath(String path) {
        // valid path
        if (path == null || path.isBlank() || !path.startsWith("/")) throw new RuntimeException("Invalid path");
        // split and handle
        List<String> dirs = new LinkedList<>();
        String[] paths = path.split("/");
        Set<String> skipPaths = Set.of("..", ".", "");
        for (String cur : paths) {
            cur = cur.trim();
            if ("..".equals(cur) && dirs.size() >= 1)
                dirs.remove(dirs.size() - 1);
            if (!skipPaths.contains(cur))
                dirs.add(cur);
        }
        // merge
        if (dirs.size() == 0) return "/";
        StringBuilder sb = new StringBuilder();
        for (String d : dirs)
            sb.append("/").append(d);
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("--- start");

        System.out.println(simplifyPath("/")); // /
        System.out.println(simplifyPath("/home/")); // /home
        System.out.println(simplifyPath("/../")); // /
        System.out.println(simplifyPath("//////home/")); // /home
        System.out.println(simplifyPath("/home///////")); // /home
        System.out.println(simplifyPath("/home/..//////")); // /
        System.out.println(simplifyPath("/home/../hello/world////")); // /hello/world
        System.out.println(simplifyPath("/home/../hello/world//    //")); // /hello/world

        System.out.println("--- end");
    }
}
