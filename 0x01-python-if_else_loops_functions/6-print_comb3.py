#!/usr/bin/python3
for i in range(0, 90):
    if i % 10 > i / 10 and i != 90:
        
        print("{:02d},".format(i), end=" ")
print()
