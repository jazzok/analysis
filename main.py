#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Для совместимости с Python 3.2
from __future__ import print_function, division, absolute_import
#Импортируем библиотеки
import sys, os, getopt;
#Импортируем библиотеку NumPy
import numpy;
#Импортируем библиотеку Math
import math;
#Импортируем один из пакетов Matplotlib
import pylab;
#Импортируем пакет со вспомогательными функциями
from matplotlib import mlab;
####

class Analysis:
	"""docstring for Analysis"""

	arrayAngelPlus = []
	arrayAngelMinus = []
	arrayOshPlus = []
	arrayOshMinus = []

	def __init__(self,filename):		
		self.filename = filename
		self.checkFile()
		self.proc()

	def proc(self):		
		self.stat()
		self.display()

	def checkFile(self):
		if os.path.exists(self.filename):
			if os.path.isfile(self.filename):
				self.loadFile()
	

	def loadFile(self):
		try:
			dataFile = open(self.filename, 'r+')			
  			for (line) in dataFile:
  				self.arrayAngelPlus.append(line.split()[0])
  				self.arrayAngelMinus.append(line.split()[1])
  				self.arrayOshPlus.append(line.split()[2])
  				self.arrayOshMinus.append(line.split()[3])
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

	def stat(self):
		#	Среднее арифметическое значение
		#	Среднее взвешенное значение (медиана)
		#	Дисперсия случайной величины
		#	Стандартное отклонение
		#	Погрешности выборки		
		pass

	def display(self):
		data = "test"
		pl = Plot(data)
		pass

####
from numpy import *
import matplotlib.pyplot as plt

class Plot:
	"""docstring for Plot"""

	def __init__(self, filename):
		self.filename = filename
		self.load()

	def load(self):
		t = linspace(0, 3, 51)
		y1 = t**2*exp(-t**2)
		y2 = t**4*exp(-t**2)
		y3 = t**6*exp(-t**2)

		plt.plot(t, y1, 'g^',    # маркеры из зеленых треугольников
		         t, y2, 'b--',   # синяя штриховая
		         t, y3, 'ro-')   # красные круглые маркеры,
		                         # соединенные сплошной линией

		plt.xlabel('t')
		plt.ylabel('y')
		plt.title('Plotting with markers')
		plt.legend(['t^2*exp(-t^2)',
		            't^4*exp(-t^2)',
		            't^6*exp(-t^2)'],    # список легенды
		            loc='upper left')    # положение легенды
		plt.show()
		pass

	def show(self):
		pass

###
class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg
        pass

###
def main(argv):
    try:
        try:            
            anal = Analysis(argv)
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2

###

import argparse
if __name__ == "__main__":
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('-f', '--file', action="store", dest="filename", help="input file", default='test.txt')	
	parser.add_argument('--version', action='version', version='%(prog)s 0.1')
	arg = parser.parse_args() 	
	pathFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + arg.filename
	sys.exit(main(pathFile))
