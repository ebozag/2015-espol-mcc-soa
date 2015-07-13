#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 08:31:22 2015

@author: Edwin Boza


        Número de Hilos: 1, 10, 20
        Workloads: workloadc, workload-rp/youtube_traces, workload_rp/redis_traces
        Numero de ejecuciones por cada prueba/caso: 10
        Estadísticas a Obtener: Promedio de "operaciones por segundo" en cada caso.


        $PATH_YCSB_RP/bin/ycsb run redis -p redis.host=127.0.0.1 -p redis.port=6379 -P $PATH_YCSB_RP/workloads/workloadc -p operationcount=5000000 -s -threads 20 > YCSB-rp_Output_zipfian_20threads_5mOps_2.dat 2> YCSB-rp_Stats_zipfian_20threads_5mOps_2.dat


"""

import os,re
print 'Threads workloadc workload-rp_youtube workload-rp_redis'
for threads in [ '1', '10', '20' ]:
	throughtputs = ''
	for workload in [ 'workloadc', 'workload-rp_youtube', 'workload-rp_redis' ]:
		sumThroughput = float(0)
		for i in range(1,11):
			suffix = '_' + workload + '_' + threads + 'threads_5mOps_' + str(i) + '.dat'
			filename = 'YCSB-rp_Output' + suffix
			with open (filename, "r") as f:
			        for line in f:
					if "Throughput" in line:
	            				throughput = re.findall(r'.*\s.*\s(.*)',line.rstrip())
						sumThroughput = sumThroughput + float(throughput[0])
						break
		#print 'Workload:',workload,'- Threads:',threads,'- Throughput:',sumThroughput/10
		throughtputs = throughtputs + ' ' + str(sumThroughput/10)
	print threads + ' ' + throughtputs

