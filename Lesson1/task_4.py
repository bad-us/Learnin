n = int(input("Please enter a positive integer"))
maximum = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maximum:
        maximum = n % 10
    else:
        continue
print("Maximum number: " + f"{maximum}")

