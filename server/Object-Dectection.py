String color = mbot.getColorObjectFromCamera(false);

if (color.equalsIgnoreCase("GREEN")) {
    System.out.println("Movable object");
} else if (color.equalsIgnoreCase("BLUE")) {
    System.out.println("Immovable object");
} else if (color.equalsIgnoreCase("RED")) {
    System.out.println("Sample object");
} else {
    System.out.println("Unknown object");
}