#%% import modules

%reload_ext autoreload
%autoreload 2


import matplotlib.pyplot as plot
import numpy as np
import random
import math
from dgraph_object import *
from simulation_functions import *
#import dgraph_object
#from dgraph_object import dGraph


#%% define_graph
KBC = 1
KNBC = 1
KD = 2
example_weighted_dgraph = dGraph(edges=[[0,1,KD],[1,0,KD],[2,1,KD],[1,2,KD],[2,3,KD],[3,2,KD],[4,3,KD],[3,4,KD],[5,4,KD],[5,6,KD],[6,5,KD],[6,7,KD],[7,6,KD],[8,7,KD],[7,8,KD],[8,9,KD],[9,8,KD],[10,11,KD],[11,10,KD],[12,11,KD],[11,12,KD],[12,13,KD],[13,12,KD],[13,14,KD],[14,13,KD],[14,15,KD],[15,14,KD],[15,16,KD],[16,15,KD],[16,17,KD],[17,16,KD],[17,18,KD],[18,17,KD],[18,19,KD],[19,18,KD],[0,10,KNBC],[10,0,KBC],[1,11,KNBC],[11,1,KBC],[2,12,KNBC],[12,2,KBC],[3,13,KNBC],[13,3,KBC],[4,14,KNBC],[14,4,KBC],[5,15,KNBC],[15,5,KBC],[6,16,KNBC],[16,6,KBC],[7,17,KNBC],[17,7,KBC],[8,18,KNBC],[18,8,KBC],[9,19,KNBC],[19,9,KBC]],nodes=20,transfers_from = [],transfers_to = [])
transfers_from_nodes(example_weighted_dgraph)
transfers_to_nodes(example_weighted_dgraph)

example_particle_positions = []
for i in range(1000):
    example_particle_positions.append(0)
particle_count = len(example_particle_positions)




#%% Run the simulation and plot relative particle concentrations in the binding region
transfers_from = transfers_from_nodes(example_weighted_dgraph)
transfers_to = transfers_to_nodes(example_weighted_dgraph)

number_non_binding = 0
times = []
quantitiesA = []
quantitiesB = []
y_list = []
time = 0
dt = 0.0001
particle_list_memory = []
for i in range(300000):
    example_particle_positions = one_step(example_weighted_dgraph,example_particle_positions, dt)
    number_non_binding_left = example_particle_positions.count(10)+example_particle_positions.count(11)+example_particle_positions.count(12)+example_particle_positions.count(13)+example_particle_positions.count(14)
    number_non_binding_right = example_particle_positions.count(15)+example_particle_positions.count(16)+example_particle_positions.count(17)+example_particle_positions.count(18)+example_particle_positions.count(19)
    time = time+dt
    times.append(time)
    quantitiesA.append(number_non_binding_left)
    quantitiesB.append(number_non_binding_right)
    y = 1000*(math.e**-time)
    y_list.append(y)
    if i>28000 and i % 1000 == 0:
        particle_list_memory.append(example_particle_positions)


fig, ax = plot.subplots()
ax.plot(times,quantitiesA)
ax.plot(times,quantitiesB)
plot.show()

print(len(particle_list_memory))
#%% Plot mRNA concentration relative to position in space
particle_count_array = []
for i in particle_list_memory:
    sub_particle_count = []
    for j in range(10,20):
        sub_particle_count.append(i.count(j))
    particle_count_array.append(sub_particle_count)

average_particle_count = []
for i in range(0,10):
    sum = 0
    for j in range(len(particle_count_array)):
        sum += particle_count_array[j][i]
    avg = sum/len(particle_count_array)
    average_particle_count.append(avg)

print(average_particle_count)
total_particle_count = 0
for i in average_particle_count:
    total_particle_count += i
positions = []
fractions = []
for i in range(10,20):
    positions.append(i-10)
    fractions.append(average_particle_count[i-10]/total_particle_count)

plot.plot(positions, fractions)