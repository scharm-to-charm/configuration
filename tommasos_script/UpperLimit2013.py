################################################################
## In principle all you have to setup is defined in this file ##
################################################################
from configManager import configMgr
from configWriter import TopLevelXML,Measurement,ChannelXML,Sample
from systematic import Systematic
from math import sqrt
from optparse import OptionParser

# Setup for ATLAS plotting
from ROOT import gROOT
import ROOT
import os, sys

##########################

ndata = float(os.environ['NDATA'])
nbkg = float(os.environ['NBKGD'])
bkgerr = float(os.environ['BGERR'])
nbkgUp=1+bkgerr/nbkg
nbkgDo=1-bkgerr/nbkg

nsig      =  1.         # Number of predicted signal events
lumiError = 0.028       # Relative luminosity uncertainty

# Set uncorrelated systematics for bkg and signal (1 +- relative uncertainties)
ucb = Systematic("uncorrl_bkg", configMgr.weights, nbkgUp, nbkgDo, "user","userOverallSys")  # 20% error up and down
# correlated systematic between background and signal (1 +- relative uncertainties)

##########################

# Setting the parameters of the hypothesis test
configMgr.nTOYs=1000
configMgr.calculatorType=0 # 2=asymptotic calculator, 0=frequentist calculator
configMgr.testStatType=3   # 3=one-sided profile likelihood test statistic (LHC default)
configMgr.nPoints=20       # number of values scanned of signal-strength for upper-limit determination of signal strength.
#configMgr.blindSR = True
##########################

# Give the analysis a name
configMgr.analysisName = "UpperLimitScharm%s" % os.environ['REGION']
configMgr.outputFileName = "results/%s_Output.root"%configMgr.analysisName

# Define cuts
configMgr.cutsDict["UserRegion"] = "1."

# Define weights
configMgr.weights = "1."

# Define samples
bkgSample = Sample("Bkg",0)
bkgSample.setStatConfig(True)
bkgSample.buildHisto([nbkg],"UserRegion","BDTG")


bkgSample.addSystematic(ucb)
sigSample = Sample("Sig",0)
sigSample.setNormFactor("mu_Sig",1.,0.,30.)

#sigSample.setStatConfig(True)
sigSample.setNormByTheory()
sigSample.buildHisto([nsig],"UserRegion","BDTG")


dataSample = Sample("Data",0)
dataSample.setData()
dataSample.buildHisto([ndata],"UserRegion","BDTG")

# Define top-level
ana = configMgr.addTopLevelXML("SPlusB")
ana.addSamples([bkgSample,sigSample,dataSample])
ana.setSignalSample(sigSample)

# Define measurement
meas = ana.addMeasurement(name="NormalMeasurement",lumi=1.0,lumiErr=lumiError)
meas.addPOI("mu_Sig")
meas.addParamSetting("Lumi",True)

# Add the channel
chan = ana.addChannel("BDTG",["UserRegion"],1,0.,1.)
ana.setSignalChannels([chan])

# These lines are needed for the user analysis to run
# Make sure file is re-made when executing HistFactory
if configMgr.executeHistFactory:
    if os.path.isfile("data/%s.root"%configMgr.analysisName):
        os.remove("data/%s.root"%configMgr.analysisName) 

