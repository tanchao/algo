package com.tanchao.playground;

import lombok.Value;
import org.apache.commons.lang3.StringUtils;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FileSystem {
    public static final String PATH_DELIMITER = "/";
    public static final String ROOT_PATH = "/";
    private final File root;
    private final Map<String, File> filePaths;

    public FileSystem() {
        root = new File(ROOT_PATH, null, true);
        filePaths = new HashMap<>();
        filePaths.put(ROOT_PATH, root);
    }

    public File mkdir(String path) {
        if (isValidPath(path)) { // "/tan/chao/test"
            String dirPath = removeEndDelimiterIfExists(path);
            String parentPath = getParentPath(dirPath);
            if (filePaths.containsKey(parentPath)) {
                File dir = new File(dirPath, null, true);
                filePaths.put(dirPath, dir);
                return dir;
            } else {
                throw new IllegalArgumentException("Invalid parent path: " + parentPath);
            }
        } else {
            throw new IllegalArgumentException("Invalid path input: " + path);
        }
    }

    public File write(String path, String content) {
        if (isValidPath(path)) {
            String filePath = removeEndDelimiterIfExists(path); // todo: clarify
            String parentPath = getParentPath(filePath);
            if (filePaths.containsKey(parentPath)) {
                File file = new File(filePath, content, false);
                filePaths.put(filePath, file);
                return file;
            } else {
                throw new IllegalArgumentException("Invalid parent path: " + parentPath);
            }
        } else {
            throw new IllegalArgumentException("Invalid path input: " + path);
        }
    }

    public String read(String path) {
        String filePath = removeEndDelimiterIfExists(path); // todo: clarify
        if (filePaths.containsKey(filePath)) {
            File file = filePaths.get(filePath);
            if (file.isDir()) {
                throw new IllegalArgumentException("File is a directory, nothing to read.");
            }
            return file.getContent();
        } else {
            throw new IllegalArgumentException("File doesn't exist: " + path);
        }
    }

    public String getParentPath(String path) {
        String parentPath = StringUtils.substringBeforeLast(path, PATH_DELIMITER);
        if ("".equals(parentPath)) { // root directs
            return ROOT_PATH;
        } else {
            return parentPath;
        }
    }

    private String removeEndDelimiterIfExists(String path) {
        if (ROOT_PATH.equals(path)) {
            return path;
        }
        return StringUtils.removeEnd(path, PATH_DELIMITER);
    }

    private boolean isValidPath(String path) {
        // not blank
        if (StringUtils.isBlank(path)) {
            throw new IllegalArgumentException("path is blank");
        }
        // starts with root
        if (!StringUtils.startsWith(path, ROOT_PATH)) {
            throw new IllegalArgumentException("path should starts with root '/'");
        }
        // todo: parent path exists?
        return true;
    }
}


@Value
class File {
    String path;
    String content; // should be null for Dir; String for File.
    boolean isDir; // directory is type of file
}
