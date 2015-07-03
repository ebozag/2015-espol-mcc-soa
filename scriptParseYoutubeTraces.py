#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 08:31:22 2015

@author: Edwin Boza

This script will convert the traces from Youtube detailed in [1], into the format required 
for the YCSB-rp (https://github.com/ebozag/YCSB-rp) in order to execute trace-driven tests.

The output will be in the form "COMMAND,ID" (without the quotes), where COMMAND is one of READ,
INSERT,UPDATE,SCAN, and ID will be the key for the record in the DB.

Usage:

    ./scriptParseYoutubeTraces.py -f <tracefile> [-o <outputs>]
    
    tracefile  Is the path and name of the file containing the Youtube trace.
    outputs    Is the number of output files, should be equal to the number of
               threads to be used in YCSB-rp.
    

[1] Michael Zink, Kyoungwon Suh, Yu Gu and Jim Kurose, "Watch Global Cache Local: YouTube
    Network Traces at a Campus Network - Measurements and Implications", 2008 IEEE MMCN.

Original trace example:
    1189828805.208862 63.22.65.73 140.8.48.66 GETVIDEO lML9dik8QNw 158.102.125.12 
    1189828810.212831 63.22.65.73 35.139.191.73 GETVIDEO bBXyB7niEc0&origin 105.136.66.5 
"""

import sys, getopt, re
from itertools import cycle

def main(argv):
    ### Put the arguments in variables.
    traceFilename = ''
    numDestinationFiles = 1
    try:
        opts, args = getopt.getopt(argv,"hf:o:",["tracefile=","outputs="])
    except getopt.GetoptError:
        print 'scriptParseYoutubeTraces.py -f <tracefile> [-o <outputs>]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'scriptParseYoutubeTraces.py -f <tracefile> [-o <outputs>]'
            sys.exit()
        elif opt in ("-f", "--tracefile"):
            traceFilename = arg
        elif opt in ("-o", "--outputs"):
            numDestinationFiles = arg
    if traceFilename == '':
        print 'ERROR: Must specify a trace filename.'
        print 'scriptParseYoutubeTraces.py -f <tracefile> [-o <outputs>]'
        sys.exit(1)
    if int(numDestinationFiles) <= 0 or traceFilename == '':
        print 'ERROR: <outputs> must be a number greater than 0.'
        sys.exit(1)
    
    ### Open the output files, they will be truncated.
    outputFiles=[]
    for i in range(1, int(numDestinationFiles)+1):
        filename = 'parsedFile-%d.dat' % i
        outputFiles.append(open(filename, 'w') )
    
    poolOutputFiles = cycle(outputFiles)
    
    ### Open the file in read mode, and parse each line to obtain the command 
    ### and the id.
    with open (traceFilename, "r") as traceFile:
        for line in traceFile:
            parsedEvent = re.findall(r'.*\s.*\s.*\s(.*)\s(.*)\s.*',line.rstrip())
            if parsedEvent[0][0] in ['GETVIDEO','LLNWD']:
               poolOutputFiles.next().write('READ,' + parsedEvent[0][1]+'\n')
    
    for fh in outputFiles:
            fh.close()

if __name__ == "__main__":
   main(sys.argv[1:])
