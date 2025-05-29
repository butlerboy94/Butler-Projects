import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

public class Main extends JPanel implements ActionListener, KeyListener {

    // Screen dimensions
    private static final int WIDTH  = 800;
    private static final int HEIGHT = 600;

    // Player properties
    private int playerX = WIDTH / 2 - 25;
    private final int playerY      = HEIGHT - 60;
    private final int playerWidth  = 50;
    private final int playerHeight = 20;
    private final int playerSpeed  = 10;

    // Bullet properties
    private final int bulletWidth  = 5;
    private final int bulletHeight = 10;
    private final int bulletSpeed  = 15;
    private final List<Bullet> bullets = new ArrayList<>();

    // Enemy properties
    private final int enemyWidth     = 40;
    private final int enemyHeight    = 20;
    private final int enemySpeed     = 2;
    private final List<Enemy> enemies = new ArrayList<>();
    private final Random rand        = new Random();
    private int spawnTimer           = 0;
    private final int spawnInterval  = 60; // frames between spawns

    // Score
    private int score = 0;

    // Movement flags and game loop
    private boolean moveLeft  = false;
    private boolean moveRight = false;
    private final Timer timer;

    public Main() {
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(this);

        timer = new Timer(15, this);
        timer.start();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Player movement
        if (moveLeft  && playerX > 0)                       playerX -= playerSpeed;
        if (moveRight && playerX < WIDTH - playerWidth)     playerX += playerSpeed;

        // Update bullets
        Iterator<Bullet> bIter = bullets.iterator();
        while (bIter.hasNext()) {
            Bullet b = bIter.next();
            b.y -= bulletSpeed;
            if (b.y + bulletHeight < 0) {
                bIter.remove();
            }
        }

        // Spawn enemies
        spawnTimer++;
        if (spawnTimer >= spawnInterval) {
            spawnTimer = 0;
            int x = rand.nextInt(WIDTH - enemyWidth);
            enemies.add(new Enemy(x, 0));
        }

        // Update enemies
        Iterator<Enemy> eIter = enemies.iterator();
        while (eIter.hasNext()) {
            Enemy en = eIter.next();
            en.y += enemySpeed;
            if (en.y > HEIGHT) {
                eIter.remove();
            }
        }

        // Collision: bullets vs enemies
        bIter = bullets.iterator();
        while (bIter.hasNext()) {
            Bullet b = bIter.next();
            eIter = enemies.iterator();
            while (eIter.hasNext()) {
                Enemy en = eIter.next();
                if (new Rectangle(b.x, b.y, bulletWidth, bulletHeight)
                        .intersects(new Rectangle(en.x, en.y, enemyWidth, enemyHeight))) {
                    eIter.remove();
                    bIter.remove();
                    score += 10;
                    break;
                }
            }
        }

        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw player
        g.setColor(Color.ORANGE);
        g.fillRect(playerX, playerY, playerWidth, playerHeight);

        // Draw bullets
        g.setColor(Color.RED);
        for (Bullet b : bullets) {
            g.fillRect(b.x, b.y, bulletWidth, bulletHeight);
        }

        // Draw enemies
        g.setColor(Color.CYAN);
        for (Enemy en : enemies) {
            g.fillRect(en.x, en.y, enemyWidth, enemyHeight);
        }

        // Draw score
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.BOLD, 18));
        g.drawString("Score: " + score, 10, 20);
    }

    @Override
    public void keyPressed(KeyEvent e) {
        switch (e.getKeyCode()) {
            case KeyEvent.VK_LEFT:  moveLeft  = true; break;
            case KeyEvent.VK_RIGHT: moveRight = true; break;
            case KeyEvent.VK_SPACE:
                bullets.add(new Bullet(
                    playerX + playerWidth/2 - bulletWidth/2,
                    playerY
                ));
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        switch (e.getKeyCode()) {
            case KeyEvent.VK_LEFT:  moveLeft  = false; break;
            case KeyEvent.VK_RIGHT: moveRight = false; break;
        }
    }

    @Override public void keyTyped(KeyEvent e) { /* not used */ }

    // Inner classes
    private static class Bullet {
        int x, y;
        Bullet(int x, int y) { this.x = x; this.y = y; }
    }

    private static class Enemy {
        int x, y;
        Enemy(int x, int y) { this.x = x; this.y = y; }
    }

    // **Correctly defined main method**
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Java 2D Shooting Game");
            Main panel = new Main();
            frame.add(panel);
            frame.pack();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
