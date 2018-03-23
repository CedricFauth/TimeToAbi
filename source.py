import datetime

currentdate = datetime.date.today()
print("Datum: " + currentdate.strftime("%d.%m.%Y"))

f = open("klausuren.txt", "r")

data = f.readlines()
print("")
for i in range(0, 7, 2):
    print(data[i].rstrip() + ":")
    try:
        daysleft = datetime.date(2018, int(data[i+1][3:5]), int(data[i+1][0:2]))
        print("noch " + str((daysleft-currentdate).days) + " Tage.\n")
    except:
        print("Falsches Format.\n")
input()
