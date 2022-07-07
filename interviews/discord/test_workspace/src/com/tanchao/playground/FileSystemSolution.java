package com.tanchao.playground;

public class FileSystemSolution {
    public static void main(String[] args) {
        FileSystem test = new FileSystem();
        test.mkdir("/test_dir");
        test.write("/test_dir/abc", "/test_dir/abc/1234");
        test.write("/abc", "/abc/1234");
        System.out.println(test.read("/abc"));
        System.out.println(test.read("/test_dir/abc"));
        System.out.println(test.read("/xyz"));
        System.out.println(test.read("/"));
    }
}
