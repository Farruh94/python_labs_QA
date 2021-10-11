# Input temperature (measure with thermometer) in C and program convert to F
tempMIN = 32
tempMAX = 43

Temp_health_min = 35
Temp_health_max = 37

temp_c = float(input("Input_temperature in C:"))
temp_f = temp_c * 1.8 + 32
print(f"Temperature in F:{temp_f}")

extra_message = ""
if (temp_c > tempMAX) or (temp_c < tempMIN):
    extra_message = f"Temperature {temp_f} is abnormal. Check your thermometer!"
else:
    if (temp_c >= Temp_health_min) and (temp_c <= Temp_health_max):
        extra_message = f"Temperature {temp_f} is normal"
    elif temp_c < Temp_health_min:
        extra_message = f"Temperature {temp_f} is lower"
    elif temp_c > Temp_health_max:
        extra_message = f"Temperature {temp_f} is higher"

print(extra_message)