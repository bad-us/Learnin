m = int(input("Enter number of month "))
month = ['January', 'February', 'March', 'April', 'May', 'June', 'Jule', 'August', 'September', 'October', 'November',
         'December']
season = {1: 'Winter', 2: 'Spring', 3: "Summer", 4: 'Autumn'}
time_year = ['Winter', 'Spring', "Summer", 'Autumn']
if m < 0:
    m = int(print("Plese enter number of month (1-12) "))
else:
    print("This is month " + month[m - 1])
    if m == 1 or m == 2 or m == 12:
        time = time_year[0]
        time1 = season.get(1)
    elif 3 <= m <= 5:
        time = time_year[1]
        time1 = season.get(2)
    elif 6 <= m <= 8:
        time = time_year[2]
        time1 = season.get(3)
    else:
        time = time_year[3]
        time1 = season.get(4)

    print("The month of " + month[m - 1] + " is " + time)
    print(time1)
