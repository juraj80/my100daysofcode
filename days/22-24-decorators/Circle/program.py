from circle import Circle

c = Circle(5)
print(c.radius)

print(c.area)

c.radius = 2
print(c.area)

#c.area = 100

print(c.cylinder_volume(height=4))

#c.radius = -1

c = Circle.unit_circle()

print(c.radius)

