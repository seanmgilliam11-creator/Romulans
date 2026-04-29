package edu.desu.cis.robot.control;

public class LineFollower extends RobotController {

    public LineFollower(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        mbot.followLine();
        try {
            Thread.sleep(60000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        mbot.stopBehavior("FOLLOW_LINE");
    }

    public static void main(String[] args) {
        try (LineFollower robot = new LineFollower("Greer")) {
            robot.run();
        }
    }
}