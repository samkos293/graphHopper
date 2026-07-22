#%%
import matplotlib.pyplot as plt
import numpy as np

width = 20
particle_fractions = np.array([])
for i in range(width*2):
    particle_fractions = np.append(particle_fractions,1/(width*2))

kbc = 1
knbc = 1
kd = 2
dt = 0.001
runtime = 30
for i in range(int(runtime / dt)):
    print(i)

    particle_fraction_changes = np.zeros(width*2)
    for j in range(width*2):
        #apply binding/nonbinding movements
        if j < width:
            #top row
            particle_fraction_changes[j] += particle_fractions[j+width]*kbc*dt
            particle_fraction_changes[j] += -1*particle_fractions[j]*knbc*dt
        else:
            #bottom row
            particle_fraction_changes[j] += particle_fractions[j-width]*knbc*dt
            particle_fraction_changes[j] += -1*particle_fractions[j]*kbc*dt
        #apply movements left and right
        if j % width == 0:
            #left edge
            particle_fraction_changes[j] += particle_fractions[j+1]*kd*dt
            particle_fraction_changes[j] += -1*particle_fractions[j]*kd*dt
        elif j % width == width-1:
            #right edge
            particle_fraction_changes[j] += particle_fractions[j-1]*kd*dt
            particle_fraction_changes[j] += -1*particle_fractions[j]*kd*dt
        elif j == (width/2)-1:
            #left of the missing edge
            particle_fraction_changes[j] += particle_fractions[j+1]*kd*dt+particle_fractions[j-1]*kd*dt
            particle_fraction_changes[j] += -1*particle_fractions[j]*kd*dt
        elif j == width/2:
            #right of missing edge
            particle_fraction_changes[j] += particle_fractions[j+1]*kd*dt
            particle_fraction_changes[j] += -2*particle_fractions[j]*kd*dt
        else:
            #normal position
            particle_fraction_changes[j] += particle_fractions[j+1]*kd*dt+particle_fractions[j-1]*kd*dt
            particle_fraction_changes[j] += -2*particle_fractions[j]*kd*dt
    particle_fractions += particle_fraction_changes

xlist = []
ylist = []
for i in range(width,2*width):
    xlist.append(i-width)
    ylist.append(particle_fractions[i])
plt.plot(xlist,ylist)
print(sum(particle_fractions))

# %%
