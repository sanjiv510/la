#! /usr/bin/python -tt
from  vector import Vector 



v = Vector([8.462,7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])

print "v.cross(w): ", v.cross(w)
print " area_parallogram: ", v.area_parallogram(w)
print " area_tringle: ", v.area_tringle(w)


v = Vector([8.462,7.893])
w = Vector([6.984, -5.975])

print "v.cross(w): ", v.cross(w)
exit(0)

v1= Vector([3.009, -6.172, 3.629, -2.51])
b1 = Vector([6.404, -9.144, 2.759, 8.718])

print " v|| + V per", v1.component_parallel_to(b1), v1.component_orthogonal_to(b1)
vpar = v1.component_parallel_to(b1)
vort =  v1.component_orthogonal_to(b1)

print "vpar + vort: ", vpar.plus(vort)

exit(0)



# Checking for parallelism & orthogonality
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print "v.w: ", type(v.dot(w))
print "v..magnitude: ", type(v.magnitude())
print "v.w / v.mag: ", v.dot(w)/w.magnitude()





print "v is parallel to w: ", v.is_parallel_to(w)
print "v is orthogonal to w: ", v.is_orthogonal_to(w)
exit(0)

v1 = Vector([7.887, 4.138])
w1 = Vector([-8.802, 6.776])
print "v . w: ", v1.dot(w1)
exit(0)


v1= Vector([3.009, -6.172, 3.629, -2.51])
b1 = Vector([6.404, -9.144, 2.759, 8.718])

print " v|| + V per", v1.component_parallel_to(b1), v1.component_orthogonal_to(b1)
vpar = v1.component_parallel_to(b1)
vort =  v1.component_orthogonal_to(b1)

print "vpar + vort: ", vpar.plus(vort)

v1 = Vector([-9.88, -3.264, -8.159])
b1 = Vector([-2.155, -9.353, -9.473])
print "ortogonal to basis: ", v1.component_orthogonal_to(b1)

v1 = Vector([3.039, 1.879])
b1 = Vector([0.825, 2.036])
print "projection to basis v1: ", v1.component_parallel_to(b1)


exit(0)
v1 = Vector([1,-1])
print "v1: ", v1
print "magnitude: ", v1.magnitude()
print "normalized: ", v1.normalized()
print "times_scalar (*3): ", v1.times_scalar(3)
print "is_zero: ", v1.is_zero()

v1 = Vector([0,0.00000000000000000000000000000000001])
print "v1: ", v1
print "magnitude: ", v1.magnitude()
print "normalized: ", v1.normalized()
print "times_scalar (*3): ", v1.times_scalar(3)
print "is_zero: ", v1.is_zero()

# parallel vector

v1 = Vector([1,-1])

v2 = Vector([3, -3.1])
print "is_parallel_to v1: (True)", v1.is_parallel_to(v2)
print "angle_in_rad: v1-v2", v1.angle_in_rad(v2)
print "angle_in_deg: v1-v2", v1.angle_in_deg(v2)
