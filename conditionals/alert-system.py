#  we are build smart thermostat

device_status = "unactive"
temp = 89

if(device_status == "active" and temp>35):
    print("high temprature alert ")
else:
    print("temprature is normal")


if device_status == "active":
    if temp>35:
        print("high temp alert")
    else:
        print("temp is normal")
else:
    print("device is offline")        