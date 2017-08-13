import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
from   pyforms.Controls import *
import matplotlib
matplotlib.use('Agg')

#global random
#import random as rnd

#global numpy
#import numpy as np

#global matplotlib
#import matplotlib.pyplot as pp

#global pandas 
#import pandas as pd

#global sys
import glob as gb

#global os
import os
import sys

FolderName = sys.argv[1]

from LabelingSimulationFunctions import *

class FilamentSimulationGUI(BaseWidget):

    def __init__(self):
        super(FilamentSimulationGUI,self).__init__('Filament Simulation')
        
        #Definition of the forms fields
        self._ABFolder = ControlText('Folder', 'Antibody/')
        self._ABLabEff = ControlText('Labelling efficiency [%]', '70')
        self._AB1LabPerLoc = ControlText('Number of Primary antibody per localization [int]', '2')
        self._AB2LabPerLoc = ControlText('Number of Secondary antibody per localization [int]', '4')
        self._ABFlPerLabMin = ControlText('Minimum number of fluorophores per antibody [int]', '6')
        self._ABFlPerLabMax = ControlText('Maximum number of fluorophores per antibody [int]', '8')
        self._ABsize = ControlText('Maximum extended size of antibody [um]', '0.020')

        self._NBFolder = ControlText('Folder', 'Nanobody/')
        self._NBLabEff = ControlText('Labelling efficiency [%]', '85')
        self._NB1LabPerLoc = ControlText('Number of Primary link to target leave as zero for disable [int]', '0')
        self._NB2LabPerLoc = ControlText('Number of Secondary nanobody per localization [int]', '2')
        self._NBFlPerLabMin = ControlText('Minimum number of fluorophores per nanobody [int]', '1')
        self._NBFlPerLabMax = ControlText('Maximum number of fluorophores per nanobody [int]', '2')
        self._NBsize = ControlText('Maximum extended size of nanobody [um]', '0.010')
        
        self._FPFolder = ControlText('Folder', 'FP/')
        self._FPLabEff = ControlText('Labelling efficiency [%]', '100')
        self._FP1LabPerLoc = ControlText('Number of Primary link to target leave as zero for disable [int]', '0')
        self._FP2LabPerLoc = ControlText('Number of FP per localization [int]', '1')
        self._FPFlPerLabMin = ControlText('Minimum number of fluorophores per FP [int]', '1')
        self._FPFlPerLabMax = ControlText('Maximum number of fluorophores per FP [int]', '1')
        self._FPsize = ControlText('Maximum extended size of FP [um]', '0.001')

        self._MFilLth = ControlText('Filament length [um]', '20')
        self._TrueSpc = ControlText('Underlying periodicity [um]', '0.035')
        self._Iter = ControlText('Iterations [int]', '100')
        self._BundleSpacing = ControlText('Bundle interfilament spacing [um]', '0.005')
        self._BundleNum = ControlText('Maximum Number of filaments in a Bundle [int]', '100')
        self._RendRes = ControlText('Resolution of rendred images [um]', '0.001')
        self._button        = ControlButton('Run Simulation')
        self._checkboxList = ControlCheckBoxList('Extra settings')
        self._checkboxList.value = [('Bundles', True), ('ThunderStorm', True), ('Images', True), ('Plots', False)]

        
        self._button.value = self.__buttonAction
        self._formset = [ {
            'Antibody':['_ABFolder','_ABLabEff','_AB1LabPerLoc','_AB2LabPerLoc','_ABFlPerLabMin','_ABFlPerLabMax','_ABsize'],#,'||','_middlename','||','_lastname'], 
        'Nanobody':['_NBFolder','_NBLabEff','_NB1LabPerLoc','_NB2LabPerLoc','_NBFlPerLabMin','_NBFlPerLabMax','_NBsize'],#,'||','_middlename','||','_lastname'], 
        'Fluorescent Protein':['_FPFolder','_FPLabEff','_FP1LabPerLoc','_FP2LabPerLoc','_FPFlPerLabMin','_FPFlPerLabMax','_FPsize'],#,'||','_middlename','||','_lastname']
        },
        '=',
        '_MFilLth','_TrueSpc','_Iter',
          '_BundleSpacing','_BundleNum','_RendRes','||','_checkboxList',
        '=',
        (' ','_button', ' ') ]

    def __buttonAction(self):
        FileCFG='varCFG.py'
        SimRun='LabelingSimulationRun.py'
        #print(self._checkboxList.value)
        """Button action event"""
        #self.saveWindow()
        execfile(FileCFG)
        #print(self._FPFolder, self._NB2LabPerLoc,self._ABLabEff)
        execfile(SimRun)#os.system("python LabelingSimulation.py")#self._fullname.value = self._firstname.value +" "+ self._middlename.value +" "+self._lastname.value
        for katSlf in self._checkboxList.value:
            ExtraRun=katSlf+'Run.py'
            print(ExtraRun)
            execfile(str(ExtraRun))
    
#Execute the application
if __name__ == "__main__":   
    Var = pyforms.startApp( FilamentSimulationGUI )


