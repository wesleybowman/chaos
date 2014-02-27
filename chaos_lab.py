import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import os

#Use this to clear the command history in windows, e.g clear()
clear=lambda: os.system('cls')

#Defining function
def logistics(x0,A,n=100):
	'''Iterates through the logistic equation and gives x iteratively'''
	global x,y
	x=[]
	y=[]
	j=0
	x.append(A*x0*(1-x0))
	y.append(j)
	for i in range(0,n+1):
		i=A*x[i]*(1-x[i])
		x.append(i)

		j+=1
		y.append(j)

#Using a while loop to continuously ask user for input
while True:

	#This try except sequence will do the task unless it gets a KeyboardInterupt error, and if it does it
	#will exit the while loop
	try:
		#Clear the screen then inform the user on how to work the program.
		clear()
		print "\nTo exit the program press Del then Ctrl+C \n"
		print "If no N is entered, the default value is 100 \n"

		#Get user input
		a=raw_input("x0: ")
		b=raw_input("A: ")
		c=raw_input("N: ")
		#Make user input work with the function defined
		a=float(a)
		b=float(b)
		if c == '':
			logistics(a,b)
		else:
			c=int(c)
			logistics(a,b,c)

		#run function
		#logistics(a,b,c)

		#Create Figure
		fig=plt.figure()
		ax = fig.add_subplot(111) #only 1 figure, (211) would make 2 figures horizontally

		#ax=plt.axes(xlim=(0,1),ylim=(0,1))   This sets your own axes

		#autoscale axes
		ax.autoscale()

		#set x and y labels
		ax.set_ylabel(r'$x_{n+1}$', fontsize=20)
		ax.set_xlabel(r'$n$', fontsize=20)

		#show grid
		ax.grid(True)

		#plot the scatter plot
		plt.scatter(y,x)

		#show the scatter plot
		plt.show()

	#Get the KeyboeardInterupt exception to exit the while loop
	except KeyboardInterrupt as k:
		print "\n User stopped the program"
		break

