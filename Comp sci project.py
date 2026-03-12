import serial
import csv
import os

ser = serial.Serial("COM3",115200)
line = ser.readline().decode("utf-8",errors="ignore").strip()


for x in range(4):
    print(line)
    parts = line.split(",")
    #print(parts)
    BR3_sim_result = parts[0]
    moisture = parts[1]
    extTemp = parts[2]
    print("MySimResult is ", BR3_sim_result, "My Moisture is ", moisture, "MyTemp is ", extTemp, )
    
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([BR3_sim_result,moisture,extTemp,])


import pandas as pd
import serial


def get_alert(score):
    if score > 15:
        return "High Flood Risk"
    return "No Flood Risk- Safe"

def check_flood_risk(x,z):
    #print("indside func")
    risk = x*z
    if x > 2000:
        return "High Flood Risk"
    return "No flood risk"

df['Flood_risk'] = df['Moisture'] * 5
df['Alert'] = df['Flood_risk'].apply(get_alert)
print(df['Alert'].value_counts())
print(df)

ser = serial.Serial("COM3",115200)
#ser.open()
port = "COM3"
print(port)
if port:
    print(f"Connected to {port}")
   
else:
    print("No MicroBit Found")
print('Live Data')
while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
    data = line.split(':')
    print("data",data)
    #print("data[2]",data[2])
    x = int(data[1])   #microbit moisture
    y = int(data[2])   #microbit temp
    z = 2 #Moisture multiplier
    temp = int(data[1])
    
    risk = check_flood_risk(x,z)
    print(f'risk-{risk}')
        

import pandas as pd
import serial



def get_alert(score):
    if score > 15:
        return "High Flood Risk"
    return "No Flood Risk- Safe"

def check_flood_risk(x,z):
    #print("indside func")
    risk = x*z
    if x > 2000:
        return "High Flood Risk"
    return "No flood risk"

df['Flood_risk'] = df['Moisture'] * 5
df['Alert'] = df['Flood_risk'].apply(get_alert)
print(df['Alert'].value_counts())
print(df)

ser = serial.Serial("COM3",115200)
#ser.open()
port = "COM3"
print(port)
if port:
    print(f"Connected to {port}")
 
else:
    print("No MicroBit Found")
print('Live Data')
while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
    data = line.split(':')
    print("data",data)
  
    x = int(data[1]) 
    y = int(data[2])   
    z = 2 
    temp = int(data[1])
  
    
    risk = check_flood_risk(x,z)
    print(f'risk-{risk}')
        

