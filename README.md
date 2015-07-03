# 2015-espol-mcc-soa
Projects for the "Sistemas Operativos Avanzados" course at MCC/ESPOL

====
File: scriptParseYoutubeTraces.py 

This script will convert the traces from Youtube detailed in [1], into the format required 
for the YCSB-rp (https://github.com/ebozag/YCSB-rp) in order to execute trace-driven tests.

The output will be in the form "COMMAND,ID" (without the quotes), where COMMAND is READ,
and ID will be the key for the record in the DB.

Original trace example:
    1189828805.208862 63.22.65.73 140.8.48.66 GETVIDEO lML9dik8QNw 158.102.125.12 
    1189828810.212831 63.22.65.73 35.139.191.73 GETVIDEO bBXyB7niEc0&origin 105.136.66.5 

[1] Michael Zink, Kyoungwon Suh, Yu Gu and Jim Kurose, "Watch Global Cache Local: YouTube Network Traces at a Campus Network - Measurements and Implications", 2008 IEEE MMCN.
====
