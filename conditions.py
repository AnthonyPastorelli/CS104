Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp = int(input("Please enter the current temperature"))
if (temp > 90):
	print("Wear Shorts")
else if (temp > 70):
	print("Short sleeves are fine")
else if (temp > 50):
	print("Wear a jacket")
else if (temp > 32):
	print("Wear a heavy coat")
else:
	print("Stay Inside")
