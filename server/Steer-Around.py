def steer_around_behavior(threshold, speed, diff):
    """
    Called repeatedly by the scheduler.
    Reads the ultrasonic sensor and either drives straight or arcs left.
    """
    # Read the distance — skip this cycle if the sensor is busy
    if not arbiter.acquire("ultrasonic", "STEER_AROUND", 200, blocking=False):
        return

    try:
        distance = mbuild.ultrasonic2.get()
    finally:
        arbiter.release("ultrasonic", "STEER_AROUND")

    # Acquire the motors — skip this cycle if something higher-priority holds them
    if not arbiter.acquire("motors", "STEER_AROUND", 200, blocking=False):
        return

    try:
        if distance > threshold:
            # Path is clear — drive straight
            time.sleep(0.1)
            mbot2.drive_speed(speed, -speed)
        else:
            # Obstacle detected — arc left
            move_and_turn(speed=speed, diff=diff, is_left=True)
    finally:
        arbiter.release("motors", "STEER_AROUND")


@register_command("STEER_AROUND")
def handle_steer_around(payload):
    params    = payload.get("parameters", {})
    threshold = float(params.get("threshold", 25))
    speed     = float(params.get("speed",     40))
    diff      = float(params.get("diff",      20))

    if speed < 0 or speed > 100:
        return error_response("INVALID_PARAM",
                              "speed must be between 0 and 100")
    if diff < 0 or diff >= speed:
        return error_response("INVALID_PARAM",
                              "diff must be >= 0 and less than speed")

    scheduler.start_behavior("STEER_AROUND", steer_around_behavior,
                             threshold, speed, diff)
    return ok_response("STEER_AROUND started")