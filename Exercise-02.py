import time
timestamp = time.strftime("%H:%M:%S %p")
hour = int(time.strftime("%H"))

print(timestamp)

if hour<12 :
    print("Good Morning Sir")
elif hour<16 :
    print("Good Afternoon Sir")
elif hour<20 :
    print("Good Evening Sir")
else :
    print("Good Night Sir")            
 

