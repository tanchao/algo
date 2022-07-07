package com.snake;

import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

/**
 * A Snake class that keeps track of the board state, with 3 items:
 * Score (public int)
 * Apple (public Point)
 * Snake (public List of Point)
 */
public class SnakeGame {
    private final int maxRow;
    private final int maxCol;
    private int score;
    private Point apple;
    private final List<Point> snake; // tail first and head last
    private int currentDirection;

    /**
     * Args:
     * rows (int): number of rows of the board
     * cols (int): number of columns of the board
     * initialSnake (List of Point): list of points representing snake's initial position ordered by tail first and head last
     * initialDirection (int): a value between 0-3 representing snake's initial direction
     */
    public SnakeGame(int rows, int cols, List<Point> initialSnake, int initialDirection) {
        this.maxRow = rows;
        this.maxCol = cols;
        this.score = 0;
        this.snake = initialSnake;
        this.currentDirection = initialDirection;
        this.apple = generateNewApple();
    }

    public List<Point> getSnake() {
        return this.snake;
    }

    public Point getApple() {
        return this.apple;
    }

    public int getScore() {
        return this.score;
    }

    /**
     * Args:
     * command (int): a value between 0-4 representing snake's new direction (0-Up, 1-Right, 2-Down, 3-left, 4-zoom)
     */
    public void input(int command) {
        if (command == 4) { // not changing
            return;
        }
        if (command != currentDirection && isNotReverseCommand(command)) {
            currentDirection = command;
        }
    }

    /**
     * Returns:
     * true if game continues
     * false if snake collides with self or one of the walls
     */
    public boolean tick() {
        Point oldHead = snake.get(snake.size() - 1);
        Point newHead = moveHead(oldHead);
        snake.add(newHead); // move forward to new head
        if (apple.equals(newHead)) { // ate apple
            this.score += 1;
            this.apple = generateNewApple();
        } else { // remove tail if no apple
            snake.remove(0);
        }
        return shouldGameContinue(newHead);
    }

    private Point generateNewApple() {
        int rRow = random(maxRow);
        int rCol = random(maxCol);
        Point nextApple = new Point(rRow, rCol);
        while (!isValidApple(nextApple)) {
            rRow = random(maxRow);
            rCol = random(maxCol);
            nextApple.row = rRow;
            nextApple.col = rCol;
        }
        // todo: minor - edge cases, full map?
        return nextApple;
    }

    private boolean isValidApple(Point nextApple) {
        for (Point point: snake) {
            if (nextApple.equals(point)) {
                return false;
            }
        }
        return true;
    }

    private boolean isNotReverseCommand(int command) {
        if ((command + currentDirection) % 2 == 0) {
            return false;
        }
        return true;
    }

    private Point moveHead(Point old) {
        if (currentDirection % 2 == 0) { // move up and down, update row
            return new Point(old.row + (currentDirection - 1), old.col);
        } else { // move right and left, update col
            return new Point(old.row, old.col + (2 - currentDirection));
        }
    }

    private static int random(int limit) {
        return ThreadLocalRandom.current().nextInt(0, limit);
    }

    private boolean shouldGameContinue(Point head) {
        if (head.row >= maxRow || head.row < 0 || head.col >= maxCol || head.col < 0) { // hit edge
            return false;
        }
        for (int i = 0; i < snake.size() - 1; i++) { // exclude head itself
            if (head.equals(snake.get(i))) { // hit body
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(random(1));
        System.out.println(random(1));
        System.out.println(random(1));
        System.out.println(random(1));
        System.out.println(random(2));
        System.out.println(random(2));
        System.out.println(random(2));
        System.out.println(random(2));
    }
}
