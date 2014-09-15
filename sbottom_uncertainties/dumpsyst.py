#!/usr/bin/env python3.3

import yaml

from Sbottom_theoryUncertainties_relative import *

sampdict = {
    'W': 'Wjets',
    'Z': 'Zjets',
    }

regdict = {
    'SRA150': 'signal_mct150',
    'SRA200': 'signal_mct200',
    'SRA250': 'signal_mct250',
    'CRAemu': 'cr_t',
    'CRA1l': 'cr_w',
    'CRA2l': 'cr_z'
    }

_rel_key = 'relative_systematics'

def run():
    systdict = {}
    loc = dict(globals())
    for name, syst in loc.items():
        if isinstance(syst, Systematic):
            sample, _, region = name.partition('Theory')
            dansamp = sampdict.get(sample, sample)
            danreg = regdict.get(region)
            if danreg is None:
                pass
            else:
                systdict[syst.name, danreg, dansamp] = list(syst.range)

    print(yaml.dump({_rel_key: _nest(systdict)}))

def _set_value(nest_dict, key_list, value):
    if len(key_list) == 1:
        nest_dict[key_list[0]] = value
        return
    last_key = key_list.pop()
    inner = nest_dict.setdefault(last_key, {})
    _set_value(inner, key_list, value)

def _nest(flat_dict):
    nested = {}
    for keys, rg in flat_dict.items():
        _set_value(nested, list(reversed(keys)), rg)
    return nested

if __name__ == '__main__':
    run()
