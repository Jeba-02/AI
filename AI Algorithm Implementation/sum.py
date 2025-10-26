# Step 1: Take user input
n = int(input("Enter a number: "))

# Step 2: Initialize total
total = 0

# Step 3: Loop from 1 to n
for i in range(1, n + 1):
    total += i

# Step 4: Print the result
print("Sum from 1 to", n, "is:", total)