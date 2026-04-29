package edu.desu.cis.robot.control;

import edu.desu.cis.robot.service.SensorSnapshot;

public class CrystalBot extends RobotController {

    public CrystalBot(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        mbot.avoidCrashing(15);

        while (true) {
            SensorSnapshot sensor = awaitNewData();

            if (sensor.distance() <= 15) { // <-- changed here
                mbot.stopBehavior("AVOID_CRASHING");
                // Try to retrieve crystal
                mbot.retrieveCrystal();
                // Resume moving
                mbot.avoidCrashing(15);
            }
            // Prevent tight infinite loop crash
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {}
        }
    }

    public static void main(String[] args) {
        try (CrystalBot robot = new CrystalBot("Gartei")) {
            robot.run();
        }
    }
}