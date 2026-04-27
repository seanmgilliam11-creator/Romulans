 @register_command("CLASSIFY_OBJECT")
def handle_classify_object(payload):
    if arbiter.acquire("camera", "CLASSIFY_OBJECT", 50):
        try:
            block = detect_color(True)
            color = block["color"]

            if color == "GREEN":
                object_type = "movable"
            elif color == "BLUE":
                object_type = "immovable"
            elif color == "RED":
                object_type = "sample"
            elif color == "YELLOW":
                object_type = "insertion point"
            else:
                object_type = "unknown"

            return ok_response("Object classified", {
                "color": color,
                "object_type": object_type
            })

        finally:
            arbiter.release("camera", "CLASSIFY_OBJECT")

    return error_response("RESOURCE_BUSY", "Camera is busy")








