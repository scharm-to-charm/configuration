#!/usr/bin/env python2.7
"""dump sbottom colors"""
import ROOT
from ROOT import TColor, TString


color_dict = {
    'other':('#FFA500','orange'),
    'Wjets':('#FFFF00','yellow'),
    'Zjets':('#008000','green' ),
    'top':('#0000FF',  'blue'  ),
    }
signal_list = [
    ('#800080', 'purple'),
    ('#00FFFF', 'cyan')
    ]

for num, sig in enumerate(signal_list):
    color_dict['signal_{}'.format(num)] = sig

for proc, (color, cname) in color_dict.items():
    # data = TString(color).Data()
    rgb_str = [color[x*2+1:x*2+3] for x in range(3)]
    rgb = [float(int(x, 16)) / 255 for x in rgb_str]
    enum = TColor.GetColor(color)
    back = ROOT.gROOT.GetColor(enum)
    prt_fmt = '| {:10} | {:10} | {:.3f} {:.3f} {:.3f} | {:10} |'
    out_str = prt_fmt.format(
        proc, cname,
        back.GetRed(), back.GetGreen(), back.GetBlue(), back.GetName())
    print out_str
