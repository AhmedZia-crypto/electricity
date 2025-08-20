

units = int(input("Enter the number of units you consumed: "))

if units<50:
    print("Amount = ", (units*2.60)+25)

elif units>50 and units<100:
    print("Amount =", (units*3.25)+35)

elif units>100 and units<200:
    print("Amount =", (units*5.26)+45)

elif units>200:
    print("Amount =", (units*8.45)+75)75
