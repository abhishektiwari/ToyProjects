#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

PI = 3.14

class Shape(object):
	"""
	Shape parameters
	"""
	def __init__(self, arg1, arg2):
		print "before init Shape"
		# Prefixing a name with two underscores makes that name 
		# unavailable outside the class. Use access methods get/set
		self.__a = arg1
		self.__b = arg2
		print "after init Shape"
		# object is superclass of base class
		# super(Shape, self).__init__(arg1, arg2)
	def get_a(self):
		return self.__a
	def get_b(self):
		# same as self.b, but returns copy of original parameter
		return self.__b

class Rectangle(Shape):
	"""
	Rectangle type
	"""
	def __init__(self, arg1, arg2):
		print "before init Rectangle"
		super(Rectangle, self).__init__(arg1, arg2)
		print "after init Rectangle"
	def rarea(self):
		area = self.get_a()*self.get_b()
		print "Rectangle area:", area

class Square(Shape):
	"""
	Square Type
	"""
	def __init__(self, arg1, arg2):
		print "before init Square"
		super(Square, self).__init__(arg1, arg2)
		print "after init Square"
	def sarea(self):
		area1 = self.get_a()*self.get_a()
		print "Square area 1:", area1
		area2 = self.get_b()*self.get_b()
		print "Square area 2:", area2

class Triangle(Shape):
	"""
	Triangle Type
	"""
	def __init__(self, arg1, arg2):
		print "before init Triangle"
		super(Triangle, self).__init__(arg1, arg2)
		print "after init Triangle"
	def tarea(self):
		area = 0.5*self.get_a()*self.get_b()
		print "Triangle area:", area

class Circle(Shape):
	"""
	Circle Type
	"""
	def __init__(self, arg1, arg2):
		print "before init Circle"
		super(Circle, self).__init__(arg1, arg2)
		print "after init Circle"
	def carea(self):
		area1 = PI*self.get_a()*self.get_a()
		print "Circle area 1:", area1
		area2 = PI*self.get_b()*self.get_b()
		print "Circle area 2:", area2


class Geom(Rectangle, Square, Triangle, Circle):
	"""
	Inherited from basic geometry types, Note that order of base classed
	is important. Initialization occurs in same order.
	"""
	def __init__(self, arg1, arg2):
		print "before init Geom R S T C"
		super(Geom, self).__init__(arg1, arg2)
		print "after init Geom R S T C"
		# In Python 3 super()
		# super().__init__(arg1, arg2)
	def geom_area(self):
		super(Geom, self).rarea()
		super(Geom, self).sarea()
		super(Geom, self).tarea()
		super(Geom, self).carea()
		# In Python 3 super()
		# super().rarea()
		# super().sarea()
		# super().tarea()
		# super().carea()

#>>> t1 = Geom(3,6)
#before init Geom R S T C
#before init Rectangle
#before init Square
#before init Triangle
#before init Circle
#before init Shape
#after init Shape
#after init Circle
#after init Triangle
#after init Square
#after init Rectangle
#after init Geom R S T C
#>>> t1.geom_area()
#Rectangle area: 18
#Square area 1: 9
#Square area 2: 36
#Triangle area: 9.0
#Circle area 1: 28.26
#Circle area 2: 113.04


