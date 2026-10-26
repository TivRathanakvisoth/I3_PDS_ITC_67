def celsius_to_fahrenheit(c, round_to=1):
    fahrenheit = c * 9/5 + 32
    return fahrenheit
print(celsius_to_fahrenheit(33), "F")

##Covert fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit, round_to=1):
    c = (fahrenheit - 32) * 5/9
    return c
print(fahrenheit_to_celsius(20), "C")

print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))