sek = int(input("Input time in seconds "))
hours = sek//3600
minutes = (sek - hours*3600)//60
seconds = (sek - (hours * 3600 + minutes * 60))

print (f"Time hh:mm:ss: " + f"{hours}".zfill(2) + ":" + f"{minutes}".zfill(2) + ":" + f"{seconds}".zfill(2))

