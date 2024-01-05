#!/usr/bin/python3
'''Representation of a Rectangle'''

class Rectangle:
	'''A Rectangle representation'''
	number_of_instances = 0
	print_symbol = '#'
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
		
	@classmethod
	def square(cls, size=0):
		'''Returns rectangle as a square'''
		return cls(size, size)
		
	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		'''Compares 2 rectangles'''
		if not isinstance(rect_1, Rectangle):
			raise TypeError('rect_1 must be an instance of Rectangle')
			
		if not isinstance(rect_2, Rectangle):
			raise TypeError('rect_2 must be an instance of Rectangle')
			
		if rect_1.area() >= rect_2.area():
			return rect_1
			
		else:
			return rect_2
			
	def __str__(self):
		'''String representation'''
		s = ""
		for i in range(self.height):
			if i > 0:
				s += '\n'
			s +=  str(self.print_symbol) * self.width 
		return s
		
	def __repr__(self):
		'''Actual string representation'''
		return 'Rectangle({height}, {width})'.format(height=self.height, width=self.width)
		
	def __del__(self):
		'''Method called on delete'''
		if Rectangle.number_of_instances > 0:
			Rectangle.number_of_instances -= 1
		print('Bye rectangle...')
