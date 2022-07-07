package com.snake;

public class Point {
    public int row;
    public int col;

    public Point(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }

        if (!(o instanceof Point)) {
            return false;
        }

        Point p = (Point) o;
        return p.row == this.row && p.col == this.col;
    }

    public int hashCode() {
        return this.row * 31 + this.col;
    }

    public String toString() {
        return String.format("(row: %d, col: %d)", this.row, this.col);
    }
}
