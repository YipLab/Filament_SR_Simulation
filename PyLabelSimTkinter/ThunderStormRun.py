#import pandas as pd
#import glob as gb
#import os
#import numpy as np
#import matplotlib.cm as cm
#import random as rnd
Folders=[]
print(FolderName)
FoldOut=os.getcwd()
os.chdir(FolderName)


for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        Folders.append(os.path.join(dirname, subdirname))
FolderGood=[]
for kat in Folders:
    if kat.find('Render')==-1:
       #if kat.find('Bundle')==-1:
        FolderGood.append(kat)
Folders=FolderGood

#iDx=np.arange(np.sum(Data.count().values))
cOl=["frame","x [um]","y [um]","sigma [nm]","intensity [photon]","offset [photon]","bkgstd [photon]","uncertainty [nm]"]
for kat in range(len(Folders)):
    print(Folders[kat])
    os.chdir(Folders[kat])
    FileNames=gb.glob('*.csv')
    for katN in FileNames:
        #print(katN)
        Data=pd.read_csv(katN,header=None)
        iDx=np.arange((np.sum(Data.count(numeric_only=True).values)/2)-len(Data.index.values))
        dfOut=pd.DataFrame(index=iDx,columns=cOl)
        Count=0
        LenIdx = len(Data.index)
        #colors = cm.rainbow(np.linspace(0, 1, LenIdx))
        #pp.clf()
        #ColPos=np.arange(LenIdx)
        #rnd.shuffle(ColPos)
        for katIdx in range(len(Data.index)):
            XY=np.squeeze(Data.iloc[[katIdx]].values)  
            XY=XY[~np.isnan(XY)]
            #X0=XY[0]
            #Y0=XY[1]
            #katkatkat
            Xi=np.arange(2,len(XY),2)
            Yi=np.arange(3,len(XY),2)
            for katPos in np.arange(len(Xi)):
                dfOut.iloc[Count+katPos,1]=XY[Xi[katPos]]
                dfOut.iloc[Count+katPos,2]=XY[Yi[katPos]]
                dfOut.iloc[Count+katPos,7]=0
            Count+=len(Xi)
        dfOut.to_csv('TS_like_'+katN, index=False,na_rep='NaN')
#pp.plot(X0,Y0,'k*')
            #pp.plot(XY[Xi],XY[Yi],color=colors[ColPos[katIdx]],marker='o',linestyle=' ')
        #pp.axis([0.5,1.5,-0.1,0.1])
        #pp.savefig(katN[0:len(katN)-4]+'.png')
    os.chdir(FolderName)

os.chdir(FoldOut)
