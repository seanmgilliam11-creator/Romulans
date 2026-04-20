@register_command("PUSH_OBJECT")
def handle_push_object(payload):
    if (arbiter.acquire("motors", "PUSH_OBJECT", 100) and
            arbiter.acquire("ultrasonic", "PUSH_OBJECT", 100) and
            arbiter.acquire("imu", "PUSH_OBJECT", 100)):
        try:
            dist = mbuild.ultrasonic2.get()
            if dist <= 0 or dist > 20:
                return ok_response("No object close enough to push")

            turn(180) #turns around
            mbot2.straight(-(dist * 1.3)) #drives backwards into object
            move_and_turn(speed=-40, diff=20, is_left=True) #move/turn object out of the way for 4 secnods
            time.sleep(4)
            mbot2.straight(0)
            move_and_turn(speed=40, diff=20, is_left=True) #drive back
            time.sleep(3.5)
            mbot2.drive_speed(0, 0)
            mbot2.straight(dist * 1.3)
            #mbot2.straight(-15)
            turn(180)  #turns back to original position

            return ok_response("Object cleared")
        finally:
            arbiter.release("motors", "PUSH_OBJECT")
            arbiter.release("ultrasonic", "PUSH_OBJECT")
            arbiter.release("imu", "PUSH_OBJECT")

    return error_response("RESOURCE_BUSY", "Hardware unavailable")