#!/usr/bin/python
'''
This python script is used to calculate the time , where the data and speed of transfer are given as input Like 
DATA:512 KB SPEED:1 Mbps
'''
b=1		#bit
B=8*b		#Byte
KB=1024*B	#KiloByte
MB=1024*KB	#MegaByte
GB=1024*MB	#GigaByte
data=input('Enter the Data in the form of "512 KB or MB or GB" ')

Kb=1024*b	#Kilobit
Mb=1024*Kb	#Megabit
Gb=1024*Mb	#Gigabit
speed=input('Enter the speed in the form of "1 Mbps or Gbps" ')

x=data.split(" ")

if x[1]=="KB":
    databit=int(x[0])*KB
elif x[1]=="MB":
    databit=int(x[0])*MB
elif x[1]=="GB":
    databit==int(x[0])*GB
else:
    print ("error! Please Enter in this Format 234 KB or 4434 MB or 244 GB")

y=speed.split(" ")

if y[1]=="Mbps":
    speedbit=int(y[0])*Mb
elif y[1]=="Gbps":
    speedbit=int(y[0])*Gb
else:
    print ("error! Please Enter in this Format 100 Mbps or 2 Gbps")
time=databit/speedbit

print ("For {} data at {} speed it takes {}  Time!".format(data,speed,time))

