#Callum Browm
#23-09-14
#Assignment statement spot check - Question 1

width = float(input("Please enter the width of the pool in metres: "))
length = float(input("Please enter the length of the pool in metres: "))
depth = float(input("Please enter the depth of the pool in metres: "))

main_section_volume = width*length*depth
circle_radius = width/2
circle_area = 3.14*(circle_radius*circle_radius)
half_circle_volume = (circle_area/2)*depth
pool_volume = (main_section_volume+half_circle_volume)

print("The volume of the pool is: {0} metre(s)".format(pool_volume))
      



