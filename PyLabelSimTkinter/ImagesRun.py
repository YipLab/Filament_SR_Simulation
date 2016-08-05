#import pandas as pd
#import glob as gb
#import os
#import matplotlib.pyplot as pp
#import numpy as np
#import matplotlib.cm as cm
#import random as rnd
import scipy.signal as ss
import scipy

Folders=[]
os.chdir(FolderName)
print(FolderName)

AvgErr=0.020#[um] average std of the gaussian representation
AvgErrVar=0.010#[um] average std of the gaussian representation
#RendRes=0.001#[um/px] resolution to render the image
FolderOut='Render_'+str(int(RendRes*10**3))
Padd=int(AvgErr/RendRes*10)#[px] number of pixels to padd at the edges
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
    os.mkdir(FolderOut)
    FileNames=gb.glob('Filament*.csv')
    for katN in FileNames:
        rnd.seed()
        print(katN)
        Data=pd.DataFrame.from_csv(katN)
        LenIdx = len(Data.index)
        #colors = cm.rainbow(np.linspace(0, 1, LenIdx))
        #pp.clf()
        #ColPos=np.arange(LenIdx)
        #rnd.shuffle(ColPos)
        idXx=Data.columns[np.arange(0,len(Data.columns),2)]
        LimX=Lims(idXx,Data)
        DX=np.squeeze(LimX[1]-LimX[0])
        Xpix=int(np.ceil(DX/RendRes))+Padd*2
        idXy=Data.columns[np.arange(1,len(Data.columns),2)]
        LimY=Lims(idXy,Data)
        DY=np.squeeze(LimY[1]-LimY[0])
        Ypix=int(np.ceil(DY/RendRes))+Padd*2
        RendImg=np.zeros([Ypix,Xpix])
        for katIdx in range(len(Data.index)):
            XY=np.squeeze(Data.iloc[[katIdx]].values)  
            XY=XY[~np.isnan(XY)]
            X0=XY[0]
            Y0=XY[1]
            Xi=np.arange(2,len(XY),2)
            Yi=np.arange(3,len(XY),2)
            for katBlob in range(len(Xi)):
                RndErr=np.random.normal(AvgErr,AvgErrVar/3)#AvgErrVar is taken as 3 stndard deviation
                BlobS=int(np.ceil(RndErr/RendRes))
                while BlobS<1:
                    RndErr=np.random.normal(AvgErr,AvgErrVar/3)
                    BlobS=int(np.ceil(RndErr/RendRes))
                if np.mod(BlobS,2)==0:
                    BlobS+=1
                G1D=ss.gaussian(BlobS*5,BlobS)
                G2D=np.transpose(np.mat(G1D))*np.mat(G1D)
                Xpos=int(np.round(np.squeeze((LimX[0]+XY[Xi[katBlob]])/RendRes)))
                Ypos=int(np.round(np.squeeze((LimY[0]+XY[Yi[katBlob]])/RendRes)))
                CtrG=int(np.ceil(len(G2D)/2))+1
                Yrange=np.arange(Padd+Ypos-CtrG,Padd+Ypos+(CtrG))
                Xrange=np.arange(Padd+Xpos-CtrG,Padd+Xpos+(CtrG))
                YRn=min(Yrange);YRx=max(Yrange)
                XRn=min(Xrange);XRx=max(Xrange)
                RendImg[YRn:YRx,XRn:XRx]=RendImg[YRn:YRx,XRn:XRx]+G2D
        
        scipy.misc.imsave(FolderOut+'/'+'Render'+katN[0:len(katN)-4]+'.png',RendImg)
        ##pp.matshow(RendImg,cmap=cm.gray)
        ##pp.savefig('Render'+katN[0:len(katN)-4]+'.png')
    os.chdir(FolderName)

os.chdir('/home/yipgroup/image_store/Scripts/PyLabelSim/')
