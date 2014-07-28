# import ROOT
# from ROOT import gSystem
# gSystem.Load("libSusyFitter.so")
	
# from systematic import Systematic
# from configManager import configMgr

class Systematic:
    def __init__(self, name, nothing, low, high, *whocares):
        self.name = name
        self.range = (low, high)

class CM:
    pass
configMgr = CM()
configMgr.weights = 'blork'

topTheorySRA150 = Systematic("topTheory",configMgr.weights,1.059, 0.941 ,"user","userOverallSys")
topTheorySRA200 = Systematic("topTheory",configMgr.weights,1.108, 0.892 ,"user","userOverallSys")
topTheorySRA250 = Systematic("topTheory",configMgr.weights,1.16, 0.84 ,"user","userOverallSys")
topTheorySRA300 = Systematic("topTheory",configMgr.weights,1.214, 0.786 ,"user","userOverallSys")
topTheorySRA350 = Systematic("topTheory",configMgr.weights,1.269, 0.731 ,"user","userOverallSys")
topTheoryCRA1l = Systematic("topTheory",configMgr.weights,1.021, 0.979 ,"user","userOverallSys")
topTheoryCRA2l = Systematic("topTheory",configMgr.weights,1.057, 0.943 ,"user","userOverallSys")
topTheoryCRAemu = Systematic("topTheory",configMgr.weights,1.0, 1.0,"user","userOverallSys")
topTheoryVRA = Systematic("topTheory",configMgr.weights,1.00, 1.0 ,"user","userOverallSys") # this is the inverted mCT region, mCT<100 GeV
topTheoryVRAmbb = Systematic("topTheory",configMgr.weights,1.04, 0.96 ,"user","userOverallSys") # this is the inverted mbb region, mbb< 200 GeV
topTheoryVRA1b0l = Systematic("topTheory",configMgr.weights,1.0,1.0 ,"user","userOverallSys")
topTheoryVRA1b1l = Systematic("topTheory",configMgr.weights,1.021 ,0.979 ,"user","userOverallSys")
topTheoryVRA1b2l = Systematic("topTheory",configMgr.weights,1.057 ,0.943 ,"user","userOverallSys")
topTheoryVRA1bemu = Systematic("topTheory",configMgr.weights,1.0 ,1.0 ,"user","userOverallSys")

topTheorySRB = Systematic("topTheory",configMgr.weights,0.935, 1.065 ,"user","userOverallSys")
topTheoryCRB1l = Systematic("topTheory",configMgr.weights,1.0, 1.0,"user","userOverallSys")
topTheoryCRB2l = Systematic("topTheory",configMgr.weights,1.095 ,0.905 ,"user","userOverallSys")
topTheoryVRBemu = Systematic("topTheory",configMgr.weights,1.064,0.936,"user","userOverallSys")
topTheoryVRB0L = Systematic("topTheory",configMgr.weights,1.177,0.823,"user","userOverallSys")


#############################
# W
#####

WTheorySRA150 = Systematic("WTheory",configMgr.weights,0.83, 1.093,"user","userOverallSys")
WTheorySRA200 = Systematic("WTheory",configMgr.weights,1.105, 0.778,"user","userOverallSys")
WTheorySRA250 = Systematic("WTheory",configMgr.weights,1.105, 0.778,"user","userOverallSys")
WTheorySRA300 = Systematic("WTheory",configMgr.weights,1.105, 0.778,"user","userOverallSys")
WTheorySRA350 = Systematic("WTheory",configMgr.weights,1.105, 0.778,"user","userOverallSys")
WTheoryCRA1l = Systematic("WTheory",configMgr.weights,1.0,1.0 ,"user","userOverallSys")
#WTheoryCRA2l = Systematic("WTheory",configMgr.weights,1.15 ,0.85 ,"user","userOverallSys")
#WTheoryCRAemu = Systematic("WTheory",configMgr.weights,1.15 ,0.85 ,"user","userOverallSys")
WTheoryVRA = Systematic("WTheory",configMgr.weights,1.0 ,1.0 ,"user","userOverallSys")
WTheoryVRAmbb = Systematic("topTheory",configMgr.weights,1.0,1.0 ,"user","userOverallSys")
WTheoryVRA1b0l = Systematic("WTheory",configMgr.weights,1.0,1.0 ,"user","userOverallSys")
WTheoryVRA1b1l = Systematic("WTheory",configMgr.weights,1.0,1.0 ,"user","userOverallSys")
#WTheoryVRA1b2l = Systematic("WTheory",configMgr.weights,1.709 ,0.475 ,"user","userOverallSys")
#WTheoryVRA1bemu = Systematic("WTheory",configMgr.weights,1.709 ,0.475 ,"user","userOverallSys")

#WTheorySRB = Systematic("WTheory",configMgr.weights,0.957, 1.043,"user","userOverallSys")
#WTheoryCRB1l = Systematic("WTheory",configMgr.weights,1.0, 1.0,"user","userOverallSys")
#WTheoryVRB0L = Systematic("WTheory",configMgr.weights,1.045, 0.955,"user","userOverallSys")

# added 26% HF uncertainty to Will's theory uncertainties
#WTheorySRB = Systematic("WTheory",configMgr.weights,1.762 ,0.479 ,"user","userOverallSys")
WTheorySRB = Systematic("WTheory",configMgr.weights,1.86, 0.344,"user","userOverallSys")
WTheoryCRB1l = Systematic("WTheory",configMgr.weights,1.794, 0.407 ,"user","userOverallSys")
WTheoryVRB0L = Systematic("WTheory",configMgr.weights,1.794, 0.407 ,"user","userOverallSys")


#############################
# Z
#####
ZTheorySRA150 = Systematic("ZTheory",configMgr.weights,0.953, 1.0,"user","userOverallSys")
ZTheorySRA200 = Systematic("ZTheory",configMgr.weights,0.967, 0.984,"user","userOverallSys")
ZTheorySRA250 = Systematic("ZTheory",configMgr.weights,0.965, 0.974,"user","userOverallSys")
ZTheorySRA300 = Systematic("ZTheory",configMgr.weights,0.965, 0.974 ,"user","userOverallSys")
ZTheorySRA350 = Systematic("ZTheory",configMgr.weights,0.965, 0.974 ,"user","userOverallSys")

#ZTheoryCRA1l = Systematic("ZTheory",configMgr.weights,1.01 ,0.99 ,"user","userOverallSys")
ZTheoryCRA2l = Systematic("ZTheory",configMgr.weights,1.0, 1.0 ,"user","userOverallSys")
#ZTheoryCRAemu = Systematic("ZTheory",configMgr.weights,1.01 ,0.99 ,"user","userOverallSys")
ZTheoryVRA = Systematic("ZTheory",configMgr.weights,0.976, 0.972,"user","userOverallSys")
ZTheoryVRAmbb = Systematic("topTheory",configMgr.weights,1.027, 0.953,"user","userOverallSys")
ZTheoryVRA1b0l = Systematic("ZTheory",configMgr.weights,0.976, 0.972,"user","userOverallSys")
#ZTheoryVRA1b1l = Systematic("ZTheory",configMgr.weights,1.557 ,0.668 ,"user","userOverallSys")
ZTheoryVRA1b2l = Systematic("ZTheory",configMgr.weights,1.0, 1.0,"user","userOverallSys")

ZTheorySRB = Systematic("ZTheory",configMgr.weights,1.135, 0.833,"user","userOverallSys")
ZTheoryCRB1l = Systematic("ZTheory",configMgr.weights,1.109, 0.934,"user","userOverallSys")
ZTheoryCRB2l = Systematic("ZTheory",configMgr.weights,1.0, 1.0,"user","userOverallSys")
ZTheoryVRBemu = Systematic("ZTheory",configMgr.weights,1.0,1.0,"user","userOverallSys")
ZTheoryVRB0L = Systematic("ZTheory",configMgr.weights,1.0,1.0,"user","userOverallSys")

def signalISRsyst(m_sbottom,m_LSP):
    deltaM = m_sbottom-m_LSP
    if (deltaM>0) and (deltaM<=10):
        sys = 0.287
    if (deltaM>10) and (deltaM<=30):
        sys = 0.076
    if (deltaM>30) and (deltaM<=50):
        sys = 0.079
    if (deltaM>50):
        sys = 0.112
    return sys
