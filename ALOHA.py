import numpy as np

# Initialize Parameters
serviced = []
curr_process = 0
IAT = []
AT = []
transmitting = FALSE

# Input Parameters

TT = int(input("Enter Total Time(s): "))
FT = input("Enter single frame transmission time(s): ")
G = input("Enter Attempt Rate(per frame time): ")


num_transmissions = 0
num_succ = 0
for i in range(int(TT/FT)):
    num_transmissions += int(np.random.poisson(G))
    
num_transmissions+= int(np.random.poisson(G*(TT%FT)/FT))

# Populate Inter-Arrival-Times (IAT)
for i in range(num_transmissions-1):
    IAT.append(int(np.random.exponential(1/G)*100))


# Get Arrival-Times (AT)
for i in range(num_transmissions):
    if i == 0:
        AT.append(0)    
    else:
        AT.append(AT[i-1] + IAT[i])

# Simulation of Pure ALOHA Protocol (i represents current time)
for i in range(TT*100):    
    
print("Throughput is: ", num_succ/TT)