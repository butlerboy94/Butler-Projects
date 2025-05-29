"""
A print the numbers 1 thru 5 with a while loop. 
B print the numbers 1 thru 5 with a for range loop.
C print the numbers 6 thru 20 by 2s with a for range loop (6,8,10,12,14,16,18,20)
D print the numbers 30 to 80 by 10s while loop.
E print the numbers 100 to 90 by -1 with a for range loop (100,99,98,97,96,95,94,93,92,91)
"""

# Seperated parts of code by "part A-E"


# A print the number 1 thru 5 with a while loop.
# use k for variable

print("part A")

k = 1
while k <= 5:
    print(k)
    k +=1

print("part B")

# B print the number 1 thru 5 with  for range loop
# use k for variable

for k in range(1,6):
    print(k)

print("part C")

# C print the numbers 6 thru 20 by 2s with a for range loop (6,8,10,12,14,16,18,20)
# use k for variable

for k in range(6,21,2):
    print(k)

print("part D")

# D print the numbers 30 to 80 by 10s with a while loop
# use k for variable

k = 30
while k <= 80:
    print(k)
    k += 10

print("part E")

# E print the numbers 100 to 90 by -1 with a for range loop (100, 99, 98, 97, 96, 95, 94, 93, 92, 91)
# use k for variable

for k in range(100, 90, -1):
    print(k)