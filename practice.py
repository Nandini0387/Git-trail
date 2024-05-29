process_id = []
arrival_time = []
burst_time = []
min = 0
count = int(input("Enter no. of processess"))
while count!=0:
        process_id.append(int(input("Enter Process ID"))) 
        arrival_time.append(int(input("Enter Arrival Time")))
        burst_time.append(int(input("Enter Burst Time")))
        count -=1
count = 0
while count < len(process_id):
    for i in range(0,len(arrival_time)):
        if arrival_time[i] != arrival_time[-1]:
            if arrival_time[i] < arrival_time[i+1]: 
               min = arrival_time[i]
            else:
               min = arrival_time[i+1]
        else:
            min = arrival_time[-1]
    print(min,burst_time[i])
    arrival_time.pop(min)
    burst_time.pop(burst_time[i])
    count -=1
