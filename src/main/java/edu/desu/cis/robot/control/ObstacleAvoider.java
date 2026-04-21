package edu.desu.cis.robot.control;

public class ObstacleAvoider extends RobotController {

    public ObstacleAvoider(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        // Start the background behavior — returns immediately
        mbot.steerAround(20, 40, 25);

        // Let it roam for 15 seconds, then stop
        try {
            Thread.sleep(15000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        mbot.stopBehavior("STEER_AROUND");
    }

    public static void main(String[] args) {
        try (ObstacleAvoider robot = new ObstacleAvoider("Greer")) {
            robot.run();
        }
    }
}