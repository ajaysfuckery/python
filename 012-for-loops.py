import time

# For Loop -> iterates a limited amount of time

for i in range(10):
    print(i + 1)


for i in range(50, 100):
    print(i + 1)


for i in "XTC":
    print(i)


for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1.00)

print("Happy new year!")