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

import argparse
class Parser:
	"""docstring for Parser"""

	def __init__(self, arg):
		self.arg = arg
		parser = argparse.ArgumentParser()
		subparsers = parser.add_subparsers(help='List of commands')
		# A list command
		list_parser = subparsers.add_parser('list', help='List contents')
		list_parser.add_argument('dirname', action='store', help='Directory to list')

###
class Analysis:
	"""docstring for Analysis"""

	def __init__(self,arg):
		self.arg = arg
		self.loadFile()

	def loadFile(self):
		try:
			dataFile = open(self.arg, 'r+')			
			line = dataFile.readline()  				
			print(line)
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
	#def run():

####
from numpy import *
import matplotlib.pyplot as plt

class Plot:
	"""docstring for Plot"""

	def __init__(self, arg):
		self.arg = arg

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
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])            
            par = Parser("C:/123")
            pathFile = "D:/Projects/analysis/PPGN-A.TXT"
            anal = Analysis(pathFile)
            data = "test"
			#plot = Plot(data)
        except getopt.error, msg:
             raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

###
if __name__ == "__main__":
	sys.exit(main())
