import matplotlib
from matplotlib import pyplot as plt
from brokenaxes import brokenaxes
import numpy as np

# NH2 PS
NH2_PS = [568478.6706,284239.3353,56847.86706,28423.93353] # surface area of NH2 PS
RB_NH2_PS = [0.7023517024,0.3018386794,0.04118215321,0.01094319958] # RB NH2 PS PQ slope values

COOH_PS = [2481858.196, 1240929.098,248185.8196,124092.9098] # surface area of COOH PS
RB_COOH_PS = [3.052060962,1.322511753,0.272425897,0.1542543782] # RB COOH PS PQ slope values

MNP = [9927432.785,4963716.393,992743.2785,496371.6393] # surface area of MNPs
RB_NH2_MNP = [0.5547654508,0.2517414177,0.06136025717,0.02532658866] # RB NH2 MNP PQ slope values
RB_COOH_MNP = [0.3783710161,0.2925749319,0.1182320442,0.006164247365] # RB COOH MNP PQ slope values

# RB linear regression at different surface areas
plt.figure()
plt.title('RB  Adsorption')
plt.xlabel('Surface Area ($mm^{2}$/mL)',fontsize=12)
plt.ylabel('Partitioning Quotient',fontsize=12)

def graph(x,y,color,NP):
    plt.scatter(x,y,color=color)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    line = NP + ", y=%.7fx+%.3f"%(z[0],z[1])
    print(NP,z[0])
    plt.plot(x,p(x),color,label=line,alpha=0.5)

graph(NH2_PS,RB_NH2_PS,"red","NH2 PS")
graph(COOH_PS,RB_COOH_PS,"green","COOH PS")
graph(MNP,RB_NH2_MNP,"blue","NH2 MagNPs")
graph(MNP,RB_COOH_MNP,"purple","COOH MagNPs")
plt.legend(fontsize=14)

# NB linear regression at different surface areas
NB_NH2_PS = [1.426239329,0.3075060533,0.05365853659,0.0342846198] # NB NH2 PS PQ values
NB_COOH_PS = [64.74675325,5.409241969,2.312341539,0.8233387358] # NB  COOH PS PQ values
NB_NH2_MNP = [174.6363636,79.5,2.71324236,0.7626129003] # NB NH2 MNP PQ values
NB_COOH_MNP = [867.5714286,137.1818182,19.89347079,1.697027946] # NB COOH MNP PQ values

plt.figure()
plt.title('NB Adsorption')
plt.xlabel('Surface Area ($mm^{2}$/mL)',fontsize=12)
plt.ylabel('Partitioning Quotient',fontsize=12)
graph(NH2_PS, NB_NH2_PS,"red","NH2 PS")
graph(COOH_PS, NB_COOH_PS,"green","COOH PS")
graph(MNP, NB_NH2_MNP,"blue","NH2 MagNPs")
graph(MNP, NB_COOH_MNP,"purple","COOH MagNPs")
plt.legend(fontsize=14)

NPs = ['NH2 PS','COOH PS','NH2 MagNPs','COOH MagNPs']
xpos = [0,1,2,3]
RB = [1.2763821143269165e-06, 1.224096011764534e-06, 5.5326707718702545e-08, 3.613093109821453e-08] # slopes of RB w/ NPs PQ
NB = [2.5262017339370335e-06,2.5960908678338952e-05,1.8770935658705897e-05,8.913139741098231e-05] # slopes of NB w/ NPs PQ

# RB adsorption bar graph, slopes of RB PQ of NPs
plt.figure()
plt.bar(NPs,RB,color='gray',edgecolor='black',width=0.5)
plt.xlabel('Nanoparticles')
plt.ylabel('RB Adsorption')
plt.xticks(xpos,NPs,rotation=45)

# NB adsorption bar graph, slopes of NB PQ of NPs
plt.figure()
plt.bar(NPs,NB,color='gray',edgecolor='black',width=0.5)
plt.xlabel('Nanoparticles')
plt.ylabel('NB Adsorption')
plt.xticks(xpos,NPs,rotation=45)

# DAR figure
DAR = [5.05E-01,4.72E-02,2.95E-03,4.05E-04] # dye adsorption ratios of NPs

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0.05)  # adjust space between axes

# plot the same data on both axes
ax1.bar(NPs,DAR,color='gray',edgecolor='black',width=0.5)
ax2.bar(NPs,DAR,color='gray',edgecolor='black',width=0.5)

# zoom-in / limit the view to different portions of the data
ax1.set_ylim(0.05, 0.52)  # outlier
ax2.set_ylim(0.00004, 4.8E-02)  # most of data

# hide the spines between ax and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 0], transform=ax1.transAxes, **kwargs) # 
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

plt.xticks(xpos,NPs,rotation = 45)
plt.xlabel('Nanoparticles')
plt.ylabel('DAR')

# display all graphs
plt.show()