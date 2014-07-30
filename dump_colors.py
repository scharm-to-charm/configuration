#!/usr/bin/env python2.7
"""dump scharm colors"""
import ROOT
from ROOT import TColor, TString
import warnings

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

prt_fmt = '| {:10} | {:11} | {:5.3f} | {:5.3f} | {:5.3f} | {rn:11} |'
leg_fmt = prt_fmt.replace(':5.3f',':5').replace(':',':^')

colorbox = (' <span style="background-color: {color}; padding-left: 5cm">'
            '</span> ')
prt_fmt += colorbox + '|'
leg_fmt += '*Color*'.center(len(colorbox)) + '|'

legs = ['*process*', '*html name*'] + ['*{}*'.format(x) for x in 'rgb']
print leg_fmt.format(*legs, rn='*root name*', color='#000000')
for proc, (color, cname) in color_dict.items():
    # data = TString(color).Data()
    rgb_str = [color[x*2+1:x*2+3] for x in range(3)]
    rgb = [float(int(x, 16)) / 255 for x in rgb_str]
    enum = TColor.GetColor(color)
    back = ROOT.gROOT.GetColor(enum)
    root_rgb = (back.GetRed(), back.GetGreen(), back.GetBlue())
    delta = [root - original for root, original in zip(root_rgb, rgb)]
    if any(x > 0.001 for x in delta):
        wrn = "root and html {} not the same, delta = {}".format(cname, delta)
        warnings.warn(wrn)
    out_str = prt_fmt.format(
        proc, cname, *rgb, rn=back.GetName(), color=color)
    print out_str
