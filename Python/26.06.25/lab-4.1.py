
#Converter Celsius <=> Fahrenheit


print("Please Enter Celcius degree:")
Сelsius_input = int (input())
Fahrenheit_converted = Сelsius_input * (9 / 5) + 32
print(f"Celsius {Сelsius_input} degrees in Fahreiheit is {Fahrenheit_converted}")

print("Please Enter Fahreiheit degree:")
Fahrenheit_input = int (input())
Celsius_converted = (Fahrenheit_input -32) * (5 / 9)
print(f"Fahrenheit {Fahrenheit_input} degrees in Celsius is {Celsius_converted}")
