# example for NB and COOH PS
import matplotlib
from matplotlib import pyplot as plt

import pandas
import numpy as np

# load data from csv
absorb = pandas.read_csv('COOH MNPs - NB Spectrum.csv', header=0)

wv = absorb.loc[:,"Wavelength"]
# adjust as necessary for RB (using quick.py possibly)
adsorb40 = absorb.loc[:,["40.1", "40.2", "40.3"]]
adsorb100 = absorb.loc[:,["100.1", "100.2", "100.3"]]
adsorb200 = absorb.loc[:,["200.1", "200.2", "200.3"]]
adsorb400 = absorb.loc[:,["400.1", "400.2", "400.3"]]
adsorb500s = absorb.loc[:,["500s.1", "500s.2", "500s.3"]]
adsorb1s = absorb.loc[:,["1s.1", "1s.2", "1s.3"]]
adsorb5s = absorb.loc[:,["5s.1", "5s.2","5s.3"]]
adsorb10s = absorb.loc[:,["10s.1", "10s.2", "10s.3"]]

def graph(data,line,name):
    mean = np.mean(data,axis=1)
    error = data.std(axis=1)
    plus = mean + error
    minus = mean - error

    plt.plot(wv,mean,color=line,
        alpha = 1, label=name)
    plt.plot(wv,plus,color=line,
        alpha = 0.2)
    plt.plot(wv,minus,color=line,
        alpha = 0.2)
    plt.fill_between(wv,minus,plus,color=line,alpha = 0.2)

# figure 1 - dye standards
plt.style.use('default')
plt.figure(dpi=100)
hfont = {'fontname':'Arial'}
plt.xlabel("Wavelength (nm)", fontsize = 18, **hfont)
plt.ylabel('Absorbance (a.u.)', fontsize = 18, **hfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

graph(adsorb40,'firebrick','40 µg/mL')
graph(adsorb100,'orange','100 µg/mL')
graph(adsorb200,'green','200 µg/mL')
graph(adsorb400,'blue','400 µg/mL')

plt.legend(title='Concentration of NB Dye')

# figure 2 - NP samples
plt.style.use('default')
plt.figure(dpi=100)
hfont = {'fontname':'Arial'}
plt.xlabel("Wavelength (nm)", fontsize = 18, **hfont)
plt.ylabel('Absorbance (a.u.)', fontsize = 18, **hfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

graph(adsorb500s,'indigo','500 µg/mL')
graph(adsorb1s,'orchid','1 mg/mL')
graph(adsorb5s,'gold','5 mg/mL')
graph(adsorb10s,'darkcyan','10 mg/mL')

plt.legend(title='Concentration of COOH MNP Sample')

# figure 3 - dye standards and samples
plt.style.use('default')
plt.figure(dpi=100)
hfont = {'fontname':'Arial'}
plt.xlabel("Wavelength (nm)", fontsize = 18, **hfont)
plt.ylabel('Absorbance (a.u.)', fontsize = 18, **hfont)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

graph(adsorb40,'firebrick','40 µg/mL')
graph(adsorb100,'orange','100 µg/mL')
graph(adsorb200,'green','200 µg/mL')
graph(adsorb400,'blue','400 µg/mL')
graph(adsorb500s,'indigo','500 µg/mL')
graph(adsorb1s,'orchid','1 mg/mL')
graph(adsorb5s,'gold','5 mg/mL')
graph(adsorb10s,'darkcyan','10 mg/mL')
plt.legend()

# display all graphs
plt.show()