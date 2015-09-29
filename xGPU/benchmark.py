import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import subprocess as sub
import os
import argparse


#Going to make changes to the limits Npipe can take. Trying to submit this to the branch on the master

#np.genfromtxt('plotfile.txt',delimiter=',',names=['x','y'])
ntime=2048
n_frequency = range(1,5)
npipe=1024
nstation = 352

parser = argparse.ArgumentParser()
parser.add_argument("-i", help = 'Specify the variable to iterate over: nfrequency,ntime,ntime_pipe')







BW = []
for i,j in enumerate(n_frequency):
	#opening and writing to Xmake.local file that will be used to build the Makefile and 
	#edit the cuda_correlator script. 
	f = open('Xmake.local','w')
	f.write('NSTATION=%d\n'%nstation)
	f.write('NFREQUENCY=%d\n'%j)
	f.write('NTIME=%d\n'%ntime)
	f.write('NTIME_PIPE=%d\n'%npipe)
	f.close()
	#opening a subprocess in the shell in order to execute 'make clean all' and the cuda_correlator script
	m = sub.Popen('make clean all', stdout = sub.PIPE, shell=True).communicate()
	p = sub.Popen("./cuda_correlator | awk '/BW/ {print $12}'", stdout = sub.PIPE, shell = True)
	bw, error = p.communicate()
	#p.communicate() returns the bw that cuda_correlator code outputs and 
	BW.append(float(bw))
	#print BW[i]
	#print type(BW[i])
		
	
plt.plot(n_frequency,BW)	
plt.show()
#os.system('make clean all')
#os.system('./xcorrelator')

#
#f = open('xmake.txt','w')
#f.write('NFREQUENCY=%d\n'%nfrequency)
#f.write('NTIME=%d\n'%ntime)
#f.write('NPIPE=%d\n'%npipe)
#f.close()


#os.system('./cuda_correlator | grep /Users/zara/Documents/xGPU 
#p = sub.Popen('pwd | echo',stdout = sub.PIPE, shell=True)

#p = sub.Popen("awk '/BW/ {print $12}",stdout = sub.PIPE)
# = p.communicate()

