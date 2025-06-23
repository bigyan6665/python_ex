name = input("Enter name = ")
time = int(input("Enter time = "))
if(time>=5 and time<=11):
    print("Good morning, {name}")
elif(time>=12 and time<=17):
    print("Good afternoon, {name}")
elif(time>=18 and time<=20):
    print("Good evening, {name}")
elif((time>=21 and time<=23) or (time>=0 and time<=4)):
    print("Good night, {name}")
else:
    print("Inavlid time")