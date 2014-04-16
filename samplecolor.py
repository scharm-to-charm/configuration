#!/usr/bin/env python2.7
"""Based on Will's helperfunctons.py, get the colors associated with samples"""
import ROOT
from ROOT import TColor
import sys, argparse

def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('samples', nargs="*")
    parser.add_argument('-d', '--isdan', action='store_true')
    args = parser.parse_args(sys.argv[1:])
    samples = args.samples
    for sample in samples:
        printRGB(sample, args.isdan)

    # allow piping
    if len(samples) == 0 and not sys.stdin.isatty():
        for line in sys.stdin:
            printRGB(line.strip(), args.isdan)

def getColour(name, isDan = False):

    name = name.replace('+','')
    if 'scharm' in name or 'stop' in name:
        try: int(name.split('_')[-1])
        except: name = name.split('_')[-1]+'_'+'_'.join(name.split('_')[:-1])

    if not isDan:

        if 'QCD' == name: return ROOT.kOrange+2
        if 'ttbarV' == name: return ROOT.kGreen+3
        if 'Other' == name: return ROOT.kOrange+2

        if 'diboson' == name: return ROOT.kBlue-6
        if 'nunuqq' == name: return ROOT.kGreen
        if 'lnu' == name: return ROOT.kBlue
        if 'llqq' == name: return ROOT.kRed
        if 'lnuqq' == name: return ROOT.kBlue+4

        if 'singleTop'==name or 'singletop'== name: return ROOT.kGreen-2
        if 'ttbar' == name: return ROOT.kGreen
        if 'Top' == name: return ROOT.kGreen

        if 'WjetsB' == name: return ROOT.kBlue-3
        if 'WjetsC' == name: return ROOT.kBlue-2
        if 'WjetsL' == name: return ROOT.kBlue-1
        if 'Wjets' == name: return ROOT.kBlue-3

        if 'ZjetsB' == name: return ROOT.kBlue+3
        if 'ZjetsC' == name: return ROOT.kBlue+2
        if 'ZjetsL' == name: return ROOT.kBlue+1
        if 'Zjets' == name: return ROOT.kBlue+3

        if 'ZjetsB_ee' == name: return ROOT.kBlue+3
        if 'ZjetsB_mm' == name: return ROOT.kBlue+2
        if 'ZjetsB_tt' == name: return ROOT.kBlue+1
        if 'ZjetsB_nn' == name: return ROOT.kBlue

        if 'scharm_200_1' == name: return ROOT.kRed
        if 'scharm_200_75' == name: return ROOT.kRed
        if 'scharm_300_1' == name: return ROOT.kMagenta
        if 'scharm_300_100' == name: return ROOT.kCyan+2
        if 'scharm_300_200' == name: return ROOT.kRed
        if 'scharm_400_1' == name: return ROOT.kCyan
        if 'scharm_400_100' == name: return ROOT.kMagenta
        if 'scharm_400_200' == name: return ROOT.kMagenta+3
        if 'scharm_400_300' == name: return ROOT.kMagenta+3
        if 'scharm_500_1' == name: return ROOT.kOrange-3
        if 'scharm_500_100' == name: return ROOT.kOrange-3
        if 'scharm_500_200' == name: return ROOT.kCyan
        if 'scharm_500_300' == name: return ROOT.kCyan
        if 'scharm_500_400' == name: return ROOT.kMagenta+3
        if 'scharm_500_450' == name: return ROOT.kMagenta+3
        if 'scharm_600_1' == name: return ROOT.kGreen
        if 'scharm_600_100' == name: return ROOT.kOrange-3
        if 'scharm_600_200' == name: return ROOT.kBlue
        if 'scharm_600_300' == name: return ROOT.kMagenta+3
        if 'scharm_600_400' == name: return ROOT.kMagenta+3
        if 'scharm_600_500' == name: return ROOT.kMagenta+3
        if 'scharm_700_1' == name: return ROOT.kGreen
        if 'scharm_700_100' == name: return ROOT.kOrange-3
        if 'scharm_700_200' == name: return ROOT.kBlue
        if 'scharm_700_300' == name: return ROOT.kMagenta+3
        if 'scharm_700_400' == name: return ROOT.kMagenta+3
        if 'scharm_700_500' == name: return ROOT.kMagenta+3

        if 'stop_100_70' == name: return ROOT.kSpring
        if 'stop_150_75' == name: return ROOT.kOrange+3
        if 'stop_175_100' == name: return ROOT.kOrange+3
        if 'stop_200_125' == name: return ROOT.kBlue
        if 'stop_250_175' == name: return ROOT.kGreen
        if 'stop_300_240' == name: return ROOT.kPink
        if 'stop_350_300' == name: return ROOT.kPink-5
        if 'stop_400_350' == name: return ROOT.kYellow

        print "ERROR:", name, "not recognised"


    else:

        if 'QCD' == name: return ROOT.kCyan+1
        if 'ttbarV' == name: return ROOT.kRed+3
        if 'Other' == name: return ROOT.kOrange+2

        if 'diboson' == name: return ROOT.kMagenta-10
        if 'nunuqq' == name: return ROOT.kGreen
        if 'lnu' == name: return ROOT.kBlue
        if 'llqq' == name: return ROOT.kRed
        if 'lnuqq' == name: return ROOT.kBlue+4

        if 'singleTop'==name or 'singletop'== name: return ROOT.kCyan+3
        if 'ttbar' == name: return ROOT.kBlue
        if 'Top' == name: return ROOT.kGreen

        if 'WjetsB' == name: return ROOT.kRed
        if 'WjetsC' == name: return ROOT.kYellow
        if 'WjetsL' == name: return ROOT.kMagenta+3
        if 'Wjets' == name: return ROOT.kBlue-3

        if 'ZjetsB' == name: return ROOT.kOrange-3
        if 'ZjetsC' == name: return ROOT.kGreen+3
        if 'ZjetsL' == name: return ROOT.kMagenta+2
        if 'Zjets' == name: return ROOT.kBlue+3

        if 'ZjetsB_ee' == name: return ROOT.kBlue+3
        if 'ZjetsB_mm' == name: return ROOT.kBlue+2
        if 'ZjetsB_tt' == name: return ROOT.kBlue+1
        if 'ZjetsB_nn' == name: return ROOT.kBlue

        if 'scharm_200_1' == name: return ROOT.kRed
        if 'scharm_200_75' == name: return ROOT.kRed
        if 'scharm_300_1' == name: return ROOT.kMagenta
        if 'scharm_300_100' == name: return ROOT.kCyan+2
        if 'scharm_300_200' == name: return ROOT.kRed
        if 'scharm_400_1' == name: return ROOT.kCyan
        if 'scharm_400_100' == name: return ROOT.kMagenta
        if 'scharm_400_200' == name: return ROOT.kBlack
        if 'scharm_400_300' == name: return ROOT.kMagenta+3
        if 'scharm_500_1' == name: return ROOT.kOrange-3
        if 'scharm_500_100' == name: return ROOT.kOrange-3
        if 'scharm_500_200' == name: return ROOT.kCyan
        if 'scharm_500_300' == name: return ROOT.kCyan
        if 'scharm_500_400' == name: return ROOT.kMagenta+3
        if 'scharm_500_450' == name: return ROOT.kMagenta+3
        if 'scharm_600_1' == name: return ROOT.kGreen
        if 'scharm_600_100' == name: return ROOT.kOrange-3
        if 'scharm_600_200' == name: return ROOT.kBlue
        if 'scharm_600_300' == name: return ROOT.kMagenta+3
        if 'scharm_600_400' == name: return ROOT.kMagenta+3
        if 'scharm_600_500' == name: return ROOT.kMagenta+3
        if 'scharm_700_1' == name: return ROOT.kGreen
        if 'scharm_700_100' == name: return ROOT.kOrange-3
        if 'scharm_700_200' == name: return ROOT.kBlue
        if 'scharm_700_300' == name: return ROOT.kMagenta+3
        if 'scharm_700_400' == name: return ROOT.kMagenta+3
        if 'scharm_700_500' == name: return ROOT.kMagenta+3

        if 'stop_100_70' == name: return ROOT.kSpring
        if 'stop_150_75' == name: return ROOT.kOrange+3
        if 'stop_175_100' == name: return ROOT.kOrange+3
        if 'stop_200_125' == name: return ROOT.kBlue
        if 'stop_250_175' == name: return ROOT.kGreen
        if 'stop_300_240' == name: return ROOT.kPink
        if 'stop_350_300' == name: return ROOT.kPink-5
        if 'stop_400_350' == name: return ROOT.kYellow

        print "ERROR:", name, "not recognised"

def printRGB(sample, isDan):
    print ' '.join(['{:.3f}'.format(x) for x in getRGB(sample, isDan)])

def getRGB(sample, isDan):
    code = getColour(sample)
    color = ROOT.gROOT.GetColor(code)
    return color.GetRed(), color.GetGreen(), color.GetBlue()

if __name__ == '__main__':
    run()
