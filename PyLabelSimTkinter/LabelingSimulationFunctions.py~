import random as rnd
import numpy as np
import pandas as pd
import os

#def rndSel(Arr,Lth):
    #rnd.jumpahead(Nn)
#    RndFil=rnd.sample(Arr,Lth)
#    return RndFil;

def Lims(idX,Data):
    Lim=np.zeros([2,1])
    for kat1 in idX: 
        Tdata=Data[[kat1]].values
        Tdata=Tdata[~np.isnan(Tdata)]
        if len(Tdata):
            Lim[1]=max(np.nanmax(Tdata),Lim[1])  
            Lim[0]=min(np.nanmin(Tdata),Lim[0])
    return Lim;


def LstToDF(lSt,iDx,cOl):
    dfOut=pd.DataFrame(index=iDx,columns=cOl)
    Ridx=0
    Cidx=0
    for kat in lSt:
        #print(kat,Ridx,Cidx)
        if kat is (False):
            Ridx+=1  
            Cidx=0
        else:
            dfOut.iloc[Ridx,Cidx]=kat
            Cidx+=1
        #print(dfOut.iloc[Ridx,Cidx])
    return dfOut;

def DumpTest(LstDump) :
    with open('CheckLst.dat', 'wb') as f:
        for s in LstDump:
            s1 = str(s) + '\n'
            f.write(bytes(s1, 'UTF-8'))
    return;

def MaxLab(lst):
    MaxNum=0
    Pos0=0
    for Pos, Num in enumerate(lst):
        if Num is (False):
            PosDiff=Pos-Pos0
            Pos0=Pos
            MaxNum=max(MaxNum,PosDiff)
    return MaxNum

def RndDist(Sz):
    VarRet=(rnd.random()-0.5)/0.5*Sz
    return VarRet;

def TestRND(INT):
    Vp=[]
    for kat in range(10000):
        Vp.append(rnd.randint(1,INT))
    pp.hist(Vp)
    pp.show()
    return;

def rndPop(Arr,L1PL,L2PL,FPLn,FPLx,Sz): 
    VarOut=[]
    for kat in range(len(Arr)):##Loops on the filaments entities
        if L1PL:
            NL1=rnd.randint(1,L1PL)
        else:
            NL1=1
        VarOut.append(Arr[kat,0])
        VarOut.append(Arr[kat,1])
        for kat1 in range(NL1): ## Loops on the number of Primary Labelling units
            NL2=rnd.randint(1,L2PL)
            Dx1=RndDist(min(kat1,Sz))
            Dy1=RndDist(min(kat1,Sz))
            for kat2 in range(NL2):##Loops on the number of Secondary Labelling unit
                NF=rnd.randint(FPLn,FPLx)
                for kat3 in range(NF):
                    Dx = RndDist(Sz)+Dx1#Difference in x from the real location
                    xABS = Arr[kat,0]+Dx# real x location
                    VarOut.append(xABS)
                    Dy = RndDist(Sz)#Difference in x from the real location
                    yABS = Arr[kat,1]+Dy+Dy1# real x location
                    VarOut.append(yABS)#Difference in y from the real location
        VarOut.append(False)
    return VarOut;

def FilCreation(MFil,MFilLth,ABLabEff,LenFil,AB1LabPerLoc,AB2LabPerLoc,ABFlPerLabMin,ABFlPerLabMax,ABsize):
    MFilPos=int(LenFil*ABLabEff/100)#MFilLth/TrueSpc
    rnd.seed()
    #IntJA=rnd.randint(0,100)
    #print("LenFil",LenFil)
    #print("MFilPos",MFilPos)
    #print("LenFil",LenFil)
    MFilPosR=range(LenFil)
    MFilRnd=rnd.sample(MFilPosR,MFilPos)
    ArrToPop=MFil[MFilRnd]
    sortPos=np.argsort(MFil[MFilRnd,0])
    ArrToPop=ArrToPop[sortPos]
    MFilLab=rndPop(ArrToPop,AB1LabPerLoc,AB2LabPerLoc,ABFlPerLabMin,ABFlPerLabMax,ABsize)
    return MFilLab,np.sort(MFilRnd);

def FilCall(MFil,MFilLth,ABLabEff,LenFil,AB1LabPerLoc,AB2LabPerLoc,ABFlPerLabMin,ABFlPerLabMax,ABsize,Iter,ABFolder):
    for katIt in range(Iter):#if Secondary:
        MFilLab, MFilIdx = FilCreation(MFil,MFilLth,ABLabEff,LenFil,AB1LabPerLoc,AB2LabPerLoc,ABFlPerLabMin,ABFlPerLabMax,ABsize)
        MaxLabls=MaxLab(MFilLab)
        Cols=range(MaxLabls)
        OutPut=LstToDF(MFilLab,MFilIdx,Cols)
        OutPut.to_csv(ABFolder+'Filament'+str(katIt)+'_'+str(MFilLth)+'um.csv')


