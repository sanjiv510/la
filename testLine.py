#! /usr/bin/python -tt
from nose.tools import *
from  vector import Vector 
from line import Line

def test_lines():
	n1 = Vector([4.046, 2.836])
	c1 = 1.21

	n2 = Vector([10.115, 7.09])
	c2 = 3.025

	l1 = Line(n1, c1)
	l2 = Line(n2,c2)

	#print "l1 is parallel to l2: ", l1.is_parallel_to(l2)
	print "l1 is same as l2: ", l1 ==l2
	if l1.intersects(l2):
		intersection = l1.intersection_with(l2)
		print "intersection: ", intersection
	else:
		print "No intersection"
	
	print "-"*60

	n1 = Vector([7.204, 3.182])
	c1 = 8.68

	n2 = Vector([8.172, 4.114])
	c2 = 9.883

	l1 = Line(n1, c1)
	l2 = Line(n2,c2)

	#print "l1 is parallel to l2: ", l1.is_parallel_to(l2)
	print "l1 is same as l2: ", l1 ==l2
	if l1.intersects(l2):
		intersection = l1.intersection_with(l2)
		print "intersection: ", intersection
	else:
		print "No intersection"
	
	print "-"*60
	
	n1 = Vector([1.182, 5.562])
	c1 = 6.744

	n2 = Vector([1.773, 8.343])
	c2 = 9.525

	l1 = Line(n1, c1)
	l2 = Line(n2,c2)

	#print "l1 is parallel to l2: ", l1.is_parallel_to(l2)
	print "l1 is same as l2: ", l1 ==l2
	if l1.intersects(l2):
		intersection = l1.intersection_with(l2)
		print "intersection: ", intersection
	else:
		print "No intersection"
	

def test_is_parallel():
	n1 = Vector([1,1])
	c1 = 1
	l1 = Line(n1,c1)
	n2 = Vector([-3,-3])
	c2 = -3
	l2 = Line(n2,c2)

	#print l1, l2
	assert l1.is_parallel_to(l2)


# n = Vector([2,3])
# k = 6

# l1 = Line(n,k)

# print "Line l1: ", l1