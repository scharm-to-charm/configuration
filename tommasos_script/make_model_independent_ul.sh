#!/usr/bin/env bash

export PYTHONPATH=$(dirname $(which HistFitter.py))/../python

# set counts as environment variables. This is a horrible hack, but
# the same could be said for all of HistFitter.

# each array contains one of the inputs, there are only three:
# number of data events, number of background events, and background error

ndata=([150]=19   [200]=11   [250]=4   )
nbkgd=([150]=29.6 [200]=16.3 [250]=8.21)
bgerr=([150]=5.57 [200]=3.46 [250]=1.94)

# build workspaces
for reg in 150 200 250 ; do
    echo ===================== doing $reg ===========================
    export REGION=$reg
    export NDATA=${ndata[$reg]}
    export NBKGD=${nbkgd[$reg]}
    export BGERR=${bgerr[$reg]}
    HistFitter.py -w -f UpperLimit2013.py
done
