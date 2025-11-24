print("WELCOME TO UNIT CONVERTER")
print("Choose what you want to convert:")

print("1. Meter → Kilometer")
print("2. Kilometer → Meter")
print("3. Centimeter → Meter")
print("4. Gram → Kilogram")
print("5. Kilogram → Gram")
print("6. Celsius → Fahrenheit")
print("7. Fahrenheit → Celsius")

c = int(input("Enter your choice number: "))      #c=choice

v = float(input("Enter the value to convert: "))      #v=value


if c == 1:
      result = v/ 1000
      print(v, "meters =", result, "kilometers")

elif c == 2:
      result = v * 1000 
      print(v, "kilometers =", result, "meters") 

elif c == 3:
      result = v / 100 
      print(v, "centimeters =", result, "meters") 

elif c == 4: 
      result = v / 1000 
      print(v, "grams =", result, "kilograms") 

elif c == 5: 
      result = v * 1000 
      print(v, "kilograms =", result, "grams") 

elif c == 6: 
      result = (v * 9/5) + 32 
      print(v, "°C =", result, "°F") 

elif c == 7: 
      result = (v - 32) * 5/9 
      print(v, "°F =", result, "°C") 

else:
      print("Invalid option. Please choose a correct number.")






