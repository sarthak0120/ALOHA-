import numpy as np

# Initialize 
IAT = []
AT = []
transmitting = False
num_transmissions = 0
num_succ = 0

# Input Parameters
TT = int(input("Enter Total Time(s): "))
FT = float(input("Enter single frame transmission time(s): "))
G = float(input("Enter Attempt Rate(per frame time): "))


for i in range(int(TT/FT)):
    num_transmissions += int(np.random.poisson(G))

num_transmissions+= int(np.random.poisson(G*(TT%FT)/FT))

# Populate Inter-Arrival-Times (IAT)
for i in range(num_transmissions-1):
    IAT.append(int(np.random.exponential(1/G)*1000))
    
    
# Populate Arrival-Times (AT)
for i in range(num_transmissions):
    if i == 0:
        AT.append(0)    
    else:
        AT.append(AT[i-1] + IAT[i-1])

# Simulation of Pure ALOHA Protocol (i is simulation clock)
FT_copy = FT*1000
for i in range(TT*1000):    
    
    if transmitting:
        if i in AT:
            transmitting = False
            FT_copy = FT*1000
        else:
            FT_copy-=1
            if FT_copy==0:
                num_succ+=1
                transmitting = False
                FT_copy = FT*1000
            
    elif not transmitting:
        if i in AT:
            transmitting = True
            FT_copy = FT*1000
        else:
            continue

print("Throughput is: ", num_succ*FT/TT)