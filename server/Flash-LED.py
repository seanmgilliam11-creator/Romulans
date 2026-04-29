@register_command("FLASH_LED")
def handle_flash_led(payload):
    params = payload.get("parameters", {})
    times  = int(params.get("times", 3))
    r      = int(params.get("red",   0))
    g      = int(params.get("green", 0))
    b      = int(params.get("blue",  255))
    delay  = float(params.get("delay", 0.3))

    if times < 1 or times > 20:
        return error_response("INVALID_PARAM",
                              "times must be between 1 and 20")

    if arbiter.acquire("led", "FLASH_LED", 50):
        try:
            for _ in range(times):
                cyberpi.led.on(r, g, b, id="all")
                time.sleep(delay)
                cyberpi.led.off(id="all")
                time.sleep(delay)
            return ok_response("Flash complete")
        finally:
            arbiter.release("led", "FLASH_LED")