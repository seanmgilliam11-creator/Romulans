import edu.desu.cis.robot.control.RobotController;

public class ColorDetectionBot extends RobotController {

    public ColorDetectionBot(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        mbot.setFlashlight(true);

        String color = mbot.getColorObjectFromCamera(false);
        System.out.println("Detected color: " + color);

        if (color.equalsIgnoreCase("GREEN")) {
            System.out.println("Movable object detected");
        } else if (color.equalsIgnoreCase("BLUE")) {
            System.out.println("Immovable object detected");
        } else if (color.equalsIgnoreCase("RED")) {
            System.out.println("Sample detected");
        } else if (color.equalsIgnoreCase("YELLOW")) {
            System.out.println("Insertion point detected");
        } else {
            System.out.println("Unknown object");
        }

        mbot.setFlashlight(false);
    }

    public static void main(String[] args) {
        try (ColorDetectionBot robot = new ColorDetectionBot(“Snell”)) {
            robot.run();
        }
    }
}