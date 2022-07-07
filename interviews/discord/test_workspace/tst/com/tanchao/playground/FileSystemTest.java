package com.tanchao.playground;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class FileSystemTest {
    FileSystem testFileSystem;

    @BeforeEach
    void init() {
        testFileSystem = new FileSystem();
        testFileSystem.mkdir("/test_dir");
        testFileSystem.write("/test_dir/abc", "/test_dir/abc/1234");
        testFileSystem.write("/abc", "/abc/1234");
    }

    @Test
    public void testRead_withDifferentInputs() {
        Assertions.assertEquals("/abc/1234", testFileSystem.read("/abc"));
    }
}
