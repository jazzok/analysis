#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#	Для совместимости с Python 3.2
from __future__ import print_function, division, absolute_import

#	Импортируем библиотеки
import argparse, sys, os;
import scipy as sp
import matplotlib.pyplot as plt
from scipy import stats
from numpy import random, mean, var, std

import scipy.fftpack
import pylab
from scipy import pi

class Analysis:
	"""docstring for Analysis"""

	arrayAngelPlus = []
	arrayAngelMinus = []
	arrayOshPlus = []
	arrayOshMinus = []

	def __init__(self,filename):		
		self.filename = filename		
		self.proc()

	def proc(self):
		self.checkFile()
		self.calc()
		self.display()

	def checkFile(self):
		if os.path.exists(self.filename):
			if os.path.isfile(self.filename):
				self.loadFile()
	

	def loadFile(self):
		try:
			dataFile = open(self.filename, 'r+')			
  			for (line) in dataFile:
  				self.arrayAngelPlus.append(float(line.split()[0]))
  				self.arrayOshPlus.append(float(line.split()[1]))
  				self.arrayAngelMinus.append(float(line.split()[2]))
  				self.arrayOshMinus.append(float(line.split()[3]))
  			dataFile.close()
		except IOError as (errno, strerror):
			print ("I/O error({0}): {1}",format(errno, strerror))
			sys.exit('Open file error!')
		except ValueError:
			print ("Не могу преобразовать данные в целое.")
			sys.exit('Open file error!')
		except:
			print ("Неизвестная ошибка:", sys.exc_info()[0])
			sys.exit('Open file error!')
			raise
		finally:
			dataFile.close()

	def calc(self):				
		#	Среднее взвешенное значение (медиана)
		medianOshPlus = sp.median(self.arrayOshPlus)
		medianOshMinus = sp.median(self.arrayOshMinus)
		print ("medianOshMinus =", medianOshPlus)
		print ("medianOshMinus =", medianOshMinus)
		#	среднее значение
		meanOshPlus = mean(self.arrayOshPlus)
		meanOshMinus = mean(self.arrayOshMinus)
		print ("meanOshPlus =", meanOshPlus)
		print ("meanOshMinus =", meanOshMinus)
		#	дисперсия
		varOshPlus = var(self.arrayOshPlus)
		varOshMinus = var(self.arrayOshMinus)
		print ("varOshPlus =", varOshPlus)
		print ("varOshMinus =", varOshMinus)
		#	СКО
		stdOshPlus = std(self.arrayOshPlus)
		stdOshMinus = std(self.arrayOshMinus)
		print ("stdOshPlus =", stdOshPlus)
		print ("stdOshMinus =", stdOshMinus)		
		pass

	def display(self):
		self.chartError()
		#self.chartBacklash()
		#self.chartFFT()
		pass

	def chartError(self):
		plt.plot(self.arrayAngelPlus, self.arrayOshPlus,
				 self.arrayAngelMinus, self.arrayOshMinus)		
		plt.xlabel('Angel')
		plt.ylabel('Error')
		plt.title('osc')
		plt.legend(['osc'], loc='upper right')
		plt.show()

	def chartBacklash(self):		
		plt.plot(self.arrayAngelPlus,self.arrayOshPlus)
		plt.xlabel('Angel', size=10)
		plt.ylabel('Error', size=10)
		plt.title('osc', size=12)
		plt.legend(['osc'], loc='upper right')
		plt.show()

	def chartFFT(self):
		#self.arrayOshPlus
		FFT = abs(scipy.fft(self.arrayOshPlus))
		freqs = scipy.fftpack.fftfreq(self.arrayOshPlus, 25)
		plt.plot(freqs,20*scipy.log10(FFT),'x')
		plt.show()
		pass


###
def main(argv):
    anal = Analysis(argv)    

###
if __name__ == "__main__":
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('-f', '--file', action="store", dest="filename", help="input file", default='test.txt')	
	parser.add_argument('--version', action='version', version='%(prog)s 0.1')
	arg = parser.parse_args() 	
	pathFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + arg.filename
	sys.exit(main(pathFile))
