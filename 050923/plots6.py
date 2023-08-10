import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as skl
from sklearn import *
import os

Data = []
Bfield = ['-1.06, 0.273', '-1.06, 0.265', '-2.14, 0.353', '-2.15, 0.36', '-3.02 0.442', '-3.02, 0.442', '-0.06, 0.20', '-0.072, 0.19', '-0.303 0.201', '-.304,0.209', ' -0.573 0.213', '-0.567, 0.22', '-1.06, 0.271', '-1.06 0.26', '-2.14, 0.360', '-2.145 0.370']
MagPos = ['10, 0', '10, 0', '15, 0', '15 ,0', '18,0', '18, 0', '3, 0', '3, 0', '5, 0', '5, 0', '7, 0', '7, 0', '10, 0', '10, 0', '15, 0', '15, 0']
folder = r'W:\shared\Jonathon\ODMR_BfieldBasesline\050923\Data'
for files in sorted( os.listdir(folder)):
    df = pd.read_csv(os.path.join(folder,files), header = None)
    Data.append(df)

def MultiPlot(Data, MagPos,Bfield):
     for idx1, data1 in enumerate(Data[5:]):
         freq1 = data1[0]
         inten1 = data1[1]
         for idx, data in enumerate(Data[4:]):
             freq = data[0]
             inten = data[1]
             fig, ax=plt.subplots() 
             plt.plot(freq, inten, label = 'B1 and B2 ({})[mT]      Mag1 and Mag2 Position ({})'.format(Bfield[idx], MagPos[idx]))
             plt.plot(freq1,inten1)
             ax.set(xlabel="Frequency [MHz]", ylabel="Amplitude")
             #plt.title('B1 and B2 ({})[mT]      Mag1 and Mag2 Position ({})'.format(Bfield[idx1], MagPos[idx1]), fontsize =8)
             plt.legend()
             #plt.savefig('test%d'%idx1)
             plt.show()
    
    
    
def SinglePlot(Data, MagPos,Bfield):
    for idx, data in enumerate(Data[4:]):
        fig, ax=plt.subplots()
        freq = data[0]
        inten = skl.preprocessing.normalize(data[1])
        plt.plot(freq, inten)
        ax.set(xlabel="Frequency [MHz]", ylabel="Amplitude")
        plt.title('B1 and B2 ({})[mT]\nMag2 and Mag1 Position ({})'.format(Bfield[idx], MagPos[idx]), fontsize =8)
        plt.savefig('test%d'%idx)
        plt.show()


def Cauchy(Amp, x0, Gamma, Afit, Bfit):
   g = Amp/(1 + ((x -x0)/Gamma^2))
   return g

    
#multiplot =  MultiPlot(Data, MagPos,Bfield)
#singleplot = SinglePlot(Data, MagPos,Bfield)
print(sorted(os.listdir(folder)))

freq = Data[14][0]
inten = skl.preprocessing.minmax_scale(Data[14][1])

freq1 = Data[14][0]
inten1 = skl.preprocessing.minmax_scale(Data[15][1])

fig, ax=plt.subplots()

plt.plot(freq, inten, label ='B1 and B2 ({})[mT]\nMag2 and Mag1 Position ({})'.format(Bfield[14], MagPos[14]))
plt.plot(freq1, inten1, label ='B1 and B2 ({})[mT]\nMag2 and Mag1 Position ({})'.format(Bfield[15], MagPos[15]))
plt.legend(bbox_to_anchor = (1.05,1.15),loc = 'upper right')
ax.set(xlabel="Frequency [MHz]", ylabel="Amplitude")
ax.grid(which = 'both')
#plt.savefig('dplot0')
plt.show() 
