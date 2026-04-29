public class RobotExplorer {

    // Simulated robot position
    static int x = 0;
    static int y = 0;

    public static void main(String[] args) {

        System.out.println("Mission started...");

        // Simulate robot moving forward 10 steps
        for (int step = 0; step < 10; step++) {

            if (detectObstacle()) {
                System.out.println("Obstacle detected! Avoiding...");
                avoidObstacle();
            } else {
                moveForward();
            }
        }

        System.out.println("Navigation complete.");
    }

    // Simulates obstacle detection (random for now)
    public static boolean detectObstacle() {
        return Math.random() < 0.3; // 30% chance of obstacle
    }

    // Simulates avoiding obstacle
    public static void avoidObstacle() {
        System.out.println("Turning right to avoid obstacle...");
        x++; // simple move to the side
    }

    // Simulates forward movement
    public static void moveForward() {
        y++;
        System.out.println("Moving forward to position (" + x + ", " + y + ")");
    }
}