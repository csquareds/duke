import matplotlib
from matplotlib import pyplot as plt

# dls figure
NPs = ['NH2 PS', 'COOH PS', 'NH2 MagNPs', 'COOH MagNPs']
xpos = [0,1,2,3] # 0.1,1.1,2.1,3.1
DLS = [966.4,217.9666667,181.8333333,222.6333333]
PDI = [0.156,0.014333333,0.290333333,0.179333333]
DLSerrors = [52.21905782,1.266227994,44.74174039,15.03606775]
PDIerrors = [0.074303432,0.008144528,0.089578643,0.044049215]

fig, ax1 = plt.subplots(figsize=(4,7))
ax2 = ax1.twinx()

ax1.bar(NPs, DLS, color='gray',label='Average d.nm',width=0.5, yerr=DLSerrors, capsize=3, alpha=0.5,edgecolor='black')
ax2.scatter(xpos, PDI,color='navy',label='Average PDI')
ax2.errorbar(xpos, PDI, yerr=PDIerrors, fmt="o",capsize=3, color='navy',alpha=0.5)
ax1.set_xticklabels(NPs, rotation=45)

ax1.set_xlabel('Nanoparticles')
ax1.set_ylabel('d.nm')
ax2.set_ylabel('PDI')

# display
plt.show()