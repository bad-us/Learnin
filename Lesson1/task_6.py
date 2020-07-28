kil = float(input("Enter the distance in kilometers"))
kil2 = float(input("Enter the distance in kilometers on day"))
n = 1
print(f"You distance in {n} day = " + f"{kil}")
while kil2 >= kil:
    kil = round(kil + (kil * 0.1),2)
    n += 1
    print(f"You distance in {n} day = " + f"{kil}")

print(f"You result in {n} day ")
