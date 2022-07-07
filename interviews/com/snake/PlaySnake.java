package com.snake;

import  java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class PlaySnake extends JPanel {

    /**
     *
     */
    private static final long serialVersionUID = 439503649348465838L;

    private static final int GRID_WIDTH = 10;
    private static final int GRID_HEIGHT = 10;
    private static final int WIDTH = 40;
    private static final int HEIGHT = 30;

    SnakeGame game;
    JLabel text;
    Thread gameThread;
    Object paintLock = new Object();
    boolean running = true;

    public PlaySnake() {
        List<Point> snake = new ArrayList<Point>();
        for (int i = 0; i < 1; i++) {
            snake.add(new Point(0, i));
        }
        game = new SnakeGame(HEIGHT, WIDTH, snake, 1); // todo: initial
        setFocusable(true);
        requestFocusInWindow();
        addKeyListener(new KeyListener() {

            @Override
            public void keyPressed(KeyEvent arg0) {
                switch (arg0.getKeyCode()) {
                case KeyEvent.VK_LEFT:
                    game.input(3);
                    break;
                case KeyEvent.VK_RIGHT:
                    game.input(1);
                    break;
                case KeyEvent.VK_UP:
                    game.input(0);
                    break;
                case KeyEvent.VK_DOWN:
                    game.input(2);
                    break;
                case KeyEvent.VK_SPACE:
                    game.input(4);
                    break;
                }

            }

            @Override
            public void keyReleased(KeyEvent arg0) {}

            @Override
            public void keyTyped(KeyEvent arg0) {}

        });
    }

    public void start() {
        gameThread = new Thread() {
            @Override
            public void run() {
                while (running) {
                    synchronized (paintLock) {
                        running = game.tick();
                    }
                    PlaySnake.this.repaint();
                    try {
                        Thread.sleep(75);
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            };
        };
        gameThread.start();
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        if (!running) {
            g.drawString("GAME OVER: " + game.getScore(), 10, 20);
        } else {
            g.drawString("Score: " + game.getScore(), 10, 20);
        }
        List<Point> snake;
        synchronized (paintLock) {
            snake = new ArrayList<Point>(game.getSnake());
        }
        g.drawRect(5, 25, 10 + WIDTH * GRID_WIDTH, 10 + HEIGHT * GRID_HEIGHT);
        for (Point p : snake) {
            g.drawRect(10 + p.col * GRID_WIDTH, 30 + p.row * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT);
        }

        Point apple = game.getApple();
        g.fillOval(10 + apple.col * GRID_WIDTH + 1, 30 + apple.row * GRID_HEIGHT + 1, GRID_WIDTH - 2,
                GRID_HEIGHT - 2);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Snake");
        PlaySnake game = new PlaySnake();
        frame.getContentPane().add(game);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(new Rectangle(20 + WIDTH * GRID_WIDTH, 64 + HEIGHT * GRID_HEIGHT));
        frame.setVisible(true);
        game.start();
    }
}
