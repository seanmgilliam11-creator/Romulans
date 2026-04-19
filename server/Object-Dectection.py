String color = mbot.getColorObjectFromCamera(false);

System.out.println("Detected color: " + color);

if (color.equalsIgnoreCase("GREEN")) {
    System.out.println("Movable object");
    mbot.moveForward();

} else if (color.equalsIgnoreCase("BLUE")) {
    System.out.println("Immovable object");
    mbot.turn();

} else if (color.equalsIgnoreCase("RED")) {
    System.out.println("Sample detected");
    mbot.stop();

} else {
    System.out.println("Unknown object");
}