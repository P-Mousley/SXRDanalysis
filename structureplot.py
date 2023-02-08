# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:12:16 2022

@author: rpy65944
"""

from PyQt5 import QtWidgets, uic
import sys
import pandas as pd
import numpy as np
import os, fnmatch
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#import SXRDplot as sxrdplot
#import SXRDfunction as sfunc
#test adddition


class StructurePlot(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(StructurePlot, self).__init__(*args, **kwargs)
        self.ui = uic.loadUi(r"C:\\Users\\rpy65944\Documents\\GitHub\SXRDanalysis\structuregui.ui", self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        #self.button = QPushButton('Plot')
        self.occval=0
        self.partval=1
        self.parts=[0]

        layout = self.vlayoutModel
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        
 
        self.ax = plt.axes([0,0,0.95,0.95],projection ='3d')
        self.occset=1
        self.dispset=1
        self.indset=1

        # self.fig2 = plt.figure(figsize=(15,35))
        # self.canvas2 = FigureCanvas(self.fig2)
        # self.toolbar2 = NavigationToolbar(self.canvas2, self)
        # layout2 = self.vlayoutCTR
        # layout2.addWidget(self.canvas2)
        # layout2.addWidget(self.toolbar2)
        
        # self.fig3 = plt.figure(figsize=(15,35))
        # self.canvas3 = FigureCanvas(self.fig3)
        # self.toolbar3 = NavigationToolbar(self.canvas3, self)
        # layout3 = self.vlayoutFOR
        # layout3.addWidget(self.canvas3)
        # layout3.addWidget(self.toolbar3)        
        
        self.fig4 = plt.figure(figsize=(15,35))
        self.canvas4 = FigureCanvas(self.fig4)
        self.toolbar4 = NavigationToolbar(self.canvas4, self)
        layout4 = self.vlCTRmod1
        layout4.addWidget(self.canvas4)
        layout4.addWidget(self.toolbar4)

        self.fig5 = plt.figure(figsize=(15,35))
        self.canvas5 = FigureCanvas(self.fig5)
        self.toolbar5 = NavigationToolbar(self.canvas5, self)
        layout5 = self.vlCTRmod2
        layout5.addWidget(self.canvas5)
        layout5.addWidget(self.toolbar5)

        self.fig3dcomp1 = plt.figure(figsize=(15,35))
        self.canvas6 = FigureCanvas(self.fig3dcomp1)
        self.toolbar6 = NavigationToolbar(self.canvas6, self)
        layout6 = self.vlayout3dcomp1
        layout6.addWidget(self.canvas6)
        layout6.addWidget(self.toolbar6)
        self.ax3d1 = plt.axes([0,0,0.95,0.95],projection ='3d')
  

        self.fig3dcomp2 = plt.figure(figsize=(15,35))
        self.canvas7 = FigureCanvas(self.fig3dcomp2)
        self.toolbar7 = NavigationToolbar(self.canvas7, self)
        layout7 = self.vlayout3dcomp2
        layout7.addWidget(self.canvas7)
        layout7.addWidget(self.toolbar7)
        self.ax3d2 = plt.axes([0,0,0.95,0.95],projection ='3d')



        self.fig8 = plt.figure(figsize=(15,35))
        self.canvas8 = FigureCanvas(self.fig8)
        self.toolbar8 = NavigationToolbar(self.canvas8, self)
        layout8 = self.vlFORmod1
        layout8.addWidget(self.canvas8)
        layout8.addWidget(self.toolbar8)

        self.fig9 = plt.figure(figsize=(15,35))
        self.canvas9 = FigureCanvas(self.fig9)
        self.toolbar9 = NavigationToolbar(self.canvas9, self)
        layout9 = self.vlFORmod2
        layout9.addWidget(self.canvas9)
        layout9.addWidget(self.toolbar9)
    
        self.fig10 = plt.figure(figsize=(15,35))
        self.canvas10 = FigureCanvas(self.fig10)
        self.toolbar10 = NavigationToolbar(self.canvas10, self)
        layout10 = self.vlFORmod3
        layout10.addWidget(self.canvas10)
        layout10.addWidget(self.toolbar10)

        self.fig11 = plt.figure(figsize=(15,35))
        self.canvas11 = FigureCanvas(self.fig11)
        self.toolbar11 = NavigationToolbar(self.canvas11, self)
        layout11 = self.vlCTRmod3
        layout11.addWidget(self.canvas11)
        layout11.addWidget(self.toolbar11)

        self.fig3dcomp3 = plt.figure(figsize=(15,35))
        self.canvas12 = FigureCanvas(self.fig3dcomp3)
        self.toolbar12 = NavigationToolbar(self.canvas12, self)
        layout12 = self.vlayout3dcomp3
        layout12.addWidget(self.canvas12)
        layout12.addWidget(self.toolbar12)
        self.ax3d3 = plt.axes([0,0,0.95,0.95],projection ='3d')



        
        self.axs3d=[self.ax3d1,self.ax3d2,self.ax3d3]
        self.canvs3d=[self.canvas6,self.canvas7,self.canvas12]
        #self.fig2=plt.figure(figsize=(10,8))
        self.plotvals=[]
        self.modelinds=[]
        self.modelcount=0
        self.modpvals=[]
        self.boundvals=np.array([[1,2],[1,2],[1,2]])
        self.openfit.clicked.connect(self.openfitfile)
        self.checkbonds.clicked.connect(self.checkbonds1)
        self.plotbutton1.clicked.connect(self.pushplotbutton1)
        self.plotmod1.clicked.connect(self.viewplot1)
        self.plotmod2.clicked.connect(self.viewplot2)
        self.plotmod3.clicked.connect(self.viewplot3)
        self.savemacro.clicked.connect(self.makesavemac)
        self.profmacro.clicked.connect(self.makeprofmac)
        self.openxyz.clicked.connect(self.openxyz1)
        self.plotsavefit.clicked.connect(self.plotsavemodelcompare)
        #self.clearctrs.clicked.connect(self.clearctrs1)
        self.clearmods.clicked.connect(self.clearmods1)
        self.addfit.clicked.connect(self.addfitfile)
        self.addpar.clicked.connect(self.addparfile)
        self.occbutton.clicked.connect(self.updateoccval)
        self.zbutton.clicked.connect(self.updatedispval)
        self.xbutton.clicked.connect(self.updatedispval)
        self.ybutton.clicked.connect(self.updatedispval)
        self.atomindbutton.clicked.connect(self.updateindval)
        self.occspin.valueChanged.connect(self.updateoccval)
        self.atomindex.valueChanged.connect(self.updateindval)
        # self.fitcombo.currentTextChanged.connect(self.pushplotbutton1)
        # self.parcombo.currentTextChanged.connect(self.pushplotbutton1)
        self.zspin.valueChanged.connect(self.updatedispval)
        self.xspin.valueChanged.connect(self.updatedispval)
        self.yspin.valueChanged.connect(self.updatedispval)
        #self.parcheck.toggled.connect(self.pushplotbutton1)
        self.partspin.valueChanged.connect(self.updatepartval)
        self.modlabels=[self.mod1label,self.mod2label,self.mod3label]
        self.modelinfo=[]
    def addfitfile(self):
        """
        add fit file given in textbox to drop down menu fitcombo
        """
        self.fitcombo.addItem(self.text1.toPlainText().strip('""'))
    def addparfile(self):
        """
        add par file given in textbox to drop down menu parcombo
        """
        self.parcombo.addItem(self.par1.toPlainText().strip('""'))
    def openfitfile(self):
        filename=self.text1.toPlainText()
        os.startfile(filename)
    def viewplot1(self):
        """
        switch all figures to plot data from model 1
        """
        currin=self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        if currin==1:
            self.ax3d1.view_init(self.ax3d2.elev,self.ax3d2.azim)
        else:
            self.ax3d1.view_init(self.ax3d3.elev,self.ax3d3.azim)
        self.canvas6.draw()
        if self.plotmaincheck.isChecked()==True:
            try:
                fitn=self.modelinds[0] 
                self.fitcombo.setCurrentIndex(fitn)
                self.parcombo.setCurrentIndex(fitn)
                self.parcheck.setChecked(True)
                par=self.parcombo.currentText()
                fit=self.fitcombo.currentText()
                self.plot3D(par,fit)
            except Exception as e:
                print("The error raised is: ", e)

        # self.canvas4.draw()
        # self.canvas5.draw()



    def viewplot2(self):
        currin=self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)
        if currin==0:
            self.ax3d2.view_init(self.ax3d1.elev,self.ax3d1.azim)
        else:
            self.ax3d2.view_init(self.ax3d3.elev,self.ax3d3.azim)
               
        self.canvas7.draw()
        if self.plotmaincheck.isChecked()==True:
            try:
                fitn=self.modelinds[1] 
                self.fitcombo.setCurrentIndex(fitn)
                self.parcombo.setCurrentIndex(fitn)
                self.parcheck.setChecked(True)
                par=self.parcombo.currentText()
                fit=self.fitcombo.currentText()
                self.plot3D(par,fit)
            except Exception as e:
                print("The error raised is: ", e)



    def viewplot3(self):
        currin=self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(2)
        self.stackedWidget_3.setCurrentIndex(2)
        if currin==0:
            self.ax3d3.view_init(self.ax3d1.elev,self.ax3d1.azim)
        else:
            self.ax3d3.view_init(self.ax3d2.elev,self.ax3d2.azim)
        self.canvas12.draw()

        if self.plotmaincheck.isChecked()==True:
            try:
                fitn=self.modelinds[2] 
                self.fitcombo.setCurrentIndex(fitn)
                self.parcombo.setCurrentIndex(fitn)
                self.parcheck.setChecked(True)
                par=self.parcombo.currentText()
                fit=self.fitcombo.currentText()
                self.plot3D(par,fit)
            except Exception as e:
                print("The error raised is: ", e)
        

    

#     def clearctrs1(self):
#         """
#         check for fig2 existence and clear figure if CTR plot already created
#         """
#         if hasattr(self,'fig2'):
#             self.fig2.clear()
#             self.fig3.clear()
#             plt.draw()
# #        else:
# #            self.fig2=plt.figure(figsize=(10,8))
            
    def clearmods1(self):
        # self.fig2.clear(True)
        # self.fig3.clear(True)
        self.ax.clear()
        self.fig4.clear(True)
        self.fig5.clear(True)
        self.ax3d1.clear()
        self.ax3d2.clear()
        self.fig8.clear(True)
        self.fig9.clear(True)
        self.fig10.clear(True)
        self.fig11.clear(True)
        self.ax3d3.clear()
        self.canvas.draw()
        self.canvas4.draw()
        self.canvas5.draw()
        self.canvas6.draw()
        self.canvas7.draw()
        self.canvas11.draw()
        self.canvas12.draw()
        self.parinfo.setText('Occupancy info:\n')

        self.modelinds=[]
        self.modelcount=0
        for i in np.arange(len(self.modlabels)):
            self.modlabels[i].setText('Model {}: EMPTY'.format(i+1))
        self.fitcombo.clear()
        self.parcombo.clear()
        
    def readfit(self,fitname,workfolder=0,pardata=[0],occdata=0):
    	fitcols=['El','X','x1','x2','x3','x4','Y','y1','y2','y3','y4','Z','z1','z2','z3','z4','dw1','dw2','Occ']#'ind',
    	fitcols2=['ind','El','X','x1','x2','x3','x4','Y','y1','y2','y3','y4','Z','z1','z2','z3','z4','dw1','dw2','Occ']#
    	if len(fitname.split('\\'))==1:
    		openf=r"{}\{}\fit_{}.fit".format(workfolder,fitname,fitname)
    	else:
    		openf=fitname
    	try:
    		fitfile=pd.read_csv(openf,header=1,sep=r'\s+',names=fitcols)
    	except:
    		fitfile=pd.read_csv(openf,header=1,sep=r'\s+',names=fitcols2)
    	
    	if len(pardata)>1:
    		dispdf=pardata[pardata['data'].str.contains('displace')]
    		dispdf[['type','parameter','value','upp','low','fitted']]=dispdf.data.str.split(expand=True)
    		fitfile['newZ']=fitfile.apply(lambda x: float(x['Z'])+float(dispdf[dispdf['parameter']==str(x['z2'])]['value'].values[0]) if x['z2']>0 else float(x['Z']), axis=1)
    		fitfile['newZ']=fitfile.apply(lambda x: float(x['newZ'])+float(dispdf[dispdf['parameter']==str(x['z4'])]['value'].values[0]) if x['z4']>0 else float(x['newZ']), axis=1)
    		fitfile['newX']=fitfile.apply(lambda x: float(x['X'])+float(dispdf[dispdf['parameter']==str(x['x2'])]['value'].values[0]) if x['x2']>0 else float(x['X']), axis=1)
    		fitfile['newX']=fitfile.apply(lambda x: float(x['newX'])+float(dispdf[dispdf['parameter']==str(x['x4'])]['value'].values[0]) if x['x4']>0 else float(x['newX']), axis=1)
    		fitfile['newY']=fitfile.apply(lambda x: float(x['Y'])+float(dispdf[dispdf['parameter']==str(x['y2'])]['value'].values[0]) if x['y2']>0 else float(x['Y']), axis=1)
    		fitfile['newY']=fitfile.apply(lambda x: float(x['newY'])+float(dispdf[dispdf['parameter']==str(x['y4'])]['value'].values[0]) if x['y4']>0 else float(x['newY']), axis=1)
    		occdf=pardata[pardata['data'].str.contains('occupancy')]
    		occdf[['type','parameter','value','upp','low','fitted']]=occdf.data.str.split(expand=True)
    		occdf.reset_index(drop=True)
    		fitfile['occstr']=fitfile.apply(lambda x: occdf[occdf['parameter']==str(x['Occ'])]['value'].values[0] if x['Occ']>0 else 1 , axis=1)
    		fitfile['occval']=fitfile['occstr'].apply(lambda x: float(x))
    	return(fitfile)
        
    def readpar(self,fitname,workfolder=0):
    	if workfolder==0:
    		infodf=pd.read_csv(r"{}".format(fitname),header=1)
    		pardata=pd.read_csv(r"{}".format(fitname),header=5, index_col=False, names=['data'])
    	else:
    		infodf=pd.read_csv(r"{}\{}\par_{}.par".format(workfolder,fitname,fitname),header=1)
    		pardata=pd.read_csv(r"{}\{}\par_{}.par".format(workfolder,fitname,fitname),header=5, index_col=False, names=['data'])
    	occdf=pardata[pardata['data'].str.contains('occupancy')]
    	dispdf=pardata[pardata['data'].str.contains('displace')]
    	dispdf[['type','parameter','value','upp','low','fitted']]=dispdf.data.str.split(expand=True)
    	occdf[['type','parameter','value','upp','low','fitted']]=occdf.data.str.split(expand=True)
    	return(pardata,occdf,dispdf,infodf)
	
    def openxyz1(self):
        """
        opens saved xyz file using entry in fitcombo list and par combolist 
        
        """
        fit=self.fitcombo.currentText()
        splitparts=fit.split('\\')
        workfolder=''
        for i in np.arange(len(splitparts[:-2])):
            workfolder+=splitparts[i]+'\\'
        fitname=splitparts[-2]
        try:
            xyzfile=r"{}\{}\{}.xyz".format(workfolder,fitname,fitname)
            os.startfile(xyzfile)
        except:
            print('no XYZ file found')
    

    
    def updatectrs(self,workfolder,fitname):
        #parf=self.parcombo.currentText()
        #infodf=pd.read_csv(r"{}\{}\par_{}.par".format(workfolder,fitname,fitname),header=1)
        pardata=pd.read_csv(r"{}\{}\par_{}.par".format(workfolder,fitname,fitname),header=1,names=['data'])
        occdf=pardata[pardata['data'].str.contains('occupancy')]
        dispdf=pardata[pardata['data'].str.contains('displace')]
        if len(occdf)>0:
            occdf[['type','parameter','value','upp','low','fitted']]=occdf.data.str.split(expand=True)
        if len(dispdf)>0:
            dispdf[['type','parameter','value','upp','low','fitted']]=dispdf.data.str.split(expand=True)
        #fitcols=['ind','El','X','x1','x2','x3','x4','Y','y1','y2','y3','y4','Z','z1','z2','z3','z4','dw1','dw2','Occ']
        #fitoccdata=pd.read_csv(r"{}\{}\fit_{}.fit".format(workfolder,fitname,fitname),header=1,sep='\s+',names=fitcols)
		
        datdf=pd.read_csv(r"{}\{}\dat_{}.dat".format(workfolder,fitname,fitname),header=1,names=['data'])
        datdf[['h','k','l','F','dF','flag']]=datdf.data.str.split(expand=True)
        datdf['scale']= datdf.apply(lambda x: (x['flag'][0]) ,axis=1)
        scales=pardata[pardata['data'].str.contains('subscale')].reset_index(drop=True)
        scales[['type','parameter','value','upp','low','fitted']]=scales.data.str.split(expand=True)
        plotnorm=float(scales['value'][0])
        scales['plotval']=scales.apply(lambda x: float(x['value'])/plotnorm,axis=1)
        # if hasattr(self,'fig2'):
        #     self.fig2.clear(True)
        #     self.fig3.clear(True)
        #     plt.draw()
        # else:
        #     self.fig2=plt.figure(figsize=(12,18))
        
        lisdf=pd.read_csv('{}\\{}\\comp_{}.lis'.format(workfolder,fitname,fitname),sep=r'\s+',header=1)
        inpl=lisdf.loc[0,'l']
        inpN=len(lisdf[lisdf['l']==inpl])
        mat=[1,0,0,1]
        reclab=1
        log=1
        plotupp=1
        oopdf=lisdf[inpN:]
        ooptable=oopdf.groupby(['h','k']).size().reset_index().rename(columns={0:'count'})
        ooptable['FOR']=0
        ooptable['CTR']=0
        for i in np.arange(len(ooptable)):
            maxval=oopdf[(oopdf['h']==ooptable.loc[i,'h'])&(oopdf['k']==ooptable.loc[i,'k'])]['f-dat'].max()
            if maxval<100:
                ooptable.loc[i,'FOR']=1
            else:
                ooptable.loc[i,'CTR']=1
        oopdf.loc[:,'FOR']=oopdf.apply(lambda x: ooptable[(ooptable['h']==x['h'])&(ooptable['k']==x['k'])].reset_index().loc[0,'FOR'], axis=1)
        ctrdf=oopdf[oopdf['FOR']==0]
        fordf=oopdf[oopdf['FOR']==1]
        # if self.modelcount==0:
        #     self.CTR_plot(ctrdf,1,log,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig)
        #     self.CTR_plot(fordf,1,0,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig3)
        #     self.fig2.set_tight_layout(True)
        #     self.fig3.set_tight_layout(True)
        if self.modelcount<=1:
            self.CTR_plot(ctrdf,1,log,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig4)
            self.CTR_plot(fordf,1,0,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig8)
            self.stackedWidget.setCurrentIndex(0)
            self.stackedWidget_3.setCurrentIndex(0)
            self.fig4.set_tight_layout(True)
            self.fig8.set_tight_layout(True)
            self.canvas4.draw()
            self.canvas8.draw()

        elif self.modelcount==2:
            self.CTR_plot(ctrdf,1,log,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig5)
            self.CTR_plot(fordf,1,0,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig9)
            self.stackedWidget.setCurrentIndex(1)
            self.stackedWidget_3.setCurrentIndex(1)
            self.fig5.set_tight_layout(True)
            self.fig9.set_tight_layout(True)
            self.canvas5.draw()
            self.canvas9.draw()
        elif self.modelcount==3:
            self.CTR_plot(ctrdf,1,log,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig11)
            self.CTR_plot(fordf,1,0,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig10)
            self.stackedWidget.setCurrentIndex(2)
            self.stackedWidget_3.setCurrentIndex(2)
            self.fig11.set_tight_layout(True)
            self.fig10.set_tight_layout(True)
            self.canvas11.draw()
            self.canvas10.draw()

        # else:
        #     oopdf=lisdf
        #     self.CTR_plot(oopdf,1,log,fitname,mat,plotupp,workfolder,reclab,datdf,scales,fig=self.fig2)


    def makesavemac(self):
        """
        creates a new saving macro for ROD and associated folder for directory and fitname given
        """
        directory=self.workfoldertext.toPlainText().strip('""')
        fit=self.fittext.toPlainText().strip('""')
        rodfolder=self.rodfolder.toPlainText().strip('""')
        mypath="{}\\{}".format(directory,fit)
        if not os.path.isdir(mypath):
            
            os.makedirs(mypath)
            f = open(r'{}\savefit.mac'.format(rodfolder), "w")
            f.write("calc data\n")
            f.write("list data {}\\{}\\dat_{} data_file_for_best_fit\n".format(directory,fit,fit))
            f.write("list Smod {}\\{}\\sur_{} surface_model_bestfit\n".format(directory,fit,fit))
            f.write("list Bmod {}\\{}\\bul_{} bulk_model_bestfit\n".format(directory,fit,fit))
            f.write("list Mmod {}\\{}\\mol_{} molecule_model_bestfit\n".format(directory,fit,fit))
            f.write("list para {}\\{}\\par_{} parameters_bestfit\n".format(directory,fit,fit))
            f.write("list fit  {}\\{}\\fit_{} fit_file_bestfit\n".format(directory,fit,fit))
            f.write("list comp {}\\{}\\comp_{} comparison_file_bestfit\n".format(directory,fit,fit))
            f.write("list con {}\\{}\\con_{} comparison_file_bestfit\n".format(directory,fit,fit))
            f.write("plot xyz 2 2 1 {}\\{}\\{} return\n".format(directory,fit,fit))
            f.close()
            self.savemacrolabel.setText('savefit macro created')
    
        else:
            self.savemacrolabel.setText('Folder already exists')
            
    def makeprofmac(self):
        """
        creates a new saving macro for ROD to save full line profile data from scans in a dataset.
        Note that savefit.mac needs to have already been run, and data exists in the specified fit folder
        """
        directory=self.workfoldertext.toPlainText().strip('""')
        fit=self.fittext.toPlainText().strip('""')
        rodfolder=self.rodfolder.toPlainText().strip('""')
        parf='{}\\{}\\par_{}.par'.format(directory,fit,fit)
        parfile=open(r'{}'.format(parf))
        lines=parfile.readlines()
        parfile.close()
        datf=lines[1].strip().split(' ')[-3]
        bulf=lines[1].strip().split(' ')[-2]
        fitf=lines[1].strip().split(' ')[-1]
        datadf=pd.read_csv(datf,sep='\t')
        #comp=pd.read_csv("{}\\{}\\comp_{}.lis".format(directory,fit,fit),sep=r'\s+',header=1)
        f = open(r"{}\savefullprofs.mac".format(rodfolder),"w")
        f.write('re dat {}\n'.format(datf))
        f.write('re bul {}\n'.format(bulf))
        f.write('re fit {}\n'.format(fitf))
        f.write('re par {}\n'.format(parf))
        # f.write('set cal nsurf 28 return return \n')
        # f.write('set cal s2 0.1 return return \n')
        f.write('mac sfsetup\n')
        #f.write('re par limits\n')
        print(datf)
        scans=datadf[datadf['L']>0.2].groupby(['H','K']).size().reset_index().rename(columns={0:'count'})
        for i in np.arange(len(scans)):
            h=int(scans.loc[i,'H'])
            k=int(scans.loc[i,'K'])
            if (h==0) and (k==0):
                f.write('set cal lstart 0 lend 10 return return\n ')
            else:
                f.write('set cal lstart 0 lend 7 return return\n' )
            f.write('cal rod {} {} lis all {}\\{}\\{}_{}_full.dat {}_{}_full\n'.format(h,k,directory,fit,h,k,h,k))
        f.close()
        self.savemacrolabel.setText('profile macro created')

    def plotsavemodelcompare(self):
        workfolder=self.workfoldertext.toPlainText().strip('""')
        fitname=self.fittext.toPlainText().strip('""')
        parf='{}\\{}\\par_{}.par'.format(workfolder,fitname,fitname)
        fitf='{}\\{}\\fit_{}.fit'.format(workfolder,fitname,fitname)
        self.modelcount+=1
        modn=self.modelcount 
        if modn<=3:
        #self.modelinfo[modn]=[parf,fitf]
            self.updatectrs(workfolder,fitname)
            
            self.modlabels[modn-1].setText('Model {}: {}'.format(modn,fitname))
            
            self.plot3Dcomp(parf,fitf,ax=self.axs3d[modn-1],canv=self.canvs3d[modn-1])
            self.stackedWidget_2.setCurrentIndex(modn-1)
            self.stackedWidget.setCurrentIndex(modn-1)
            self.canvs3d[modn-1].draw()
            self.plotsavemodel()
        else:
            print("maximum models reached, clear models and plot again")



    def plotsavemodel(self):
        """
        plot 3D model in main window using fit and par file defined in fit model text boxes
        """
        
        workfolder=self.workfoldertext.toPlainText().strip('""')
        fitname=self.fittext.toPlainText().strip('""')
        parf='{}\\{}\\par_{}.par'.format(workfolder,fitname,fitname)
        self.ptitle='{}\\{}\\fit_{}.fit'.format(workfolder,fitname,fitname)
        #self.parcombo.currentText()
        fitindex=self.fitcombo.findText(self.ptitle)
        parindex=self.parcombo.findText(parf)
        if fitindex<0:
            self.fitcombo.addItem(self.ptitle)
            fitindex=self.fitcombo.findText(self.ptitle)
            self.modelinds.append(fitindex)
            modn=len(self.modelinds)
            self.modlabels[modn-1].setText('Model {}: {}'.format(modn,fitname))
        if parindex<0:
            self.parcombo.addItem(parf)
            parindex=self.parcombo.findText(parf)
        self.parcheck.setChecked(False)    
        self.fitcombo.setCurrentIndex(fitindex)
        self.parcombo.setCurrentIndex(parindex)
        self.parcheck.setChecked(True)
        par=self.parcombo.currentText()
        fit=self.fitcombo.currentText()
        self.plot3D(par,fit)
        splitparts=fit.split('\\')
        workfolder=''
        for i in np.arange(len(splitparts[:-2])):
            workfolder+=splitparts[i]+'\\'
        fitname=splitparts[-2]
        try:
            self.updatectrs(workfolder,fitname)
        except Exception as e:
            print("The error raised is: ", e)
            print('no CTR profiles found')
            #print(workfolder, fitname)

        
        
    def pushplotbutton1(self):
        """
        plot 3D model in main window using fit and par file defined in dropdown boxes (parcombo, fitcombo)
        """
        par=self.parcombo.currentText()
        fit=self.fitcombo.currentText()
        self.plot3D(par,fit)
    
    def plotmodeln(self,n):
        if len(self.modelinds)>=n:
            self.parcheck.setChecked(False)
            fitn=self.modelinds[n-1] 
            self.fitcombo.setCurrentIndex(fitn)
            self.parcombo.setCurrentIndex(fitn)
            par=self.parcombo.currentText()
            fit=self.fitcombo.currentText()
            self.parcheck.setChecked(True)
            self.plot3D(par,fit)
            splitparts=fit.split('\\')
            workfolder=''
            for i in np.arange(len(splitparts[:-2])):
                workfolder+=splitparts[i]+'\\'
            fitname=splitparts[-2]
            try:
                self.updatectrs(workfolder,fitname)
            except:
                print('no CTR profiles found')
        else:
            print('no model {} loaded'.format(n))
        
    def plot3Dcomp(self,par,fit,ax,canv):
        ax.clear()
        parf=par
        self.ptitle=fit
        self.parcheck.setChecked(True)
        if len(self.ptitle)>0:
            self.calcstructure(fit,parfile=parf)
            [x,y,z,cols]=self.plotvals
            ax.scatter3D(x, y, z,c=cols,edgecolors='black',)
            if self.checkfix.isChecked()==False:
                ax.view_init(5,3)
            self.boundbox(ax)

        else:
            print('no fit file loaded')
        self.updateoccval()
        if (len(parf)>0)  & (self.parcheck.isChecked()==True):
             ax.set_title('{}\n{}'.format(fit,par),pad=0)
        else:
             ax.set_title(parf,pad=0)
        canv.draw()
        

    
    def plot3D(self,par,fit):
        self.ax.clear()
        parf=par
        if len(parf)>0:
            pard=self.readpar(parf)
            occs=pard[1][['parameter','value']].reset_index(drop=True)
            totalstring=''
            for i in np.arange(len(occs)):
                totalstring+='{}  {}\n'.format(occs.loc[i,'parameter'],occs.loc[i,'value'])
            self.parinfo.setText('Occupancy info:\n'+totalstring)

        self.ptitle=fit
        if len(self.ptitle)>0:
            self.calcstructure(self.ptitle)
            [x,y,z,cols]=self.plotvals
            self.ax.scatter3D(x, y, z,c=cols,edgecolors='black',)
            if self.checkfix.isChecked()==False:
                self.ax.view_init(5,3)
            self.boundbox(self.ax)


        else:
            print('no fit file loaded')
        self.updateoccval()
        if (len(parf)>0)  & (self.parcheck.isChecked()==True):
             self.ax.set_title('{}\n{}'.format(self.fitcombo.currentText(),self.parcombo.currentText()),pad=0)
        else:
             self.ax.set_title(self.ptitle +' parts= ' + str(len(self.parts)),pad=0)
        self.canvas.draw()
        
    def boundbox(self,ax):
        """
        draw a boundary box on axis to ensure 3D plot is centred on display
        """
        [x,y,z]=self.boundvals
        max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z.max()+z.min())
        # Comment or uncomment following both lines to test the fake bounding box:
        for xb, yb, zb in zip(Xb, Yb, Zb):
            ax.plot([xb], [yb], [zb], 'w')
    def openrf(self,rf):
        readfile=open(r'{}'.format(rf))
        lines=readfile.readlines()
        return(lines)
        
    def getcolour(self,el):
        #colnames=['index','El','atomic r', 'VdW r', 'Ionic R', 'R','G','B']
        #colors=pd.read_csv(r"O:\elements.txt",sep='\s+',names=colnames) 
        if not hasattr(self,'colorlist'):
            indices=[1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
            els=['H', 'D', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'XX']
            atomicr=[0.46, 0.46, 1.22, 1.57, 1.12, 0.81, 0.77, 0.74, 0.74, 0.72, 1.6, 1.91, 1.6, 1.43, 1.18, 1.1, 1.04, 0.99, 1.92, 2.35, 1.97, 1.64, 1.47, 1.35, 1.29, 1.37, 1.26, 1.25, 1.25, 1.28, 1.37, 1.53, 1.22, 1.21, 1.04, 1.14, 1.98, 2.5, 2.15, 1.82, 1.6, 1.47, 1.4, 1.35, 1.34, 1.34, 1.37, 1.44, 1.52, 1.67, 1.58, 1.41, 1.37, 1.33, 2.18, 2.72, 2.24, 1.88, 1.82, 1.82, 1.82, 1.81, 1.81, 2.06, 1.79, 1.77, 1.77, 1.76, 1.75, 1.0, 1.94, 1.72, 1.59, 1.47, 1.41, 1.37, 1.35, 1.36, 1.39, 1.44, 1.55, 1.71, 1.75, 1.82, 1.77, 0.62, 0.8, 1.0, 2.35, 2.03, 1.8, 1.63, 1.56, 1.56, 1.64, 1.73, 0.8]
            vdw=[1.2, 1.2, 1.4, 1.4, 1.4, 1.4, 1.7, 1.55, 1.52, 1.47, 1.54, 1.54, 1.54, 1.54, 2.1, 1.8, 1.8, 1.75, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.85, 1.9, 1.85, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.02, 2.0, 2.06, 1.98, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 1.0]
            ionicr=[0.2, 0.2, 1.22, 0.59, 0.27, 0.11, 0.15, 1.46, 1.4, 1.33, 1.6, 1.02, 0.72, 0.39, 0.26, 0.17, 1.84, 1.81, 1.92, 1.51, 1.12, 0.745, 0.605, 0.58, 0.615, 0.83, 0.78, 0.745, 0.69, 0.73, 0.74, 0.62, 0.53, 0.335, 1.98, 1.96, 1.98, 1.61, 1.26, 1.019, 0.72, 0.64, 0.59, 0.56, 0.62, 0.665, 0.86, 1.15, 0.95, 0.8, 0.69, 0.76, 2.21, 2.2, 0.48, 1.74, 1.42, 1.16, 0.97, 1.126, 1.109, 1.093, 1.27, 1.066, 1.053, 1.04, 1.027, 1.015, 1.004, 0.994, 0.985, 0.977, 0.71, 0.64, 0.6, 0.53, 0.63, 0.625, 0.625, 1.37, 1.02, 0.885, 1.19, 1.03, 0.94, 0.62, 0.8, 1.8, 1.48, 1.12, 1.05, 0.78, 0.73, 0.75, 0.86, 0.975, 0.8]
            red=[1.0, 0.8, 0.98907, 0.52731, 0.37147, 0.1249, 0.5043, 0.69139, 0.99997, 0.69139, 0.99954, 0.97955, 0.98773, 0.50718, 0.10596, 0.75557, 1.0, 0.19583, 0.81349, 0.63255, 0.35642, 0.71209, 0.47237, 0.9, 0.0, 0.66148, 0.71051, 0.0, 0.72032, 0.1339, 0.56123, 0.62292, 0.49557, 0.45814, 0.6042, 0.49645, 0.98102, 1.0, 0.0, 0.40259, 0.0, 0.29992, 0.70584, 0.80574, 0.81184, 0.80748, 0.75978, 0.72032, 0.95145, 0.84378, 0.60764, 0.84627, 0.67958, 0.55914, 0.60662, 0.05872, 0.11835, 0.3534, 0.82055, 0.9913, 0.98701, 0.0, 0.99042, 0.98367, 0.75325, 0.44315, 0.1939, 0.02837, 0.28688, 0.0, 0.15323, 0.15097, 0.70704, 0.71952, 0.55616, 0.70294, 0.78703, 0.78975, 0.79997, 0.99628, 0.8294, 0.58798, 0.32386, 0.82428, 0.0, 0.0, 1.0, 0.0, 0.42959, 0.39344, 0.14893, 0.16101, 0.47774, 0.3, 0.3, 0.3, 0.3]
            green=[0.8, 0.8, 0.91312, 0.87953, 0.8459, 0.63612, 0.28659, 0.72934, 0.01328, 0.72934, 0.21788, 0.86618, 0.48452, 0.70056, 0.23226, 0.61256, 0.98071, 0.98828, 0.99731, 0.13281, 0.58863, 0.3893, 0.79393, 0.1, 0.0, 0.03412, 0.44662, 0.0, 0.73631, 0.28022, 0.56445, 0.89293, 0.43499, 0.81694, 0.93874, 0.19333, 0.75805, 0.0, 1.0, 0.59739, 1.0, 0.70007, 0.52602, 0.68699, 0.72113, 0.82205, 0.76818, 0.73631, 0.12102, 0.50401, 0.56052, 0.51498, 0.63586, 0.122, 0.63218, 0.99922, 0.93959, 0.77057, 0.99071, 0.88559, 0.5556, 0.0, 0.02403, 0.03078, 0.01445, 0.01663, 0.02374, 0.25876, 0.45071, 0.0, 0.99165, 0.99391, 0.70552, 0.60694, 0.54257, 0.69401, 0.69512, 0.81033, 0.77511, 0.70149, 0.72125, 0.53854, 0.32592, 0.18732, 0.0, 0.0, 1.0, 0.0, 0.66659, 0.62101, 0.99596, 0.98387, 0.63362, 0.3, 0.3, 0.3, 0.3]
            blue=[0.8, 1.0, 0.81091, 0.4567, 0.48292, 0.05948, 0.16236, 0.9028, 0.0, 0.9028, 0.71035, 0.23787, 0.0847, 0.84062, 0.98096, 0.76425, 0.0, 0.01167, 0.77075, 0.96858, 0.74498, 0.67279, 1.0, 0.0, 0.62, 0.62036, 0.00136, 0.68666, 0.74339, 0.86606, 0.50799, 0.45486, 0.65193, 0.34249, 0.06122, 0.01076, 0.95413, 0.6, 0.15259, 0.55813, 0.0, 0.46459, 0.68925, 0.79478, 0.68089, 0.67068, 0.72454, 0.74339, 0.86354, 0.73483, 0.72926, 0.31315, 0.32038, 0.54453, 0.97305, 0.72578, 0.17565, 0.28737, 0.02374, 0.02315, 0.02744, 0.96, 0.49195, 0.83615, 1.0, 0.99782, 0.99071, 0.98608, 0.23043, 0.88, 0.95836, 0.71032, 0.3509, 0.33841, 0.50178, 0.55789, 0.47379, 0.45049, 0.75068, 0.22106, 0.79823, 0.42649, 0.35729, 0.97211, 1.0, 1.0, 0.0, 0.0, 0.34786, 0.45034, 0.47106, 0.20855, 0.66714, 0.3, 0.3, 0.3, 0.3]
            
            data={'index':indices,'El':els,'atomic r':atomicr,'VdW r':vdw,'Ionic R':ionicr,'R':red,'G':green,'B':blue}
            self.colorlist=pd.DataFrame(data)
        
        colors=self.colorlist
        plotcol=colors[colors['El']==el]
        colR=plotcol.values[0][5]
        colG=plotcol.values[0][6]
        colB=plotcol.values[0][7]
        col=(colR,colG,colB)
        return(col)
        
    def calcvec(self,p1,p2):
        sqvec=np.square(p1[0]-p2[0])+np.square(p1[1]-p2[1])+np.square(p1[2]-p2[2])
        vec=np.sqrt(sqvec)
        return(vec)
        
    def checkbonds1(self):
        """
        check bond lengths to nearest atoms neighbouring atom with chosen index
        """
        if self.atomindex.value()>0:
            ind=self.atomindex.value()-1
            if (self.parcheck.isChecked()==True):
                self.model['xang']=self.model['newX']*self.lattice[0]
                self.model['yang']=self.model['newY']*self.lattice[1]
                self.model['zang']=self.model['newZ']*self.lattice[2]
            else:
                self.model['xang']=self.model['X']*self.lattice[0]
                self.model['yang']=self.model['Y']*self.lattice[1]
                self.model['zang']=self.model['Z']*self.lattice[2]
            self.model2=self.model.copy(deep=True)
            self.model3=self.model.copy(deep=True)
            self.model4=self.model.copy(deep=True)
            self.model2['xang']=self.model['xang']+self.lattice[0]
            self.model3['yang']=self.model['yang']+self.lattice[1]
            self.model4['xang']=self.model['xang']+self.lattice[0]
            self.model4['yang']=self.model['yang']+self.lattice[1]
            self.modelfull=self.model.append([self.model2,self.model3,self.model4]).reset_index(drop=True)
            
            con1=abs(self.modelfull['xang']-self.modelfull.loc[ind+3*len(self.model),'xang'])<3
            con2= abs(self.modelfull['yang']-self.modelfull.loc[ind+3*len(self.model),'yang'])<3
            con3=abs(self.modelfull['zang']-self.modelfull.loc[ind+3*len(self.model),'zang'])<3
            con4=abs(self.modelfull['zang']-self.modelfull.loc[ind+3*len(self.model),'zang'])>0
            nearest=self.modelfull[(con1&con2&con3&con4)].reset_index(drop=True)
            nearest['bondlength(Å)']=0
            for n in np.arange(len(nearest)):
                p1=self.modelfull.loc[ind+3*len(self.model),['xang','yang','zang']]
                p2=nearest.loc[n,['xang','yang','zang']]
                nearest.loc[n,'bondlength(Å)']=self.calcvec(p1,p2)
            newnear=nearest.sort_values(by='bondlength(Å)')
            print(newnear[['index','El','bondlength(Å)']])
        
    def calcstructure(self,file,parfile=0):
        """
        calculate structure from a given fit file
        """
        if parfile==0:
            parf=self.parcombo.currentText()
        else:
            parf=parfile
        if (len(parf)>0)&(self.parcheck.isChecked()):
            pard=self.readpar(parf)
            model1=self.readfit(file,pardata=pard[0])
        else:
            model1=self.readfit(file)
        
        model1=model1.reset_index()
        parts=[0]
        for i in np.arange(len(model1))[1:]:
            if (i>=1) &(model1.loc[i]['Z']>model1.loc[i-1]['Z']):
                parts.append(i)
        parts.append(len(model1))
        self.parts=parts
        if len(parts)==1:
            model=model1
            self.model=model
        if len(parts)>15:
            model=model1
            self.model=model
        else:
            model=model1[parts[self.partval-1]:parts[self.partval]].reset_index()
            self.model=model
        textlat=self.openrf(file)[1].split()
        lattice=[float(i) for i in textlat]
        self.lattice=lattice
        a1=[lattice[0],0,0]
        if lattice[5]>90:
            b1=[-lattice[1]*np.cos(np.radians(180-lattice[5])),lattice[1]*np.sin(np.radians(180-lattice[5])),0]
        else:
            b1=[lattice[1]*np.cos(np.radians(lattice[5])),lattice[1]*np.sin(np.radians(lattice[5])),0]
        c1=[0,0,(lattice[2])]
        model['color']=model.apply(lambda x: self.getcolour(x['El']),axis=1)
        cols1=model['color']
        self.vectors=[a1,b1,c1]


        if (len(parf)>0)  & (self.parcheck.isChecked()==True):
            x1=model['newX']*a1[0] + model['newY']*b1[0]
            y1=model['newX']*a1[1] + model['newY']*b1[1]
            z1=model['newZ']*lattice[2]
        else:
            x1=model['X']*a1[0] + model['Y']*b1[0]
            y1=model['X']*a1[1] + model['Y']*b1[1]
            z1=model['Z']*lattice[2]
        
        x=x1.append(x1+a1[0])
        y=y1.append(y1+a1[1])
        z=z1.append(z1)
        cols=cols1.append(cols1)

        x=x.append(x1+b1[0])
        y=y.append(y1+b1[1])
        z=z.append(z1)
        cols=cols.append(cols1)

        x=x.append(x1+a1[0]+b1[0])
        y=y.append(y1+a1[1]+b1[1])
        z=z.append(z1)
        cols=cols.append(cols1)
        xb=model['X']*a1[0] + model['Y']*b1[0]
        yb=model['X']*a1[1] + model['Y']*b1[1]
        zb=model['Z']*lattice[2]
        if (xb.max()>self.boundvals[0].max()):
            self.boundvals=[xb,yb,zb]
        elif (yb.max()>self.boundvals[1].max()):
            self.boundvals=[xb,yb,zb]
        elif (zb.max()>self.boundvals[2].max()):
            self.boundvals=[xb,yb,zb]
        self.plotvals=[x,y,z,cols]
        
    def updatepartval(self):
        """
        updates surface part value and redraws 3D plot
        """
        self.partval=self.partspin.value()
        self.pushplotbutton1()
        
        
    def updateoccval(self):
        """
        updates occupancy value and redraws 3D plot
        """
        self.occval=self.occspin.value()
        if self.dispset!=1:
            self.dispset.remove()
            self.dispset=1
        if self.occset!=1:
            self.occset.remove()
            self.occset=1
        if self.indset!=1:
            self.indset.remove()
            self.indset=1
        self.plotoccatoms()
        self.canvas.draw()
    def updateindval(self):
        """
        updates index value and redraws 3D plot
        """
        self.indval=self.atomindex.value()
        if self.indset!=1:
            self.indset.remove()
            self.indset=1
        if self.occset!=1:
            self.occset.remove()
            self.occset=1
        if self.dispset!=1:
            self.dispset.remove()
            self.dispset=1
        self.plotindex()
        self.canvas.draw()
        
    def plotindex(self):
        """
        plots selected atoms with chosen index
        """
        if self.atomindbutton.isChecked()&(self.indval>0):
            indatoms=self.model[self.model['index']==self.indval]
            lattice=self.lattice
            [a1,b1,c1]=self.vectors
            
            if (len(self.par1.toPlainText())>0) & (self.parcheck.isChecked()):
                indx1=indatoms['newX']*a1[0] + indatoms['newY']*b1[0]
                indy1=indatoms['newX']*a1[1] + indatoms['newY']*b1[1]
                indz1=indatoms['newZ']*lattice[2]
            else:
                indx1=indatoms['X']*a1[0] + indatoms['Y']*b1[0]
                indy1=indatoms['X']*a1[1] + indatoms['Y']*b1[1]
                indz1=indatoms['Z']*lattice[2]
                
            indxfull=indx1.append(indx1+a1[0])
            indyfull=indy1.append(indy1+a1[1])
            indzfull=indz1.append(indz1)
            
            indxfull=indxfull.append(indx1+b1[0])
            indyfull=indyfull.append(indy1+b1[1])
            indzfull=indzfull.append(indz1)
            
            indxfull=indxfull.append(indx1+a1[0]+b1[0])
            indyfull=indyfull.append(indy1+a1[1]+b1[1])
            indzfull=indzfull.append(indz1)
            
            indx=[float(i) for i in indxfull]
            indy=[float(i) for i in indyfull]
            indz=[float(i) for i in indzfull]
            indcol=self.occhigh.toPlainText()
            self.indset=self.ax.scatter3D(indx, indy, indz,c=indcol,edgecolors='black',alpha=1,s=100)
            if self.occset!=1:
                self.occset.remove()
                self.occset=1
            if self.dispset!=1:
                self.dispset.remove()
                self.dispset=1
    
            self.canvas.draw()
    
    def plotoccatoms(self):
        """
        plots selected atoms with chosen occupancy parameter
        """
        if self.occbutton.isChecked():
            occatoms=self.model[self.model['Occ']==self.occval]
            lattice=self.lattice
            [a1,b1,c1]=self.vectors
            
            if (len(self.par1.toPlainText())>0) & (self.parcheck.isChecked()):
                occx1=occatoms['newX']*a1[0] + occatoms['newY']*b1[0]
                occy1=occatoms['newX']*a1[1] + occatoms['newY']*b1[1]
                occz1=occatoms['newZ']*lattice[2]
            else:
                occx1=occatoms['X']*a1[0] + occatoms['Y']*b1[0]
                occy1=occatoms['X']*a1[1] + occatoms['Y']*b1[1]
                occz1=occatoms['Z']*lattice[2]
            
            occxfull=occx1.append(occx1+a1[0])
            occyfull=occy1.append(occy1+a1[1])
            occzfull=occz1.append(occz1)
            
            occxfull=occxfull.append(occx1+b1[0])
            occyfull=occyfull.append(occy1+b1[1])
            occzfull=occzfull.append(occz1)
            
            occxfull=occxfull.append(occx1+a1[0]+b1[0])
            occyfull=occyfull.append(occy1+a1[1]+b1[1])
            occzfull=occzfull.append(occz1)
            
            occx=[float(i) for i in occxfull]
            occy=[float(i) for i in occyfull]
            occz=[float(i) for i in occzfull]
            occcol=self.occhigh.toPlainText()
            self.occset=self.ax.scatter3D(occx, occy, occz,c=occcol,edgecolors='black',alpha=1,s=100)
            self.canvas.draw()
            
        else:
            if self.occset!=1:
                self.occset.remove()
                self.occset=1
            if self.dispset!=1:
                self.dispset.remove()
                self.dispset=1
            if self.indset!=1:
                self.indset.remove()
                self.indset=1
    
            self.canvas.draw()
    def updatedispval(self):
        """
        update value for displacement parameter chosen in either x,y or z
        """
        if self.zbutton.isChecked():
            value=self.zspin.value()
        elif self.xbutton.isChecked():
            value=self.xspin.value()
        elif self.ybutton.isChecked():
            value=self.yspin.value()
        if self.indset!=1:
            self.indset.remove()
            self.indset=1
        
        if self.occset!=1:
            self.occset.remove()
            self.occset=1
        self.dispval=value
        if self.dispset!=1:
            self.dispset.remove()
            self.dispset=1
        self.plotdispatoms()
        self.canvas.draw()
    def plotdispatoms(self):
        """
        plots selected atoms with chosen displacement parameter
        """
        if self.zbutton.isChecked():
            dispatoms=self.model[(self.model['z2']==self.dispval) |(self.model['z4']==self.dispval)]
            
        elif self.xbutton.isChecked():
            dispatoms=self.model[(self.model['x2']==self.dispval) |(self.model['x4']==self.dispval)]
        elif self.ybutton.isChecked():
            dispatoms=self.model[(self.model['y2']==self.dispval) |(self.model['y4']==self.dispval)]
        else:
            if self.dispset!=1:
                self.dispset.remove()
                self.dispset=1
            self.canvas.draw()
        lattice=self.lattice
        [a1,b1,c1]=self.vectors     
        if (len(self.par1.toPlainText())>0) & (self.parcheck.isChecked()):
            dispx1=dispatoms['newX']*a1[0] + dispatoms['newY']*b1[0]
            dispy1=dispatoms['newX']*a1[1] + dispatoms['newY']*b1[1]
            dispz1=dispatoms['newZ']*lattice[2]
        else:
            dispx1=dispatoms['X']*a1[0] + dispatoms['Y']*b1[0]
            dispy1=dispatoms['X']*a1[1] + dispatoms['Y']*b1[1]
            dispz1=dispatoms['Z']*lattice[2]
        
        dispxfull=dispx1.append(dispx1+a1[0])
        dispyfull=dispy1.append(dispy1+a1[1])
        dispzfull=dispz1.append(dispz1)
        
        dispxfull=dispxfull.append(dispx1+b1[0])
        dispyfull=dispyfull.append(dispy1+b1[1])
        dispzfull=dispzfull.append(dispz1)
        
        dispxfull=dispxfull.append(dispx1+a1[0]+b1[0])
        dispyfull=dispyfull.append(dispy1+a1[1]+b1[1])
        dispzfull=dispzfull.append(dispz1)
        
        dispx=[float(i) for i in dispxfull]
        dispy=[float(i) for i in dispyfull]
        dispz=[float(i) for i in dispzfull]
        Zcol=self.occhigh.toPlainText()
        self.dispset=self.ax.scatter3D(dispx, dispy, dispz,c=Zcol,edgecolors='black',alpha=1,s=100)
        self.canvas.draw()

    def CTR_plot(self,df,model,log,fit,mat,plotupp,wf,reclab,datdf,scales,fig):
    		ooptable=df.groupby(['h','k']).size().reset_index().rename(columns={0:'count'})
    		CTRnum=len(ooptable)
    		rowcalc=lambda x: (x[0]//x[1])+1 if x[0]%x[1]>0 else (x[0]//x[1])
    		rowvals=[CTRnum,3]
    		rows=rowcalc(rowvals)
    		#fig=plt.figure(figsize=(20,30))		#figs[1]#		
    		datdf['fh']=datdf.apply(lambda x: float(x['h']),axis=1)
    		datdf['fk']=datdf.apply(lambda x: float(x['k']),axis=1)
    		datdf['fl']=datdf.apply(lambda x: float(x['l']),axis=1)
    		#plt.title('{}'.format(fit),y=1.08)
    		for i in np.arange(len(ooptable)):
    			ax=fig.add_subplot(rows,3,1+i)
    			hval=round(ooptable.iloc[i]['h'])
    			kval=round(ooptable.iloc[i]['k'])
    			
    			x=df[(df['h']==hval) & (df['k']==kval)]['l']
    			if model==1:
    				calcdf=pd.read_csv("{}\\{}\\{}_{}_full.dat".format(wf,fit,str(hval),str(kval)),header=1,sep=r'\s+')
    				xcalc=calcdf['l']
    				ycalc=calcdf['f-sum']
    				ybul=calcdf['f-bulk']
    				ydat = df[(df['h']==hval) & (df['k']==kval)]['f-dat']
    				#ycalc = df[(df['h']==hval) & (df['k']==kval)]['f-th']
    				errors=df[(df['h']==hval) & (df['k']==kval)]['sigma']
    				con1=(datdf['fh']==hval)
    				con2=(datdf['fk']==kval)
    				yscale=scales[scales['parameter']==datdf[con1&con2].reset_index(drop=True)['scale'][1]]['plotval'].values[0]
    				#if not((hval==0)&(kval==0)):
    				ycalc=ycalc*yscale#
    					#ycalc=ycalc 
    				ax.errorbar(x,ydat,yerr=errors,color='black',linestyle='', marker='',markersize=5,label='data',zorder=1)
    				if log==1:
    					ax.semilogy(xcalc,ycalc,color='r',linestyle='-', marker='', label='model',zorder=2)
    					#ax.semilogy(xcalc,ybul,color='blue',linestyle='--', marker='', label='bulk',zorder=2)
    				else:
    					ax.plot(xcalc,ycalc,color='r',linestyle='-', marker='', label='model',zorder=2)
    					#ax.plot(xcalc,ybul,color='blue',linestyle='--', marker='', label='bulk',zorder=2)
    	
    				#ax.plot(x,ycalc,color='r',linestyle='-', marker='', label='model',zorder=2)			
    				
    				
    			else:
    				ydat = df[(df['h']==hval) & (df['k']==kval)]['F']
    				yerr=df[(df['h']==hval) & (df['k']==kval)]['dF']
    				ax.errorbar(x,ydat,yerr,color='black',linestyle=' ', marker='o',markersize=5,label='data')
    				
    			if reclab==1:
    				hvalrev,kvalrev=hval,kval
    			else:
    				hrev,krev=self.calcreverseab(mat,hval,kval)
    				hvalrev=round(hrev)
    				kvalrev=round(krev)
    			if i==0:
    				ax.set_title('{}\n[{}  {} L]'.format(fit,str(round(hvalrev,5)),str(round(kvalrev,5))))
    				ax.legend()
    			else:
    				
    				ax.set_title('[{}  {}  L]'.format(str(round(hvalrev,5)),str(round(kvalrev,5))))
    			#ax.xlabel('L')
    			ax.set_ylim(2,6e3)
    			ax.set_xlim(0,x.max()+0.25)
    			if log==1:
    				ax.set_yscale('log')
    			else:
    				ax.set_yscale('linear')
    			#print(ydat.max(),'\n',hval,kval,plotupp)
    			if ydat.max()<101:
    				ax.set_ylim(1,5.5)
    			#fig.tight_layout()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = StructurePlot()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()