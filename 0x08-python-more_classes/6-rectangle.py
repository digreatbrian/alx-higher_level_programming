#!/usr/bin/python3
'''Representation of a Rectangle'''

class Rectangle:
	'''A Rectangle representation'''
	number_of_instances = 0
	def __init__(self, width=0, height=0):
		self.height = height
		self.width = width
		Rectangle.number_of_instances += 1
	
	@property
	def width(self):
		'''Gets the rectangle width'''
		return self.__width
	
	@width.setter
	def width(self, value):
		'''Sets rectangle width'''
		if not isinstance(value, int):
		 	raise TypeError('width must be an integer')
		elif value < 0:
		 	raise ValueError('width must be >= 0')
		self.__width = value
		 
	@property
	def height(self):
		'''Gets the rectangle height'''
		return self.__height
	
	@height.setter
	def height(self, value):
		'''Sets rectangle height'''
		if not isinstance(value, int):
		 	raise TypeError('height must be an integer')
		elif value < 0:
		 	raise ValueError('height must be >= 0')
		self.__height = value
		
	def area(self):
		'''Returns the Area'''
		return self.width * self.height
		
	def perimeter(self):
		'''Returns the perimeter'''
		return (self.width + self.height) * 2
		
	def __str__(self):
		'''String representation'''
		s = ""
		for i in range(self.height):
			if i > 0:
				s += '\n'
			s +=  '#' * self.width 
		return s
		
	def __repr__(self):
		'''Actual string representation'''
		return 'Rectangle({height}, {width})'.format(height=self.height, width=self.width)
		
	def __del__(self):
		'''Method called on delete'''
		if Rectangle.number_of_instances > 0:
			Rectangle.number_of_instances -= 1
		print('Bye rectangle...')
