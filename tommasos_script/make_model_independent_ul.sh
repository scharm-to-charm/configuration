#!/usr/bin/env bash

# safety set: quit on nonzero return code, quit on unset variable
set -eu

export PYTHONPATH=$(dirname $(which HistFitter.py))/../python

# set counts as environment variables. This is a horrible hack, but
# the same could be said for all of HistFitter.

# each array contains one of the inputs, there are only three:
# number of data events, number of background events, and background error

ndata=([150]=19   [200]=11   [250]=4   )
nbkgd=([150]=29.6 [200]=16.3 [250]=8.21)
bgerr=([150]=5.57 [200]=3.46 [250]=1.94)

# we make a subdirectory to fill with all HistFitter's barf
mkdir -p barf
cd barf

# build workspaces
for reg in 150 200 250 ; do
    echo ===================== doing $reg ===========================
    export REGION=$reg
    export NDATA=${ndata[$reg]}
    export NBKGD=${nbkgd[$reg]}
    export BGERR=${bgerr[$reg]}
    HistFitter.py -w -f ../UpperLimit2013.py > /dev/null
done

# NOTE: I've hacked UpperLimitTable.py to simplify the arguments, this
# won't work unless you check out the version of Histfitter here:
# https://github.com/dguest/HistFitter
# Fortunately, the script will quit at this point if anything goes wrong
# so you can run UpperLimitTable yourself.

WS_TAIL=SPlusB_combined_NormalMeasurement_model.root
WORKSPACES=$(echo results/UpperLimitScharm{150,200,250}/$WS_TAIL)
UpperLimitTable.py $WORKSPACES > /dev/null
UpperLimitTable.py $WORKSPACES -n 30