max_capacity = 1000
power_level = 100

print("--- SMART BIN SYSTEM INITIALIZED ---")

# This loop lets you test the bin multiple times
while True:
    print("\n" + "=" * 30)

    # 1. Power Status
    print(f"Power: {power_level}%")
    if power_level > 50:
        print("Power status: Normal")
    elif power_level >= 10:
        print("Power status: Below Normal")
    else:
        print("Power status: Critical - Kindly recharge your bin")

    # 2. Hand Distance
    distance = int(input("\nDistance from the bin (cm): "))
    if distance <= 50:
        print("Bin light ON")
        print("Bin OPEN")
    else:
        print("Bin light OFF")
        print("Bin CLOSED")

    # 3. Waste Capacity
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

    # 4. Interactive Simulation Control
    power_level -= 15

    repeat = input("\nDo you want to test again? (yes/no): ").lower()
    if repeat != "yes" and repeat != "y":
        print("Goodbye!")
        break
