from numpy import *
import matplotlib.pyplot as plt
from pylab import *


x,y = loadtxt('dataset.csv', delimiter=',',unpack=True)
p15=polyfit(x,y,15)

merged=stack((x, y), axis=-1)

distances=[]
for a,b in merged:
	distances.append([a, abs(b-polyval(p15,a))])

avg=[]
for dist_value in (list(set(x))):
	avg_part=[]
	for part_x,part_y in distances:
		if dist_value==part_x:
			avg_part.append(part_y)
	avg.append([dist_value,mean(avg_part)])



fig = plt.figure(figsize=(18, 9))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
plt.title("Value Classifier")
ax2 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
plt.title("Average Distance Classifier")


colors_val=[]
for a,b in merged:
	if b>polyval(p15,a):
		colors_val.append('#ffb07c')
	else:
		colors_val.append('#c04e01')

ax1.scatter(x,y, s=2,marker='o', c=colors_val)
ax1.plot(x,polyval(p15,x), '#36013f',linewidth='1')

colors_dist=[]
for a,b in merged:
	for value,max_dist in avg:
		if a==value:
			max_dist_part=max_dist
			if abs(polyval(p15,a)-b)>max_dist:
				colors_dist.append('r')

			else:
				colors_dist.append('#3f9b0b')


ax2.scatter(x,y, s=2,marker='o', c=colors_dist)
ax2.plot(x,polyval(p15,x), 'k',linewidth='1')

plt.show()




