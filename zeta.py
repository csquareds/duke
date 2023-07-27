import matplotlib
from matplotlib import pyplot as plt

# zeta potential figure
plt.figure(figsize=(4,7))

xpos = [1,2,3,4]
NPs = ['NH2 PS', 'COOH PS', 'NH2 MagNPs', 'COOH MagNPs'] # nanoparticle names
zeta = [20.56666667,-30.11111111,-27.18888889,-41.03333333] # zeta potential values, respectively
errors = [2.968725877,1.189926857,2.592796288,4.631774318] # error values, respectively
x = [0.4,1,2,4.6]
y = [0,0,0,0]
plt.bar(xpos, zeta, width=0.5, yerr= errors, alpha=0.5, capsize=3, color='gray', edgecolor='black') # label=NPs
plt.plot(x, y, color='black')
plt.xticks(xpos, NPs, rotation = 45)
plt.xlabel('Nanoparticles')
plt.ylabel('mV')
#plt.title('Zeta potential of nanoparticles')

# display
plt.show()