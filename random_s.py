''' Belajar AI Ahadian Akbar 10/13/2013 <-> random search '''
import random
import math
import string
from random import randint
huruf 	= 'abcdefghijklmnopqrstuvwxyz !,.'
goal  	= 'ahadian akbar love real madrid!'
e 	  	= 0
pop		= 10
iters   = 200
target  = []
for i in range(0,len(goal)):
	target.insert(i,'')

def krom():
	s =  ''
	while len(s) < len(goal):
		s += random.choice(huruf)
	return s
	
def acakkata():
	ind = []
	for i in range(0,pop): 
		krs = krom() 
		ind.append(krs)
	return ind

def fitnes(n):
	fit = 0 
	for i,c in enumerate(n): fit += abs(ord(c) - ord(goal[i]))
	return fit	
	
def randomSearch(n):
	for i in range(0,len(goal)): 
		if ord(n[i]) == ord(goal[i]):
			if target[i] == '':
				target.insert(i,n[i])
			else:
				target[i]= n[i]
		else:
			if target[i] == '':
				target[i] = n[i]	
	hasil = ''.join(target[:len(goal)]) 
	return hasil
s = ''
for i in range(0,iters):
	kandidat = acakkata()
	s = randomSearch(kandidat[0])
	print 'solusi =>',s,' fitnes=>',fitnes(s)
