package edu.desu.cis.robot.control;

import edu.desu.cis.robot.service.SensorSnapshot;

public class CrystalBot extends RobotController {

    public CrystalBot(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        mbot.avoidCrashing(15);

        boolean crystalRetrieved = false;

        while (true) {
            SensorSnapshot sensor = awaitNewData();

            if (!crystalRetrieved && sensor.distance() <= 15) {
                mbot.stopAllBehaviors();

                mbot.retrieveCrystal();

                crystalRetrieved = true;
            }
        }
    }

    public static void main(String[] args) {
        try (CrystalBot robot = new CrystalBot("Gartei")) {
            robot.run();
        }
    }
}