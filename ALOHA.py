import numpy as np

num_nodes = 10
transmission_time = 12
num_transmissions_done = 0

total_time = int(input("Enter total simulation time: "))
N = int(input("Enter N: "))

channel_busy = False

waiting = [0 for i in range(num_nodes)]
k = [0 for i in range(num_nodes)]

curr_sender = None
curr_start_time = None

p_send = 2.718**(-N/(num_nodes*transmission_time))*(N/(num_nodes*transmission_time))

for i in range(total_time):
    random = []
    sending = []
    num_senders = 0
    temp=0
    
    
    
    for j in range(num_nodes):
        random.append(np.random.rand())
        
    for j in range(num_nodes):
        if j == curr_sender :
            continue
        
        if random[j]<p_send:
            sending.append(1)
            num_senders = num_senders + 1
            temp = j
        else:
            sending.append(0)
    
    if channel_busy and i == curr_start_time + transmission_time:
        channel_busy = False
        curr_sender = curr_start_time = None
        num_transmissions_done +=1
        
    if not channel_busy and num_senders ==1 :
        channel_busy = True
        curr_sender = temp
        curr_start_time = i
    
    elif num_senders>= 1:
        for item in range(num_nodes):
            if sending[item]==1:
                k[item]=k[item]+1
        
                waiting[item] = i + np.random.randint(2**k[item]-1)*transmission_time
        if channel_busy:
            k[curr_sender] = k[curr_sender] + 1
            waiting[curr_sender] = i + np.random.randint(2**k-1)*transmission_time
        
        channel_busy = False
        curr_sender = None
        curr_start_time = None
        
