@register_command("CHECK_MOVABLE_OBJECT")
def handle_check_movable_object(payload):
    if arbiter.acquire("camera", "CHECK_MOVABLE_OBJECT", 50):
        try:
            block = detect_color(True)
            color = block["color"]

            if color == "GREEN":
                return ok_response("Movable object detected", {
                    "color": color,
                    "is_movable": True
                })
            else:
                return ok_response("Object is not movable", {
                    "color": color,
                    "is_movable": False
                })

        finally:
            arbiter.release("camera", "CHECK_MOVABLE_OBJECT")

    return error_response("RESOURCE_BUSY", "Camera is busy")