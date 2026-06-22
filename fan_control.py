import time
import random  # only used to FAKE sensor readings for this demo

# ---- Variables: the settings and state our program tracks ----
TEMP_ON = 35       # turn fan ON when temperature reaches this (°C)
TEMP_OFF = 30      # turn fan OFF when temperature drops to this (°C)
fan_is_on = False  # current state of the fan


def read_temperature():
    """
    Get the current temperature.
    Right now this fakes a reading. Later, replace the body of this
    function with real sensor code (e.g. reading a thermistor's
    voltage and converting it to °C).
    """
    return random.uniform(20, 45)


def decide_fan_state(temp, fan_is_on):
    """
    Decide whether the fan should be on or off.
    Uses hysteresis: two thresholds instead of one, so the fan
    doesn't flicker on/off when the temperature sits near the edge.
    """
    if temp >= TEMP_ON:
        fan_is_on = True
    elif temp <= TEMP_OFF:
        fan_is_on = False
    # if temp is between TEMP_OFF and TEMP_ON: do nothing,
    # leave the fan in whatever state it already was
    return fan_is_on


def set_fan(state):
    """
    Apply the fan state.
    Right now this just prints. Later, replace this with real
    hardware control (e.g. turning a GPIO pin high/low).
    """
    print("Fan ON" if state else "Fan OFF")


# ---- Main loop: check temperature repeatedly, forever ----
while True:
    temperature = read_temperature()
    fan_is_on = decide_fan_state(temperature, fan_is_on)
    set_fan(fan_is_on)
    print(f"Temp: {temperature:.1f}°C -> Fan: {'ON' if fan_is_on else 'OFF'}")
    time.sleep(1)
