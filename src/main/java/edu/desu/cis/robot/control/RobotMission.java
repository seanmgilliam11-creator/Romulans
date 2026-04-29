package edu.desu.cis.robot.control;

import edu.desu.cis.robot.commands.CommandResult;
import java.util.Map;

public class RobotMission extends RobotController {
    private enum RobotState {
        CRUISE, ANALYZE_OBJECT, PUSH_OBJECT, STEER_AROUND, RETRIEVE_SAMPLE, DONE
    }

    public RobotMission(String robotName) {
        super(robotName);
    }

    @Override
    public void run() {
        RobotState currentState = RobotState.CRUISE;
        mbot.followLine();

        while (currentState != RobotState.DONE) {
            var snapshot = awaitNewData();
            double distance = snapshot.distance();

            switch (currentState) {
                case CRUISE:
                    if (distance > 0 && distance <= 20) {
                        mbot.stopBehavior("FOLLOW_LINE");
                        try {
                            Thread.sleep(1000);
                        } catch (Exception e) {}

                        mbot.forward(20, 0.6);

                        try { Thread.sleep(500); } catch (Exception e) {}

                        currentState = RobotState.ANALYZE_OBJECT;
                        break;
                    }

                case ANALYZE_OBJECT:
                    String type = mbot.classifyObject();

                    if ("movable".equals(type)) currentState = RobotState.PUSH_OBJECT;
                    else if ("immovable".equals(type)) currentState = RobotState.STEER_AROUND;
                    else if ("sample".equals(type)) currentState = RobotState.RETRIEVE_SAMPLE;
                    else currentState = RobotState.STEER_AROUND;
                    break;

                case RETRIEVE_SAMPLE:
                    mbot.retrieveSample();
                    currentState = RobotState.DONE;
                    break;

                case PUSH_OBJECT:
                    mbot.pushObject();
                    mbot.followLine();
                    currentState = RobotState.CRUISE;
                    break;

                case STEER_AROUND:
                    mbot.steerAround(25, 40, 20);
                    try { Thread.sleep(4000); } catch (Exception e) {}
                    mbot.stopBehavior("STEER_AROUND");
                    mbot.followLine();
                    currentState = RobotState.CRUISE;
                    break;

            }
        }
    }

    public static void main(String[] args) {
        try (RobotMission mission = new RobotMission("Greer")) {
            mission.run();
        }
    }
}