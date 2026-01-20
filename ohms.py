# Ohm's Law Program

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (R): "))

current = voltage / resistance

print("Current =", current, "A")

if current < 0.5:
    print("Low current")
elif 0.5 <= current <= 2:
    print("Normal current")
else:
    print("High current")