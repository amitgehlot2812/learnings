import time

timestamp = time.strftime('%H:%M:%S')
print(f"Current time is: {timestamp}")

if '06:00:00' <= timestamp < '12:00:00': 
    print("Good Morning Sir!")
elif '12:00:00' <= timestamp < '18:00:00':
    print("Good Afternoon Sir!")
elif '18:00:00' <= timestamp <= '23:59:59':
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
