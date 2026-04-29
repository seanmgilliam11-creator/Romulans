def follow_line_behavior():
    if not arbiter.acquire("line", "FOLLOW_LINE", 10, blocking=False):
        return
    try:
        line = mbuild.quad_rgb_sensor.get_line_sta() # line 1
    finally:
        arbiter.release("line", "FOLLOW_LINE")

    if not arbiter.acquire("motors", "FOLLOW_LINE", 10, blocking=False):
        return
    try:
        # implement line 2 – 13
        kp = 0.4
        base_speed = 30
        error = 0

        if line == 0:
            error = 45
        elif line == 1:
            error = 0
        elif 1 < line < 4:
            error = -30
        elif line < 7:
            error = -35
        else:
            error = -45

        correction = error * kp
        em1_speed = base_speed + correction
        em1_speed = min(max(em1_speed, -50), 50)
        em2_speed = -base_speed + correction
        em2_speed = min(max(em2_speed, -50), 50)
        mbot2.drive_speed(em1_speed, em2_speed)

    finally:
        arbiter.release("motors", "FOLLOW_LINE")

@register_command("FOLLOW_LINE")
def handle_follow_line(payload):
    scheduler.start_behavior("FOLLOW_LINE", follow_line_behavior)
    return ok_response("Following Line")