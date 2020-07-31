rang = [7, 5, 3, 3, 2]
print(rang)
num = int(input("Enter number of rang. If you want to QUIT enter 000 "))
while num != 000:
    for el in range(len(rang)):
        if rang[el] == num:
            rang.insert(el + 1, num)
            break
        elif rang[0] < num:
            rang.insert(0, num)
        elif rang[-1] > num:
            rang.append(num)
        elif rang[el] > num and rang[el + 1] < num:
            #print(rang)
            rang.insert(el+1, num)
    print(f"Current Rank - {rang}")
    num = int(input("Enter number. For QUIT enter 000 "))
