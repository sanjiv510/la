#! /usr/bin/python -tt
from  vector import Vector 
from line import Line

n1 = Vector([1,1])
c1 = 1
l1 = Line(n1,c1)
n2 = Vector([-3,-3])
c2 = -3
l2 = Line(n2,c2)

print "l1 || l2: ", l1.is_parallel_to(l2)


n = Vector([2,3])
k = 6

l1 = Line(n,k)

print "Line l1: ", l1