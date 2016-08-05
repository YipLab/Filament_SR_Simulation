#def RndNm(Nms,Bdm):
#    FNr=rnd.sample(Nms,Bdm)
#    return FNr;


#import pandas as pd
#import glob as gb
#import os
#import matplotlib.pyplot as pp
#import numpy as np
#import matplotlib.cm as cm
#import random as rnd
Folders=[]
FolderBund='Bundle/'
#BundleSpcing=0.005
#BundleNum=50
os.chdir(FolderName)
print(FolderName)
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        Folders.append(os.path.join(dirname, subdirname))
       
FolderGood=[]
for kat in Folders:
    if kat.find('Render')==-1:
        FolderGood.append(kat)
Folders=FolderGood


for kat in range(len(Folders)):
    print(Folders[kat])
    os.chdir(Folders[kat])
    os.mkdir(FolderBund)
    FileNames=gb.glob('Filament*.csv')
    for katN in FileNames:
        DataRoot=pd.DataFrame.from_csv(katN)
        BundleIds=rnd.sample(FileNames,BundleNum-1)
        #print(katN)
        Count=0
        for katNbd in BundleIds: 
            Data=pd.DataFrame.from_csv(katNbd)
            #katkat
            MaxCol=max((Data.columns.values).astype(int))
            ColArr=np.arange(3,MaxCol,2)
            #print(BundleSpcing*Count)
            Data.iloc[:,ColArr]=Data.iloc[:,ColArr]+BundleSpcing*Count
            Count+=1
            DataRoot=DataRoot.append(Data)
        DataRoot.to_csv(FolderBund+katN[0:len(katN)-4]+'_Bundle.csv')
    os.chdir('../')


os.chdir('/home/yipgroup/image_store/Scripts/PyLabelSim/')
