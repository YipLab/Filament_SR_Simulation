if  CheckVarExt.get():
    MFilLth=Data[:,0].max()
    PosSort=np.argsort(Data[:,0],0)
    TrueSpc=np.diff(Data[PosSort,0]).mean()
    LenFil=len(Data[:,0])
else:
    MFilLth=float(MFilLth.get()) #[um] Filament length 
    TrueSpc=float(TrueSpc.get())#[um] underlying periodicity
    LenFil=len(range(0,MFilLth,TrueSpc))#LenFil=int(MFilLth/TrueSpc)+1

 ##Length of array for filament coordinates                                                            

Secondary = True #[#] Priamry/Secondary labelling                                                                                   
ABFolder =str(ABFolder.get())
ABLabEff =float(ABLabEff.get()) #[%] antibody labelling efficiency                                                                                    
AB1LabPerLoc =float(AB1LabPerLoc.get()) #[#] num of Primary antibody per localization                                                                      
AB2LabPerLoc =float(AB2LabPerLoc.get()) #[#] num of Secondary antibody per localization                                                                    
ABFlPerLabMin =float(ABFlPerLabMin.get()) #[#] min num of fluorophores per antibody                                                                         
ABFlPerLabMax =float(ABFlPerLabMax.get()) #[#] max num of fluorophores per antibody                                                                         
ABsize =float(ABsize.get())#[um] size of antibody primary + secondary                                                                            

NanoB = True
NBFolder =str(NBFolder.get())
NBsize =float(NBsize.get()) #[um] size of nanobody                                                                                               
NB1LabPerLoc =float(NB1LabPerLoc.get()) #[#] num of nanobody per localization been 0 to disable its effect                                                 
NB2LabPerLoc =float(NB2LabPerLoc.get()) #[#] num of nanobody per localization                                                                              
NBFlPerLabMin =float(NBFlPerLabMin.get())#[#] min num of fluorophores per nanobody                                                                          
NBFlPerLabMax =float(NBFlPerLabMax.get())#[#] max num of fluorophores per nanobody                                                                          
NBLabEff =float(NBLabEff.get()) #[%] nanobody labelling efficiency                                                                                    

FP =True
FPFolder =str(FPFolder.get())
FPsize =float(FPsize.get()) #[um] size of Fluorescent Protein (FP)                                                                               
FP1LabPerLoc =float(FP1LabPerLoc.get()) #[#] num of FP per localization                                                                                    
FP2LabPerLoc =float(FP2LabPerLoc.get()) #[#] num of FP per localization                                                                                    
FPFlPerLabMin =float(FPFlPerLabMin.get())#[#] min num of fluorophores per FP                                                                                
FPFlPerLabMax =float(FPFlPerLabMax.get())#[#] max num of fluorophores per FP                                                                                
FPLabEff =float(FPLabEff.get()) #[%] FP labelling efficiency                                                                               
Iter=int(Iter.get())
BundleSpcing=float(BundleSpacing.get())
BundleNum=int(BundleNum.get())
RendRes=float(RendRes.get())
