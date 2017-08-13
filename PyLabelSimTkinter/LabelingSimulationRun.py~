
os.chdir(FolderName)

if boxList5:
    MFil=Data
else:
    MFilx = np.arange(0,MFilLth,TrueSpc)
    MFily = np.arange(0,MFilLth,TrueSpc)*0
    MFil=np.zeros([LenFil,2])
    MFil[:,0]=MFilx
    MFil[:,1]=MFily

os.mkdir(ABFolder)
FilCall(MFil,MFilLth,ABLabEff,LenFil,AB1LabPerLoc,AB2LabPerLoc,ABFlPerLabMin,ABFlPerLabMax,ABsize,Iter,ABFolder)
os.mkdir(NBFolder)
FilCall(MFil,MFilLth,NBLabEff,LenFil,NB1LabPerLoc,NB2LabPerLoc,NBFlPerLabMin,NBFlPerLabMax,NBsize,Iter,NBFolder)
os.mkdir(FPFolder)
FilCall(MFil,MFilLth,FPLabEff,LenFil,FP1LabPerLoc,FP2LabPerLoc,FPFlPerLabMin,FPFlPerLabMax,FPsize,Iter,FPFolder)

os.chdir('/home/yipgroup/image_store/Scripts/PyLabelSimTkinter/')
