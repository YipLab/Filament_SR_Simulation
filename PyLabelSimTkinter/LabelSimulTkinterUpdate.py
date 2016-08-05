from Tkinter import *
import glob as gb
import os
import sys
import tkMessageBox
import Tkinter
import ttk
import numpy as np
import tkFileDialog

FolderName = sys.argv[1]

from LabelingSimulationFunctions import *

def ButtonAct(boxList1,boxList2,boxList3,boxList4,boxList5):
    checkboxList=np.asarray([boxList1,boxList2,boxList3,boxList4])
    checkboxListNam=np.asarray(['ThunderStorm','Bundles','Images','Plots'])
    print boxList5
    if boxList5:
        Data=getInputFile(FolderName)
        
        #print(Data)
    Sel=checkboxListNam[checkboxList>0]
    FileCFG='varCFG.py'
    SimRun='LabelingSimulationRun.py'
    execfile(FileCFG)
    execfile(SimRun)
    for katSlf in Sel:
        ExtraRun=katSlf+'Run.py'
        #print(ExtraRun)
        execfile(str(ExtraRun))
    return

def getInputFile(IniFold):
    iFile=tkFileDialog.askopenfile(mode='r',initialdir=IniFold)
    Data=np.genfromtxt(iFile.name, delimiter=',')
    return Data

def ButtonCheck(boxList1,boxList2,boxList3,boxList4):
    checkboxList=np.asarray([boxList1,boxList2,boxList3,boxList4])
    checkboxListNam=np.asarray(['ThunderStorm','Bundles','Images','Plots'])
    Sel=checkboxListNam[checkboxList>0]
    LenFil=int(MFilLth/TrueSpc)+1 ##Length of array for filament coordinates
    print(checkboxList>0)
    print(checkboxListNam)
    print(checkboxList)
    print(Sel)

def add_entry(master, text, default):
    column, row = master.grid_size()
    label = Label(master, text=text)
    label.grid(row=row, column=0, sticky=E, padx=2)
    entry = Entry(master)
    entry.grid(row=row, column=1, columnspan=2, sticky=E+W)
    entry.insert(0,default)
    return entry


def naccheck(entry1, entry2, var):
    if var.get():
        entry1.configure(state='disabled')
        entry2.configure(state='disabled')
    else:
        entry1.configure(state='normal')
        entry2.configure(state='normal')

top = Tkinter.Tk()    
top.title("Filament Simulation")
GlobFrame = Frame(top)
GlobFrame.grid()
#Grid.columnconfigure(grid, x, weight=1)



CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
#varG = IntVar()

C1 = Checkbutton(top, text = "ThunderStorm", variable = CheckVar1, onvalue = 1, offvalue = 0, height=0, width = 15)
C2 = Checkbutton(top, text = "Bundles", variable = CheckVar2, onvalue = 1, offvalue = 0, height=0, width = 15)
C3 = Checkbutton(top, text = "Images", variable = CheckVar3, onvalue = 1, offvalue = 0, height=0, width = 15)
C4 = Checkbutton(top, text = "Plots", variable = CheckVar4, onvalue = 1, offvalue = 0, height=0, width = 15)



bottomframe = Frame(top)
#bottomframe.grid(row=0,column=0)
#C1.pack(side=RIGHT)
#C2.pack(side=RIGHT)
#C3.pack(side=RIGHT)
C1.grid(row=0,column=1)
C2.grid(row=0,column=2)
C3.grid(row=0,column=3,sticky=W)
C4.grid(row=0,column=3)

SimulSets = ttk.PanedWindow(top, orient=VERTICAL)
f1 = ttk.Labelframe(SimulSets, text='Simulation Settings', width=200, height=200)
SimulSets.add(f1)
SimulSets.grid(row=1,column=3,rowspan=2,padx=50)
MFilLth=add_entry(f1, text="Filament length [um]", default='20')
TrueSpc=add_entry(f1, text="Underlying periodicity [um]", default='0.035')
Iter=add_entry(f1, text="Iterations [int]", default='100')
BundleSpacing=add_entry(f1, text="Bundle interfilament spacing [um]", default='0.005')
BundleNum=add_entry(f1, text="Maximum Number of filaments in a Bundle [int]", default='100')
RendRes=add_entry(f1, text="Resolution of rendred images [um]", default='0.001')
SimulExpLgth=add_entry(f1, text="Enter Simulation Experiment total frames [int]", default='5000')
SimulExpAct=add_entry(f1, text="Enter Simulation Experiment activation ratio [%]", default='2')


CheckVarExt = IntVar()
CExt = Checkbutton(top, text = "Use external csv", variable = CheckVarExt, onvalue = 1, offvalue = 0, height=0, width = 15,command=lambda ent1=MFilLth, ent2=TrueSpc, v=CheckVarExt: naccheck(ent1,ent2,v))
CExt.grid(row=0,column=3,sticky=E)


CheckVarSimulExp = IntVar()
CExt = Checkbutton(top, text = "Use external csv", variable = CheckVarSimulExp, onvalue = 1, offvalue = 0, height=0, width = 15,command=lambda ent1=SimulExpLgth, ent2=SimulExpAct, v=CheckVarSimulExp: naccheck(ent1,ent2,v))
CExt.grid(row=0,column=4,sticky=w)


RunButton = Button(GlobFrame, text="Run Simulation", command=lambda:ButtonAct(CheckVar1.get(),CheckVar2.get(),CheckVar3.get(),CheckVar4.get(),CheckVarExt.get()), fg='red')
RunButton.grid(row=0,column=0)#.pack(side = BOTTOM)

Mods=ttk.Notebook(top)
Pan1=ttk.Frame(Mods)
Mods.add(Pan1, text='Antibody')
Grid.columnconfigure(Pan1, 1, weight=1)

Pan2=ttk.Frame(Mods)
Mods.add(Pan2, text='Nanobody')
Grid.columnconfigure(Pan2, 1, weight=1)

Pan3=ttk.Frame(Mods)
Mods.add(Pan3, text='Fluorescent Protein')
Grid.columnconfigure(Pan3, 1, weight=1)

Secondary = True
ABFolder=add_entry(Pan1, text="Folder", default='Antibody/')
ABLabEff=add_entry(Pan1, text="Labelling efficiency [%]", default='70')
AB1LabPerLoc=add_entry(Pan1, text="Number of Primary antibody per localization [int]", default='2')
AB2LabPerLoc=add_entry(Pan1, text="Number of Secondary antibody per localization [int]", default='4')
ABFlPerLabMin=add_entry(Pan1, text="Minimum number of fluorophores per antibody [int]", default='6')
ABFlPerLabMax=add_entry(Pan1, text="Maximum number of fluorophores per antibody [int]", default='8')
ABsize=add_entry(Pan1, text="Maximum extended size of antibody [um]", default='0.020')


NanoB = True
NBFolder=add_entry(Pan2, text="Folder", default='Nanobody/')
NBLabEff=add_entry(Pan2, text="Labelling efficiency [%]", default='85')
NB1LabPerLoc=add_entry(Pan2, text="Number of Primary link to target -leave as zero for disable- [int]", default='0')
NB2LabPerLoc=add_entry(Pan2, text="Number of Secondary nanobody per localization [int]", default='2')
NBFlPerLabMin=add_entry(Pan2, text="Minimum number of fluorophores per nanobody [int]", default='1')
NBFlPerLabMax=add_entry(Pan2, text="Maximum number of fluorophores per antibody [int]", default='2')
NBsize=add_entry(Pan2, text="Maximum extended size of antibody [um]", default='0.010')


FP =True
FPFolder=add_entry(Pan3, text="Folder", default='FP/')
FPLabEff=add_entry(Pan3, text="Labelling efficiency [%]", default='100')
FP1LabPerLoc=add_entry(Pan3, text="Number of Primary link to target -leave as zero for disable- [int]", default='0')
FP2LabPerLoc=add_entry(Pan3, text="Number of FP per localization [int]", default='1')
FPFlPerLabMin=add_entry(Pan3, text="Minimum number of fluorophores per FP [int]", default='1')
FPFlPerLabMax=add_entry(Pan3, text="Maximum number of fluorophores per FP [int]", default='1')
FPsize=add_entry(Pan3, text="Maximum extended size of FP [um]", default='0.005')

Mods.grid(row=2,column=0,columnspan=3)

#LoadCsvButton = Button(GlobFrame, text="Load external csv", command=lambda:getInputFile(FolderName), fg='blue')
#Data.shape
#LoadCsvButton.grid(row=0,column=1,sticky=E)
#Data2=LoadCsvButton.cget("command")


L1 = Label(top, text="Yip Lab")
L1.grid(row=3,column=3,sticky=E)


#E1 = Entry(top, bd =5)
#L2 = Label(top, text="Labelling efficiency [%]")
#E2 = Entry(top, bd =5)
#
#E1.pack( side = RIGHT)

#E2.pack( side = LEFT)
#L2.pack( side = RIGHT)

#for x in range(10):
#  Grid.columnconfigure(top, x, weight=1)

#for y in range(5):
#  Grid.rowconfigure(top, y, weight=1)


top.mainloop()
