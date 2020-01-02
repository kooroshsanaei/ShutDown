import time , os

second = input("pelase enter the time in seconds for shut downing the Computer:")
int(second)
counter = int(second)

print("For canceling the program press CTRl+Z")
print("\n")
i = 1
while (counter >= 0) :
    print("Seconds left to shut down : {0}".format(counter))
    counter = counter - 1
    time.sleep(i)

os.system("shutdown")





