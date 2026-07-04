[SMART HOME PROGRAMME.py](https://github.com/user-attachments/files/29665327/SMART.HOME.PROGRAMME.py)[Uploading SM"""
==================================================
SMART HOME SYSTEM - COMBINED APPLICATION
==================================================
This program combines 6 independent smart-device simulations into a
single master program with a menu-driven interface:

    1. Smart Lighting Control System
    2. Smart Parking System
    3. Smart Bin System
    4. Smart Fridge System
    5. Smart Fan Controller
    6. Smart Rain Detector

Each subsystem was originally a standalone script. To combine them
safely (without variable name clashes, since several used the same
name, e.g. `power_level`), each subsystem has been wrapped in its own
function / class, keeping all of its original logic, structure, and
print statements unchanged. Selecting an option from the master menu
runs that subsystem exactly as it behaved on its own; exiting a
subsystem returns you to the master menu.
"""

import time
import random


# ==================================================
# 1. SMART LIGHTING CONTROL SYSTEM
# ==================================================
def run_smart_lighting():
    password = "1234"
    attempts = 3

    print("=== SMART LIGHTING CONTROL SYSTEM ===")

    while attempts > 0:
        user_password = input("Enter system password: ")

        if user_password == password:
            print("ACCESS GRANTED!")
            break
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts remaining: {attempts}")

    if attempts == 0:
        print("SYSTEM LOCKED!")
        return

    # --------------------------------------------------
    # SYSTEM INITIALIZATION
    # --------------------------------------------------
    power_level = 100

    print("\n=== SYSTEM INITIALIZED ===")

    # --------------------------------------------------
    # MAIN SYSTEM LOOP
    # --------------------------------------------------
    while True:

        print("\n" + "=" * 50)

        # BATTERY STATUS CHECK
        print(f"Battery Level: {power_level}%")

        if power_level > 50:
            print("Power Status: Normal")
        elif power_level >= 20:
            print("Power Status: Low")
        else:
            print("Power Status: Critical")

        # MOTION DETECTION
        motion = input("\nMotion detected? (yes/no): ").lower()

        if motion == "yes":
            print("Motion Detected")
            lights_on = True
        else:
            print("No Motion Detected")
            lights_on = False

        # AMBIENT LIGHT SENSOR
        ambient_light = int(input("Ambient Light Level (0-100): "))

        if ambient_light < 30:
            brightness = 100
            print("Dark Environment")
        elif ambient_light < 70:
            brightness = 60
            print("Moderately Lit Environment")
        else:
            brightness = 20
            print("Bright Environment")

        # TIME-BASED CONTROL (NIGHT MODE)
        hour = int(input("Current Hour (0-23): "))

        if 18 <= hour <= 23 or 0 <= hour <= 5:
            print("Night Mode Activated")
            brightness += 20

            if brightness > 100:
                brightness = 100

        # SECURITY ALERT
        if motion == "yes" and (hour >= 23 or hour <= 5):
            print("SECURITY ALERT: Unexpected Night Movement!")

        # ENERGY SAVING MODE
        if power_level < 30:
            brightness = brightness // 2
            print("Energy Saving Mode Activated")

        # VOICE COMMANDS
        command = input(
            "Voice Command (lights on/lights off/skip): "
        ).lower()

        if command == "lights on":
            lights_on = True
        elif command == "lights off":
            lights_on = False

        # LIGHT CONTROL
        if lights_on:
            print("\nLIGHT STATUS: ON")
            print(f"Brightness Level: {brightness}%")
            power_level -= 5
        else:
            print("\nLIGHT STATUS: OFF")
            power_level -= 1

        # PREVENT NEGATIVE BATTERY
        if power_level < 0:
            power_level = 0

        # EMERGENCY MODE
        if power_level <= 10:
            print("EMERGENCY MODE ACTIVATED")
            print("Battery Critically Low!")

        # CONTINUE OR EXIT
        choice = input("\nRun system again? (yes/no): ").lower()

        if choice != "yes":
            print("\n=== FINAL REPORT ===")
            print(f"Battery Remaining: {power_level}%")
            print("System Shutting Down...")
            break


# ==================================================
# 2. SMART PARKING SYSTEM
# ==================================================
class SmartParking:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = [False] * total_slots   # False = Available, True = Occupied

    def display_slots(self):
        print("\n===== PARKING STATUS =====")
        available = 0
        for i, occupied in enumerate(self.slots):
            if occupied:
                print(f"Slot P{i+1}: Occupied")
            else:
                print(f"Slot P{i+1}: Available")
                available += 1
        print(f"\nAvailable Slots: {available}/{self.total_slots}")

    def park_vehicle(self):
        for i in range(self.total_slots):
            if not self.slots[i]:
                self.slots[i] = True
                print(f"\nVehicle parked in Slot P{i+1}")
                return
        print("\nParking Full!")

    def leave_vehicle(self, slot):
        if slot < 1 or slot > self.total_slots:
            print("Invalid Slot Number")
            return
        if self.slots[slot - 1]:
            self.slots[slot - 1] = False
            print(f"\nSlot P{slot} is now available.")
        else:
            print("\nSlot already empty.")


def run_smart_parking():
    parking = SmartParking(5)
    while True:
        print("\n====== SMART PARKING SYSTEM ======")
        print("1. Display Parking Slots")
        print("2. Park Vehicle")
        print("3. Vehicle Leaves")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            parking.display_slots()
        elif choice == "2":
            parking.park_vehicle()
        elif choice == "3":
            slot = int(input("Enter slot number: "))
            parking.leave_vehicle(slot)
        elif choice == "4":
            print("System Closed.")
            break
        else:
            print("Invalid Choice")


# ==================================================
# 3. SMART BIN SYSTEM
# ==================================================
def run_smart_bin():
    max_capacity = 1000
    power_level = 100
    print("--- SMART BIN SYSTEM INITIALIZED ---")
    while True:
        print("\n" + "=" * 30)
        # Power Status
        print(f"Power: {power_level}%")
        if power_level > 50:
            print("Power status: Normal")
        elif power_level >= 10:
            print("Power status: Below Normal")
        else:
            print("Power status: Critical - Kindly recharge your bin")

        # Hand Distance
        distance = int(input("\nDistance from the bin (cm): "))
        if distance <= 50:
            print("Bin light ON")
            print("Bin OPEN")
        else:
            print("Bin light OFF")
            print("Bin CLOSED")

        # Waste Capacity
        current_waste = int(input("\nCurrent waste amount (grams): "))
        bin_percentage = (current_waste / max_capacity) * 100
        print(f"Capacity: {bin_percentage:.1f}%")
        if bin_percentage > 80:
            print("Bin IS FULL, kindly take out trash")
        elif bin_percentage > 50:
            print("Bin is near full")
        elif bin_percentage >= 10:
            print("Bin is half empty")
        else:
            print("Bin is empty")

        # Interactive Control System
        power_level -= 15
        repeat = input("\nDo you want to test again? (yes/no): ").lower()
        if repeat != "yes" and repeat != "y":
            print("Goodbye!")
            break


# ==================================================
# 4. SMART FRIDGE SYSTEM
# ==================================================
def run_smart_fridge():
    fridge_max_items = 50
    power_level = 100
    print("--- SMART FRIDGE SYSTEM INITIALIZED ---")
    while True:
        print("\n" + "---" * 10)
        print(f"Power left: {power_level}%")
        if power_level > 70:
            print("Status: Power is high (Saving energy)")
        elif power_level >= 20:
            print("Status: Power is okay (Running normally)")
        else:
            print("Status: Power is very low (Slowing down to save battery!)")

        temperature = float(input("\nEnter current fridge temperature (C): "))
        if temperature < 10:
            print("Alert: Temperature too cold! Food might freeze.")
        elif 1.0 <= temperature <= 4.0:
            print("Status: Perfect Temperature. Food is fresh.")
        else:
            print("Warning: Temperature too warm! Food spoilage danger.")

        items_inside = int(input("\nHow many grocery items are inside right now?: "))
        fill_rate = (items_inside / fridge_max_items) * 100
        print(f"Storage Space Used: {fill_rate:.1f}%")
        if fill_rate >= 100:
            print("Status: Overloaded! Door cannot close properly.")
        elif fill_rate > 75:
            print("Status: Well stocked. No need to shop.")
        elif fill_rate >= 25:
            print("Status: Getting low. Consider a grocery run soon.")
        else:
            print("Status: Fridge is practically empty! Restock immediately.")

        power_level -= 25  # Subtracts 25 from power level each loop
        user_loop = input("\nRefresh fridge sensors? (yes/no): ").lower()
        if user_loop != "yes" and user_loop != "y":
            print("Smart Fridge App Closed.")
            break


# ==================================================
# 5. SMART FAN CONTROLLER
# ==================================================
TEMP_ON = 35       # turn fan ON when temperature reaches this (35°C)
TEMP_OFF = 30      # turn fan OFF when temperature drops to this (30°C)


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


def run_smart_fan():
    fan_is_on = False
    print("--- SMART FAN CONTROLLER INITIALIZED ---")
    print("(Press Ctrl+C to stop and return to the main menu)")
    try:
        while True:
            temperature = read_temperature()
            fan_is_on = decide_fan_state(temperature, fan_is_on)
            set_fan(fan_is_on)
            print(f"Temp: {temperature:.1f}°C -> Fan: {'ON' if fan_is_on else 'OFF'}")
            time.sleep(12*60*60)
    except KeyboardInterrupt:
        print("\nSmart Fan Controller stopped. Returning to main menu...")


# ==================================================
# 6. SMART RAIN DETECTOR
# ==================================================
RAIN_SENSOR_THRESHOLD = 600
buzzer_pin_state = "LOW"


def read_rain_sensor():
    """
    Simulates reading the analog value from the rain sensor.
    Analog values typically range from 0 (very wet) to 1023 (completely dry).
    """
    return random.randint(200, 1023)


def set_buzzer(state):
    """
    Controls the state of the buzzer.
    """
    global buzzer_pin_state
    buzzer_pin_state = "HIGH" if state else "LOW"
    print(f"Buzzer Pin Status: {buzzer_pin_state}")


def run_smart_rain_detector():
    print("--- SMART RAIN DETECTOR SYSTEM INITIALIZED ---")
    print("(Press Ctrl+C to stop and return to the main menu)")
    try:
        while True:
            rain_value = read_rain_sensor()
            print(f"\nRain Sensor Value: {rain_value}")

            if rain_value < RAIN_SENSOR_THRESHOLD:
                print("Status: RAIN DETECTED!")
                set_buzzer(True)
            else:
                print("Status: Clear Weather")
                set_buzzer(False)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nSmart Rain Detector stopped. Returning to main menu...")


# ==================================================
# MASTER MENU
# ==================================================
def main():
    while True:
        print("\n" + "#" * 50)
        print("        SMART HOME SYSTEM - MASTER MENU")
        print("#" * 50)
        print("1. Smart Lighting Control System")
        print("2. Smart Parking System")
        print("3. Smart Bin System")
        print("4. Smart Fridge System")
        print("5. Smart Fan Controller")
        print("6. Smart Rain Detector")
        print("7. Exit")

        choice = input("\nSelect a subsystem to run: ")

        if choice == "1":
            run_smart_lighting()
        elif choice == "2":
            run_smart_parking()
        elif choice == "3":
            run_smart_bin()
        elif choice == "4":
            run_smart_fridge()
        elif choice == "5":
            run_smart_fan()
        elif choice == "6":
            run_smart_rain_detector()
        elif choice == "7":
            print("\nShutting down Smart Home System. Goodbye!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()ART HOME PROGRAMME.py…]()
