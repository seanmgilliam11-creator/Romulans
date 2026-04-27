@register_command("CHECK_IMMOVABLE_OBJECT")
def handle_check_immovable_object(payload):
    if arbiter.acquire("camera", "CHECK_IMMOVABLE_OBJECT", 50):
        try:
            block = detect_color(True)
            color = block["color"]

            if color == "BLUE":
                return ok_response("Immovable object detected", {
                    "color": color,
                    "is_immovable": True
                })
            else:
                return ok_response("Object is not immovable", {
                    "color": color,
                    "is_immovable": False
                })

        finally:
            arbiter.release("camera", "CHECK_IMMOVABLE_OBJECT")

    return error_response("RESOURCE_BUSY", "Camera is busy")