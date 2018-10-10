import numpy as np

# Initialize Parameters
serviced = []
IAT = []
ST = 12
AT = []


# Input Parameters
total_time = int(input("Enter Total Time: "))
IAT_rate = int(input("Enter IAT Rate: "))


num_processes = np.random.poisson(IAT_rate)
num_processes_served = 0

# Populate Inter-Arrival-Times (IAT)
for i in range(num_processes):
    temp = int(np.random.exponential(IAT_rate))

    if i==0:
        IAT.append(0)
    else:
        IAT.append(temp)


# Get Arrival-Times (AT) from IAT starting at t=0
# and initialize Waiting-Times to 0
for i in range(num_processes):
    if i == 0:
        AT.append(0)    
    else:
        AT.append(AT[i-1] + IAT[i])

# Simulation of M/M/1 Queue (i represents current time)

end_time = -1

for i in range(total_time):    
    for j in range(num_processes):
        if i == j and i>end_time:
            serviced.append(i)
            num_processes_served = num_processes_served + 1
            end_time = i + ST
            break
    
print ("Throughput is: ", num_processes_served/total_time)
                
