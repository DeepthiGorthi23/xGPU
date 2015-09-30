import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import subprocess as sub
import os
import argparse





#Command line options
parser = argparse.ArgumentParser()
parser.add_argument('-i', dest = 'iterate', type=str, help = 'Specify the variable to iterate over: nfrequency,ntime or ntime_pipe')
parser.add_argument('--ntime',dest= 'ntime',help = 'Specify the accumulation time',default=2048)
parser.add_argument('--nfrequency',dest='nfrequency',help='Specify number of frequncy bins to use',default = 10)
parser.add_argument('--ntime_pipe',dest='ntime_pipe',help='Specify the value for ntime_pipe',default = 1024)
parser.add_argument('--nstations',dest='nstations',help='Number of antennas',default=352)
args = parser.parse_args()

ntime = args.ntime
iterate = args.iterate
nfrequency = args.nfrequency
ntime_pipe = args.ntime_pipe
nstations = args.nstations
#Iterating with respect to the variable specified by command-line options
if iterate=='nfrequency':

	nfrequency = range(1,5)



	BW = []
	for i,j in enumerate(nfrequency):
		#opening and writing to Xmake.local file that will be used to build the Makefile and 
		#edit the cuda_correlator script. 
		f = open('Xmake.local','w')
		f.write('NSTATION=%d\n'%nstations)
		f.write('NFREQUENCY=%d\n'%j)
		f.write('NTIME=%d\n'%ntime)
		f.write('NTIME_PIPE=%d\n'%ntime_pipe)
		f.close()
		#opening a subprocess in the shell in order to execute 'make clean all' and the cuda_correlator script
		m = sub.Popen('make clean all', stdout = sub.PIPE, shell=True).communicate()
		p = sub.Popen("./cuda_correlator | awk '/BW/ {print $12}'", stdout = sub.PIPE, shell = True)
		bw, error = p.communicate()
		#p.communicate() returns the bw that cuda_correlator code outputs and 
		BW.append(float(bw))
	plt.plot(nfrequency,BW)
	plt.show()

#iterating over ntime
elif iterate=='ntime':

	ntime = range(1,5)

	BW = []
	for i,j in enumerate(ntime):
		#opening and writing to Xmake.local file that will be used to build the Makefile and 
		#edit the cuda_correlator script. 
		f = open('Xmake.local','w')
		f.write('NSTATION=%d\n'%nstations)
		f.write('NFREQUENCY=%d\n'%nfrequency)
		f.write('NTIME=%d\n'%j)
		f.write('NTIME_PIPE=%d\n'%ntime_pipe)
		f.close()
		#opening a subprocess in the shell in order to execute 'make clean all' and the cuda_correlator script
		m = sub.Popen('make clean all', stdout = sub.PIPE, shell=True).communicate()
		p = sub.Popen("./cuda_correlator | awk '/BW/ {print $12}'", stdout = sub.PIPE, shell = True)
		bw, error = p.communicate()
		#p.communicate() returns the bw that cuda_correlator code outputs and 
		BW.append(float(bw))
	


	plt.plot(ntime,BW)	
	plt.show()

elif iterate=='ntime_pipe':

	ntime_pipe = range(1,5)

	BW = []
	for i,j in enumerate(ntime_pipe):
		#opening and writing to Xmake.local file that will be used to build the Makefile and 
		#edit the cuda_correlator script. 
		f = open('Xmake.local','w')
		f.write('NSTATION=%d\n'%nstations)
		f.write('NFREQUENCY=%d\n'%nfrequency)
		f.write('NTIME=%d\n'%ntime)
		f.write('NTIME_PIPE=%d\n'%j)
		f.close()
		#opening a subprocess in the shell in order to execute 'make clean all' and the cuda_correlator script
		m = sub.Popen('make clean all', stdout = sub.PIPE, shell=True).communicate()
		p = sub.Popen("./cuda_correlator | awk '/BW/ {print $12}'", stdout = sub.PIPE, shell = True)
		bw, error = p.communicate()
		#p.communicate() returns the bw that cuda_correlator code outputs and 
		BW.append(float(bw))

	plt.plot(ntime_pipe,BW)
	plt.show()




