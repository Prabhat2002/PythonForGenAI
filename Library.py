import math
from datetime import datetime
from datetime import time
import random

print(math.sqrt(16))      # Square root
print(math.pow(2, 3))     # Power
print(math.pi)            # Value of pi

print(math.factorial(5))  # Factorial

print(math.log10(3))


now = datetime.now()
timenow = now.time()
print(now)
print(now.strftime("%d-%m-%Y %H:%M:%S"))

print(time.max)
print(time.min)
print(timenow)
print(time(hour=14, minute=30, second=23))

print(random.randint(1, 10))
print(random.choice(["SAP", "Python", "AI"]))
